let runtime = [];
const __time = parseInt(Date.now());


	function log(t, c, g, s) { console.log('%c' + t, (c && c.length == 6 ? 'color: #' + c + '; ' : '') + (g && g.length == 6 ? 'background-color: #' + g + '; ' : '') + (s ? 'font-weight: bold;' : '')); }
		log('Welcome my friend!', '000000', 'f5f5f5', true); 
		
		function addClass(element, className) {
		  element.classList.add(className);
		};

		function hasClass(element, className) {
			return element.classList.contains(className);
		};

		function removeClass(element, className) {
			element.classList.remove(className);
		};

		function canUseWebP() {
			var elem = document.createElement('canvas');
			if (!!(elem.getContext && elem.getContext('2d'))) {
				return elem.toDataURL('image/webp').indexOf('data:image/webp') == 0;
			}
			return false;
		}

		function loadScript(url, func) {
			var script = document.createElement('script');
			if(func) script.onload = func();
			document.head.appendChild(script);
			script.src = url;	
		};

		const throttle = (func, limit) => {
		  let lastFunc;
		  let lastRan;
		  return function() {
			const context = this;
			const args = arguments;
			if (!lastRan) {
			  func.apply(context, args);
			  lastRan = Date.now();
			} else {
			  clearTimeout(lastFunc);
			  lastFunc = setTimeout(function() {
				if ((Date.now() - lastRan) >= limit) {
				  func.apply(context, args);
				  lastRan = Date.now();
				}
			  }, limit - (Date.now() - lastRan));
			}
		  }
		};

		function on(container, event, selector, handler) {
			container.addEventListener(event, function(e){
				if (e.target.matches(selector)) {
					handler(e.target);
				} else if(e.target.parentNode.matches(selector)) {
					handler(e.target.parentNode);
				} else if(e.target.parentNode.parentNode.matches(selector)) {
					handler(e.target.parentNode.parentNode);
				};
				e.stopPropagation();
			});
		};

		function absolutePosition(el) {
			let found,
				left = 0,
				top = 0,
				width = 0,
				height = 0,
				offsetBase = absolutePosition.offsetBase;
			if (!offsetBase && document.body) {
				offsetBase = absolutePosition.offsetBase = document.createElement('div');
				offsetBase.style.cssText = 'position:absolute;left:0;top:0';
				document.body.appendChild(offsetBase);
			};
			if (el && el.ownerDocument === document && 'getBoundingClientRect' in el && offsetBase) {
				var boundingRect = el.getBoundingClientRect();
				var baseRect = offsetBase.getBoundingClientRect();
				found = true;
				left = boundingRect.left - baseRect.left;
				top = boundingRect.top - baseRect.top;
				width = boundingRect.right - boundingRect.left;
				height = boundingRect.bottom - boundingRect.top;
			};
			return {
				found: found,
				left: left,
				top: top,
				width: width,
				height: height,
				right: left + width,
				bottom: top + height
			};
		};
		
		if(canUseWebP()) {
			addClass(document.body, 'webp');
		} else {
			addClass(document.body, 'no-webp');
		};

		let body, html, height, vheight, width, vwidth = false;
		
		runtime.push({ 'id': 'sliderFunc', 'fun': function(){
			loadScript('/static/core/js/glide.js', function() {
				var glide = new Glide('#intro', {
				  type: 'carousel',
				  perView: 1,
				  focusAt: 'center'
				})

				glide.mount();
			});
		}});

		window.onload = function(ev) {
			
			body = document.body;
			html = document.documentElement;
			height = Math.max( body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight );
			vheight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
			width = Math.max( body.scrollWidth, body.offsetWidth, html.clientWidth, html.scrollWidth, html.offsetWidth );
			vwidth = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
			
			addClass(body, 'loaded');
			
			log('Page has been loaded in ' + (parseInt(Date.now()) - __time) + ' miliseconds.');
			log('Crazy fast!', '990000', 'eeeeee', true);
				
			let targets = [];
			let watched = document.querySelectorAll(".lazyLoad, .runtime, .watched");
			function getInitialPositions() {
				targets = [];
				for (key = 0; key < watched.length; key++) {
					var box = absolutePosition(watched[key]);
					watched[key].setAttribute('data-top', box.top);
					watched[key].setAttribute('data-bottom', box.bottom);
					watched[key].setAttribute('data-class', watched[key].className);
					targets.push([watched[key], watched[key].className, box.top-vheight-(width > 600 ? 200 : 400), box.bottom + (width > 600 ? 200 : 300), box.top-vheight, box.bottom]);
				};
			};
			
			const onPositionHandler = throttle(getInitialPositions, 500);	
			
			onPositionHandler();
			
			window.addEventListener('resize', (e) => {
				onPositionHandler();
				setTimeout(function(){
					onScroll(window.scrollY);
				}, 300);
			}, { capture: false, passive: true });
			
			var already = false;
			var loaded = [];
			
			const onScroll = function(where) {
				var i = 0;
				for (key in targets) {
					setTimeout(function(obj){
						
						const tag = obj[0].tagName ? obj[0].tagName.toLowerCase() : false;
						
						if(obj[2] <= where && obj[3] >= where) {
							
							if(obj[0].getAttribute('data-preloaded') != '1') {
								
								obj[0].setAttribute('data-preloaded', '1');
								obj[0].className = obj[0].className + ' preloaded';
								
								if((tag == 'img' || tag == 'iframe') && !hasClass(obj[0], 'alreadyVisible') && obj[0].src != obj[0].getAttribute("data-src")) {
									obj[0].src = obj[0].getAttribute("data-src");
								};
								
								if(tag == 'div' && hasClass(obj[0], 'runtime')) {
									runtime.forEach(function(have){
										if(have.id == obj[0].getAttribute('id') && !loaded.includes(have.id)) {
											have.fun();
											loaded.push(have.id);
										};
									});
								};
								
							};
						};
						
						onPositionHandler();
						
					}, 1, targets[key]);
					
					setTimeout(function(obj){
						
						const tag = obj[0].tagName ? obj[0].tagName.toLowerCase() : false;
						
						if(obj[4] <= where && obj[5] >= where) {
							
							obj[1] = obj[0].className.replace(' visible', '');
							obj[0].className = obj[1] + ' visible';
							
							if(obj[0].getAttribute('data-already-visible') != '1') {
								obj[0].setAttribute('data-already-visible', '1');
								obj[0].className = obj[0].className + ' alreadyVisible';
							}
							
						} else {
							removeClass(obj[0], 'visible');
						}
						
						onPositionHandler();
						
					}, i*17, targets[key]);
					
					i++;
				}

				if(where > 200) {
					if(!already) {
						addClass(body, 'changed');
						already = true;
					}
				} else {
					removeClass(body, 'changed');
					already = false;
				}
			};
			
			onScroll(window.scrollY);
			
			var goToTop = document.getElementById('goToTop');
			goToTop.onclick = function(){
				scrollTo(0,0);
			};
			
			const onScrollHandler = throttle(onScroll, 200);	
			let ticking = false;
			let last_known_scroll_position = 0;

			window.addEventListener('scroll', (e) => {
			  last_known_scroll_position = window.scrollY;
			  if (!ticking) {
				window.requestAnimationFrame( () => {
					onScrollHandler(last_known_scroll_position);
				  ticking = false;
				});
				ticking = true;
			  }
			}, { capture: false, passive: true });
			
			var i, toggles = document.getElementsByClassName('toggle');
			for (i = 0; i < toggles.length; i++) {
				var obj = toggles[i];
				setTimeout(function(element) {
					element.onclick = function(ev) {
					
						ev.stopPropagation();
						ev.cancelBubble = true;
						
						var id = element.attributes.rel.value;
						var objX = document.getElementById(id);
						var height = absolutePosition(objX).height;
						
						if(height > 0) {
							console.log('Zwijam');
							objX.style.maxHeight = '0px';
							objX.dataset.height = height;
							element.classList.remove('toggled');
						} else {
							console.log('Rozwijam');
							objX.style.maxHeight = objX.dataset.height + 'px';
							element.classList.add('toggled');
						};
						
						objX.classList.toggle('dead');
						
						setTimeout(function(){
							getInitialPositions();
						}, 1300);
						
						setTimeout(function(){
							onScroll(window.scrollY);
						}, 1400);
						
					};
				}, 1, toggles[i]);
			};			

			let mobileMenuStatus = false;
			const menuMenu = document.getElementById('menu-menu');
			const mobileMenu = document.getElementById('mobileMenu');
			if(menuMenu && mobileMenu) mobileMenu.onclick = () => {
				if(mobileMenuStatus){
					menuMenu.className = 'navigation';
					mobileMenuStatus = false;
				} else {
					menuMenu.className = 'navigation__opened navigation';
					mobileMenuStatus = true;
				};
			};
			
		};
	


// START CONTACT FORM

window.addEventListener('load', (event) => {
    var contactFormDOM = document.getElementById("contactFormDOM");
    document.getElementById("contactFormSubmitButton").addEventListener("click", function(){
        contactFormDOM.classList.add("submitted");
    });
    contactFormDOM.onsubmit = function(event) {
        contactFormDOM.innerHTML = '<p class="h1">Dziękujemy za kontakt. W najbliższym czasie skontaktuje się z Tobą jeden z naszych ekspertów.</p>';
        event.preventDefault();
    };
});
		
// END CONTACT FORM
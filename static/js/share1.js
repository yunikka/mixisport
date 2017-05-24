//---------------------------------
//     WebDiscover Share API
//---------------------------------

if ( ! window.WD ) window.WD = {};
if ( ! WD.Share ) {

	WD.Share = {
		_popups: [],
		_post_url: [],

		button: function (post_url, but, index) {

			// Index of window
			if ( index === undefined ) {
				this._popups.push(false);
				index = this._popups.length - 1;
			}

			// Define post_url
			if ( ! post_url || post_url == '' ) {
				this._post_url[index] = WD.Share._loc;
			} else {
				this._post_url[index] = post_url;
			}

			// Define buttin params
			if ( ! but ) but = { id: 1 };
			if ( but === but.toString() ) but = { id: 1, text: 'Поделиться', width: 100 };
			
			if ( ! but.text ) but.text = 'Поделиться';
			if ( ! but.width || but.width <= 100 ) but.width = 100;

			if ( but.id == 1 ) {
				but_style = 'width:50px; height:55px;';
			} else if ( but.id == 2 || but.id == 3 || but.id == 4 ) {
				but_style = 'width:' + but.width + 'px; height:20px;';
			} else {
				but_style = '';
			}
			
			but_id = '?id=' + but.id;
			but_text = '&text=' + encodeURIComponent(but.text);
			but_url = encodeURIComponent(this._post_url[index]);
			but_url_full = '&link=' + but_url;
			
			if ( but.id != 5 ) {
				return '<iframe src="http://webdiscover.ru/engine/api/share/share.button.php' + but_id + but_url_full + but_text + '" allowtransparency="true" frameborder="0" scrolling="no" style="' + but_style + ' overflow:hidden;"></iframe>';
			} else {
				return '<a href="http://webdiscover.ru/share.php?url=' + but_url + '" onclick="WD.Share.open(\'' + but_url + '\'); return false;" target="_blank">' + but.text + '</span>';
			}

		},
		
		open: function (post_url) {
			var url = 'http://webdiscover.ru/share.php?url=' + post_url,
			width = 600,
			height = 530,
			left = (screen.width - width) / 2,
			top = (screen.height - height) / 2.7,
			popupParams = 'scrollbars=0, resizable=1, menubar=0, left=' + left + ', top=' + top + ', width=' + width + ', height=' + height + ', toolbar=0, status=0';

			newwindow = window.open(url, null, popupParams);
			if ( window.focus ) {
				newwindow.focus()
			}
			return false;
		}

	}
	
	try {
		WD.Share._loc = location.toString();
	} catch (e) {
		WD.Share._loc = '';
	}
}
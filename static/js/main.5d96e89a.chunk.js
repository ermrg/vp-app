(this.webpackJsonpapp=this.webpackJsonpapp||[]).push([[0],{72:function(e,t,n){},73:function(e,t,n){"use strict";n.r(t);var r=n(2),a=n.n(r),s=n(37),c=n.n(s),o=n(11),i=n(4),u=n(1);function p(){return Object(u.jsx)("div",{className:"home",children:Object(u.jsxs)("div",{children:[Object(u.jsxs)("div",{className:"title",children:[Object(u.jsx)("h3",{children:"\u0916\u093e\u0901\u0921\u093e\u0926\u0947\u0935\u0940 \u0917\u093e\u0909\u0901\u092a\u093e\u0932\u093f\u0915\u093e"}),Object(u.jsx)("p",{children:"\u092e\u093e\u0915\u093e\u0926\u0941\u092e , \u0930\u093e\u092e\u0947\u091b\u093e\u092a, \u092a\u094d\u0930\u0926\u0947\u0936 \u0928\u0902 \u0969"})]}),Object(u.jsx)(o.b,{to:"/vp-app/app",children:"Village Profile App"})]})})}var d=n(0),l=n.n(d),h=n(27),f=n(3),j=n(13),v=n(10),b=n(15),w=n(21),m=n(42),x=n(40),O=n(39),g=n(19),y=n.n(g),k="https://55c69b6640a7.ngrok.io/api/",N={loadCollectors:function(){return y.a.get("".concat(k,"collectors/"))},loadWada:function(){return y.a.get("".concat(k,"wards/"))},loadMarga:function(){return y.a.get("".concat(k,"margas/"))},loadBasti:function(){return y.a.get("".concat(k,"bastis/"))}},S=function(){function e(t,n,r,a){Object(v.a)(this,e),this.id=void 0,this.name=void 0,this.phone=void 0,this.password=void 0,this.name=t,this.phone=n,this.password=r,a&&(this.id=a),Q.collectors.mapToClass(e)}return Object(b.a)(e,[{key:"save",value:function(){return Q.collectors.put(this)}}]),e}();function W(e){return C.apply(this,arguments)}function C(){return(C=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.transaction("rw",Q.collectors,Object(f.a)(l.a.mark((function e(){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.collectors.add(new S(t.name,t.phone,t.password,t.id));case 2:case"end":return e.stop()}}),e)}))));case 2:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function A(){return I.apply(this,arguments)}function I(){return(I=Object(f.a)(l.a.mark((function e(){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.transaction("r",Q.collectors,Object(f.a)(l.a.mark((function e(){var t;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.collectors.toArray();case 2:return t=e.sent,e.abrupt("return",t);case 4:case"end":return e.stop()}}),e)}))));case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function P(e){return B.apply(this,arguments)}function B(){return(B=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.collectors.where("phone").startsWithAnyOfIgnoreCase(t).toArray();case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function D(e,t){return q.apply(this,arguments)}function q(){return(q=Object(f.a)(l.a.mark((function e(t,n){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.collectors.where({phone:t,password:n}).first();case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}var E=function(){function e(t,n,r){Object(v.a)(this,e),this.id=void 0,this.name=void 0,this.status=void 0,this.name=t,this.status=n,r&&(this.id=r),Q.wards.mapToClass(e)}return Object(b.a)(e,[{key:"save",value:function(){return Q.wards.put(this)}}]),e}();function L(e){return T.apply(this,arguments)}function T(){return(T=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.transaction("rw",Q.wards,Object(f.a)(l.a.mark((function e(){var n;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.wards.add(new E(t.name,t.status,t.id));case 2:n=e.sent,console.log(n);case 4:case"end":return e.stop()}}),e)}))));case 2:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function z(){return U.apply(this,arguments)}function U(){return(U=Object(f.a)(l.a.mark((function e(){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.transaction("r",Q.wards,Object(f.a)(l.a.mark((function e(){var t;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.wards.toArray();case 2:return t=e.sent,e.abrupt("return",t);case 4:case"end":return e.stop()}}),e)}))));case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function F(e){return H.apply(this,arguments)}function H(){return(H=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.wards.where("name").startsWithAnyOfIgnoreCase(t).toArray();case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function J(){return M.apply(this,arguments)}function M(){return(M=Object(f.a)(l.a.mark((function e(){var t,n;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return console.log("Synchronizing Collectors..."),e.next=3,N.loadCollectors();case 3:200===(t=e.sent).status&&((n=t.data).map(function(){var e=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,P(t.phone);case 2:if(0!==e.sent.length){e.next=6;break}return e.next=6,W({name:t.name,phone:t.phone,password:t.password,id:t.id});case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()),console.log(n.length," Collectors Synced.",n));case 5:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function V(){return _.apply(this,arguments)}function _(){return(_=Object(f.a)(l.a.mark((function e(){var t,n;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return console.log("Synchronizing Wards..."),e.next=3,N.loadWada();case 3:200===(t=e.sent).status&&((n=t.data).map(function(){var e=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,F(t.name);case 2:if(0!==e.sent.length){e.next=6;break}return e.next=6,L({name:t.name,status:t.status,id:t.id});case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()),console.log(n.length," Wards Synced."));case 5:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function R(){return $.apply(this,arguments)}function $(){return($=Object(f.a)(l.a.mark((function e(){var t,n;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return console.log("Synchronizing Basti..."),e.next=3,N.loadBasti();case 3:200===(t=e.sent).status&&((n=t.data).map(function(){var e=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,ee(t.name);case 2:if(0!==e.sent.length){e.next=6;break}return e.next=6,Y({name:t.name,status:t.status,id:t.id,wardId:t.ward_id});case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()),console.log(n.length," Bastis Synced."));case 5:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function G(){return K.apply(this,arguments)}function K(){return(K=Object(f.a)(l.a.mark((function e(){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!window.navigator.onLine){e.next=7;break}return e.next=3,J();case 3:return e.next=5,V();case 5:return e.next=7,R();case 7:case"end":return e.stop()}}),e)})))).apply(this,arguments)}var Q=new(function(e){Object(m.a)(n,e);var t=Object(x.a)(n);function n(){var e;Object(v.a)(this,n),(e=t.call(this,"VPDB")).users=void 0,e.wards=void 0,e.bastis=void 0,e.collectors=void 0;var r=Object(w.a)(e);return r.version(1).stores({users:"++id, name, phone, password",wards:"id, name, status",bastis:"id, name, status, wardId",collectors:"id, name, phone, password"}),r.open().then(function(){var e=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return console.log("DB opened Succefully"),e.next=3,G();case 3:console.log("Sync Complete");case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()).catch((function(e){console.log("DB error",e)})),e}return n}(O.a)),X=function(){function e(t,n,r,a){Object(v.a)(this,e),this.id=void 0,this.name=void 0,this.status=void 0,this.wardId=void 0,this.name=t,this.status=n,this.wardId=r,a&&(this.id=a),Q.bastis.mapToClass(e)}return Object(b.a)(e,[{key:"save",value:function(){return Q.bastis.put(this)}}]),e}();function Y(e){return Z.apply(this,arguments)}function Z(){return(Z=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.transaction("rw",Q.bastis,Object(f.a)(l.a.mark((function e(){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.bastis.add(new X(t.name,t.status,t.wardId,t.id));case 2:case"end":return e.stop()}}),e)}))));case 2:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function ee(e){return te.apply(this,arguments)}function te(){return(te=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.bastis.where("name").startsWithAnyOfIgnoreCase(t).toArray();case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function ne(e){return re.apply(this,arguments)}function re(){return(re=Object(f.a)(l.a.mark((function e(t){return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Q.bastis.where({wardId:parseInt(t)}).toArray();case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function ae(e){var t=e.data,n=Object(r.useState)([]),a=Object(j.a)(n,2),s=a[0],c=a[1],o=Object(r.useState)([]),i=Object(j.a)(o,2),p=i[0],d=i[1];function v(){return(v=Object(f.a)(l.a.mark((function e(){var t;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,z();case 2:t=e.sent,c(Object(h.a)(t));case 4:case"end":return e.stop()}}),e)})))).apply(this,arguments)}Object(r.useEffect)((function(){!function(){v.apply(this,arguments)}()}),[]);var b=function(){var e=Object(f.a)(l.a.mark((function e(t){var n,r;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=t.target.value,e.next=3,ne(n);case 3:r=e.sent,d(Object(h.a)(r));case 5:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),w=function(e){return((null===t||void 0===t?void 0:t.requiredFields)||[]).indexOf(e)>-1};return Object(u.jsxs)("div",{className:"vp-form",children:[Object(u.jsxs)("div",{className:"form-group ".concat(t&&w(1)?"required":""),id:"1",children:[Object(u.jsx)("label",{className:"label",children:"1. Ward No"}),Object(u.jsx)("div",{className:"options-verical",onChange:b,children:s.map((function(e,t){return Object(u.jsx)("div",{className:"radio",children:Object(u.jsxs)("label",{children:[Object(u.jsx)("input",{type:"radio",value:e.id,name:"ward_no"}),e.name]})},t)}))})]}),Object(u.jsxs)("div",{className:"form-group ".concat(t&&w(2)?"required":""),id:"2",children:[Object(u.jsx)("label",{className:"label",children:"2. Basti ko Naam"}),Object(u.jsx)("div",{className:"options-verical",children:p.map((function(e,t){return Object(u.jsx)("div",{className:"radio",children:Object(u.jsxs)("label",{children:[Object(u.jsx)("input",{type:"radio",value:e.id,name:"basti"}),e.name]})},t)}))})]})]})}var se=[1,2];function ce(e){var t=e.data;return t.requiredFields=se,Object(u.jsx)("div",{className:"vp-form-wrapper",children:Object(u.jsx)(ae,{data:t})})}function oe(){return Object(u.jsx)("div",{children:"Pending Data Here"})}var ie=n(22),ue=n(14),pe=new(n(41).a),de={name:"",phone:"",password:""};function le(){var e=Object(r.useState)(de),t=Object(j.a)(e,2),n=t[0],a=t[1],s=Object(r.useState)(!1),c=Object(j.a)(s,2),i=c[0],p=c[1],d=Object(r.useState)(""),h=Object(j.a)(d,2),v=h[0],b=h[1];function w(){return(w=Object(f.a)(l.a.mark((function e(){var t;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,A();case 2:t=e.sent,console.log(t);case 4:case"end":return e.stop()}}),e)})))).apply(this,arguments)}Object(r.useEffect)((function(){O(),function(){w.apply(this,arguments)}()}),[]);var m=function(e){e.persist(),a((function(t){return Object(ue.a)(Object(ue.a)({},t),{},Object(ie.a)({},e.target.name,e.target.value))}))},x=function(){var e=Object(f.a)(l.a.mark((function e(t){var r;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t.preventDefault(),p(!0),e.next=4,D(n.phone,n.password);case 4:(r=e.sent)?(a((function(e){return Object(ue.a)(Object(ue.a)({},e),{},{id:(null===r||void 0===r?void 0:r.id)?null===r||void 0===r?void 0:r.id:de.id,name:(null===r||void 0===r?void 0:r.name)?null===r||void 0===r?void 0:r.name:"",phone:(null===r||void 0===r?void 0:r.phone)?null===r||void 0===r?void 0:r.phone:de.phone})})),g(r)):b("Phone or Password did not match!"),p(!1);case 7:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),O=function(){var e=pe.get("auth");e&&a(Object(ue.a)({},e))},g=function(e){pe.set("auth",e)};return i?Object(u.jsx)("div",{className:"vp-home",children:"Loading..."}):n.id?Object(u.jsxs)("div",{className:"vp-home",children:[Object(u.jsxs)("div",{className:"welcome",children:["Welcome ",Object(u.jsx)("br",{}),null===n||void 0===n?void 0:n.name,Object(u.jsx)("p",{className:"logout",onClick:function(){a(Object(ue.a)({},de)),pe.remove("auth")},children:"Logout"})]}),Object(u.jsx)(o.b,{to:"/vp-app/app/add-new",children:"Add New Household"}),Object(u.jsx)(o.b,{to:"/vp-app/app/pending",children:"Pending Data"}),Object(u.jsx)(o.b,{to:"/vp-app/app/incomplete",children:"Incomplete Data"})]}):Object(u.jsx)("div",{className:"vp-home",children:Object(u.jsxs)("form",{method:"post",onSubmit:x,children:[Object(u.jsxs)("div",{className:"form-group",children:[Object(u.jsx)("label",{children:"Phone"}),Object(u.jsx)("input",{type:"number",placeholder:"Phone No",name:"phone",value:null===n||void 0===n?void 0:n.phone,onChange:m,required:!0})]}),Object(u.jsxs)("div",{className:"form-group",children:[Object(u.jsx)("label",{children:"Password"}),Object(u.jsx)("input",{type:"password",placeholder:"Password",name:"password",value:null===n||void 0===n?void 0:n.password,onChange:m,required:!0})]}),Object(u.jsx)("p",{style:{color:"red"},children:v}),Object(u.jsx)("button",{children:"Submit"})]})})}n(72);function he(){return Q.open(),Object(u.jsx)(o.a,{children:Object(u.jsxs)(i.c,{children:[Object(u.jsx)(i.a,{path:"/vp-app/app/add-new",children:Object(u.jsx)(ce,{data:{}})}),Object(u.jsx)(i.a,{path:"/vp-app/app/pending",children:Object(u.jsx)(oe,{})}),Object(u.jsx)(i.a,{path:"/vp-app/app",children:Object(u.jsx)(le,{})}),Object(u.jsx)(i.a,{path:"/",children:Object(u.jsx)(p,{})}),Object(u.jsx)(i.a,{path:"/vp-app",children:Object(u.jsx)(p,{})})]})})}var fe=Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));function je(e,t){navigator.serviceWorker.register(e).then((function(e){e.onupdatefound=function(){var n=e.installing;null!=n&&(n.onstatechange=function(){"installed"===n.state&&(navigator.serviceWorker.controller?(console.log("New content is available and will be used when all tabs for this page are closed. See https://cra.link/PWA."),t&&t.onUpdate&&t.onUpdate(e)):(console.log("Content is cached for offline use."),t&&t.onSuccess&&t.onSuccess(e)))})}})).catch((function(e){console.error("Error during service worker registration:",e)}))}c.a.render(Object(u.jsx)(a.a.StrictMode,{children:Object(u.jsx)(he,{})}),document.getElementById("root")),function(e){if("serviceWorker"in navigator){if(new URL("/vp-app",window.location.href).origin!==window.location.origin)return;window.addEventListener("load",(function(){var t="".concat("/vp-app","/service-worker.js");fe?(!function(e,t){fetch(e,{headers:{"Service-Worker":"script"}}).then((function(n){var r=n.headers.get("content-type");404===n.status||null!=r&&-1===r.indexOf("javascript")?navigator.serviceWorker.ready.then((function(e){e.unregister().then((function(){window.location.reload()}))})):je(e,t)})).catch((function(){console.log("No internet connection found. App is running in offline mode.")}))}(t,e),navigator.serviceWorker.ready.then((function(){console.log("This web app is being served cache-first by a service worker. To learn more, visit https://cra.link/PWA")}))):je(t,e)}))}}()}},[[73,1,2]]]);
//# sourceMappingURL=main.5d96e89a.chunk.js.map
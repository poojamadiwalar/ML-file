<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/1y4539Hc4d28v2fttdrFJlC1Ky7LOvWeo#scrollTo=hF7y1D3u_GO5 -->
<html lang="en" theme="adaptive" editor="Default Light"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script type="text/javascript" async="" charset="utf-8" src="./ML._files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-WPIRN7/u9nHvMTmnq/GvfSeKYZNo6h0erpwdlq/rBqKEeY8mZJTuv34aFA5aJVS4" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./ML._files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-WPIRN7/u9nHvMTmnq/GvfSeKYZNo6h0erpwdlq/rBqKEeY8mZJTuv34aFA5aJVS4" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./ML._files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-WPIRN7/u9nHvMTmnq/GvfSeKYZNo6h0erpwdlq/rBqKEeY8mZJTuv34aFA5aJVS4" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./ML._files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-WPIRN7/u9nHvMTmnq/GvfSeKYZNo6h0erpwdlq/rBqKEeY8mZJTuv34aFA5aJVS4" nonce=""></script><script type="text/javascript" async="" src="./ML._files/js" nonce=""></script><script src="./ML._files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./ML._files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./ML._files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Untitled3.ipynb - Colab</title><link href="./ML._files/css2(2)" rel="stylesheet"><link href="./ML._files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_9a:not(.gb_bd){font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}.gb_Fd{display:inline-block;padding:4px 4px 4px 4px;vertical-align:middle}.gb_Id .gb_r{bottom:-3px;right:-5px}.gb_Fd:first-child,#gbsfw:first-child+.gb_Fd{padding-left:0}.gb_f{position:relative}.gb_d{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_d{cursor:pointer;text-decoration:none}.gb_d,a.gb_d{color:#000}.gb_4e{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_5e{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_5e{border-bottom-color:#ccc}.gb_W{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_Fd.gb_Ea .gb_4e,.gb_Fd.gb_Ea .gb_5e,.gb_Fd.gb_Ea .gb_W,.gb_Ea.gb_W{display:block}.gb_Fd.gb_Ea.gb_6e .gb_4e,.gb_Fd.gb_Ea.gb_6e .gb_5e{display:none}.gb_Jd{position:absolute;right:8px;top:62px;z-index:-1}.gb_0a .gb_4e,.gb_0a .gb_5e,.gb_0a .gb_W{margin-top:-10px}a.gb_ra{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_ra:hover:after,a.gb_ra:focus:after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_ra:hover,a.gb_ra:focus{text-decoration:none}a.gb_ra:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_sa{background-color:#4285f4;color:#fff}a.gb_sa:active{background-color:#0043b2}.gb_ta{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_ra,.gb_sa,.gb_ua,.gb_va{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_ua{background:#f8f8f8;border:1px solid #c6c6c6}.gb_va{background:#f8f8f8}.gb_ua,#gb a.gb_ua.gb_ua,.gb_va{color:#666;cursor:default;text-decoration:none}#gb a.gb_va{cursor:default;text-decoration:none}.gb_va{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_va{color:#fff}.gb_va:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_va:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_wa{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_wa:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_wa:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_wa:active,#gb .gb_wa:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_wa.gb_i{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_wa.gb_i:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_wa.gb_i:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_wa.gb_i:active,#gb .gb_wa.gb_i:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_Fd:first-child,#gbsfw:first-child+.gb_Fd{padding-left:4px}.gb_ha.gb_Kd .gb_Fd:first-child{padding-left:0}.gb_Ld{position:relative}.gb_Xc .gb_Ld,.gb_dd .gb_Ld{float:right}.gb_d{padding:8px;cursor:pointer}.gb_d:after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_ha .gb_9d:not(.gb_ra):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_Md button svg,.gb_d{-webkit-border-radius:50%;border-radius:50%}.gb_Md button:focus:not(:focus-visible) svg,.gb_Md button:hover svg,.gb_Md button:active svg,.gb_d:focus:not(:focus-visible),.gb_d:hover,.gb_d:active,.gb_d[aria-expanded=true]{outline:none}.gb_Hc .gb_Md.gb_ie button:focus-visible svg,.gb_Md button:focus-visible svg,.gb_d:focus-visible{outline:1px solid #202124}.gb_Hc .gb_Md button:focus-visible svg,.gb_Hc .gb_d:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Hc .gb_Md.gb_ie button:focus-visible svg,.gb_Md button:focus-visible svg,.gb_Hc .gb_Md button:focus-visible svg{outline:1px solid currentcolor}}.gb_Hc .gb_Md.gb_ie button:focus svg,.gb_Hc .gb_Md.gb_ie button:focus:hover svg,.gb_Md button:focus svg,.gb_Md button:focus:hover svg,.gb_d:focus,.gb_d:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Hc .gb_Md.gb_ie button:active svg,.gb_Md button:active svg,.gb_d:active{background-color:rgba(60,64,67,.12)}.gb_Hc .gb_Md.gb_ie button:hover svg,.gb_Md button:hover svg,.gb_d:hover{background-color:rgba(60,64,67,.08)}.gb_xa .gb_d.gb_za:hover{background-color:transparent}.gb_d[aria-expanded=true],.gb_d:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_d[aria-expanded=true] .gb_h{fill:#5f6368;opacity:1}.gb_Hc .gb_Md button:hover svg,.gb_Hc .gb_d:hover{background-color:rgba(232,234,237,.08)}.gb_Hc .gb_Md button:focus svg,.gb_Hc .gb_Md button:focus:hover svg,.gb_Hc .gb_d:focus,.gb_Hc .gb_d:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Hc .gb_Md button:active svg,.gb_Hc .gb_d:active{background-color:rgba(232,234,237,.12)}.gb_Hc .gb_d[aria-expanded=true],.gb_Hc .gb_d:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Hc .gb_d[aria-expanded=true] .gb_h{fill:#fff;opacity:1}.gb_Fd{padding:4px}.gb_ha.gb_Kd .gb_Fd{padding:4px 2px}.gb_ha.gb_Kd .gb_b.gb_Fd{padding-left:6px}.gb_W{z-index:991;line-height:normal}.gb_W.gb_Nd{left:0;right:auto}@media (max-width:350px){.gb_W.gb_Nd{left:0}}.gb_Od .gb_W{top:56px}.gb_m{display:none!important}.gb_Ta{visibility:hidden}.gb_k .gb_d,.gb_V .gb_k .gb_d{background-position:-64px -29px}.gb_B .gb_k .gb_d{background-position:-29px -29px;opacity:1}.gb_k .gb_d,.gb_k .gb_d:hover,.gb_k .gb_d:focus{opacity:1}.gb_n{display:none}@media screen and (max-width:319px){.gb_jd:not(.gb_pd) .gb_k{display:none;visibility:hidden}}.gb_r{display:none}.gb_6c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_6c.gb_7c{color:#3c4043}.gb_ha.gb_Ja .gb_6c{margin-bottom:0}.gb_8c.gb_9c .gb_6c{padding-left:4px}.gb_ha.gb_Ja .gb_ad{position:relative;top:-2px}.gb_ha{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_ha.gb_Pc{min-width:120px}.gb_ha.gb_hd .gb_id{display:none}.gb_ha.gb_hd .gb_jd{height:56px}header.gb_ha{display:block}.gb_ha svg{fill:currentColor}.gb_kd{position:fixed;top:0;width:100%}.gb_ld{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_md{height:64px}.gb_jd{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_ha:not(.gb_Ja) .gb_jd{padding:8px}.gb_ha.gb_od .gb_jd{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_ha .gb_jd.gb_pd.gb_qd{min-width:0}.gb_ha.gb_Ja .gb_jd{padding:4px;padding-left:8px;min-width:0}.gb_id{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_sd>.gb_id{display:table-cell;width:100%}.gb_8c{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_ha.gb_Ja .gb_8c{padding-right:14px}.gb_td{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_td>:only-child{display:inline-block}.gb_ud.gb_Zc{padding-left:4px}.gb_ud.gb_vd,.gb_ha.gb_od .gb_ud,.gb_ha.gb_Ja:not(.gb_dd) .gb_ud{padding-left:0}.gb_ha.gb_Ja .gb_ud.gb_vd{padding-right:0}.gb_ha.gb_Ja .gb_ud.gb_vd .gb_xa{margin-left:10px}.gb_Zc{display:inline}.gb_ha.gb_Sc .gb_ud.gb_wd,.gb_ha.gb_dd .gb_ud.gb_wd{padding-left:2px}.gb_6c{display:inline-block}.gb_ud{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_dd{height:48px}.gb_ha.gb_dd{min-width:auto}.gb_dd .gb_ud{float:right;padding-left:32px}.gb_dd .gb_ud.gb_xd{padding-left:0}.gb_yd{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_cd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Dd{color:black}.gb_Hc{color:white}.gb_ha a,.gb_Mc a{color:inherit}.gb_M{color:rgba(0,0,0,.87)}.gb_ha svg,.gb_Mc svg,.gb_8c .gb_gd,.gb_Xc .gb_gd{color:#5f6368;opacity:1}.gb_Hc svg,.gb_Mc.gb_Qc svg,.gb_Hc .gb_8c .gb_gd,.gb_Hc .gb_8c .gb_Fc,.gb_Hc .gb_8c .gb_ad,.gb_Mc.gb_Qc .gb_gd{color:rgba(255,255,255,.87)}.gb_Hc .gb_8c .gb_Ec:not(.gb_Ed){opacity:.87}.gb_7c{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Hc .gb_7c,.gb_Dd .gb_7c{opacity:1}.gb_zd{position:relative}.gb_o{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_y,span.gb_y{color:rgba(0,0,0,.87);text-decoration:none}.gb_Hc a.gb_y,.gb_Hc span.gb_y{color:white}a.gb_y:focus{outline-offset:2px}a.gb_y:hover{text-decoration:underline}.gb_z{display:inline-block;padding-left:15px}.gb_z .gb_y{display:inline-block;line-height:24px;vertical-align:middle}.gb_ed{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_ha.gb_dd .gb_ed{margin-left:8px}#gb a.gb_va.gb_ed{cursor:pointer}.gb_va.gb_ed:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_va.gb_ed:focus,.gb_va.gb_ed:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_va.gb_ed:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_ed{background:#1a73e8;border:1px solid transparent}.gb_ha.gb_Ja .gb_ed{padding:9px 15px;min-width:80px}.gb_Ad{text-align:left}#gb .gb_Hc a.gb_ed:not(.gb_i),#gb.gb_Hc a.gb_ed{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_va.gb_i.gb_ed{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Hc a.gb_ed:hover:not(.gb_i),#gb.gb_Hc a.gb_ed:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_va.gb_i.gb_ed:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Hc a.gb_ed:focus:not(.gb_i),#gb .gb_Hc a.gb_ed:focus:hover:not(.gb_i),#gb.gb_Hc a.gb_ed:focus:not(.gb_i),#gb.gb_Hc a.gb_ed:focus:hover:not(.gb_i){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_va.gb_i.gb_ed:focus,#gb a.gb_va.gb_i.gb_ed:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Hc a.gb_ed:active:not(.gb_i),#gb.gb_Hc a.gb_ed:active{background:#ecf3fe}#gb a.gb_va.gb_i.gb_ed:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_l{display:none}@media screen and (max-width:319px){.gb_jd:not(.gb_pd) .gb_k{display:none;visibility:hidden}}.gb_xa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_xa.gb_i{background-color:transparent;border:1px solid #5f6368}.gb_Da{display:inherit}.gb_xa.gb_i .gb_Da{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_xa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_xa.gb_i:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_xa:focus-visible,.gb_xa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_xa.gb_i:focus-visible,.gb_xa.gb_i:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_xa.gb_i:active,.gb_xa.gb_Ea.gb_i:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_Fa{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_xa.gb_i .gb_Fa{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_Fa.gb_Ha{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_Fa.gb_Ha .gb_Ia{vertical-align:middle}.gb_ha:not(.gb_Ja) .gb_xa{margin-left:10px;margin-right:4px}.gb_Ka{max-height:32px;width:78px}.gb_xa.gb_i .gb_Ka{max-height:26px;width:72px}.gb_q{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_Ua{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_Ua.gb_q{height:30px;width:30px}.gb_Ua.gb_q:hover,.gb_Ua.gb_q:active{-webkit-box-shadow:none;box-shadow:none}.gb_Va{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_Wa{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_q::before,.gb_Xa::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_D .gb_Xa::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_q:hover,.gb_q:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_q:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_q:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_Za{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_d.gb_Za{width:auto}.gb_Za:hover,.gb_Za:focus{opacity:.85}.gb_0a .gb_Za,.gb_0a .gb_1a{line-height:26px}#gb#gb.gb_0a a.gb_Za,.gb_0a .gb_1a{font-size:11px;height:auto}.gb_2a{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_za:hover .gb_2a{opacity:.85}.gb_xa>.gb_b{padding:3px 3px 3px 4px}.gb_3a.gb_Ta{color:#fff}.gb_B .gb_Za,.gb_B .gb_2a{opacity:1}#gb#gb.gb_B.gb_B a.gb_Za,#gb#gb .gb_B.gb_B a.gb_Za{color:#fff}.gb_B.gb_B .gb_2a{border-top-color:#fff;opacity:1}.gb_V .gb_q:hover,.gb_B .gb_q:hover,.gb_V .gb_q:focus,.gb_B .gb_q:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_4a .gb_b,.gb_5a .gb_b{position:absolute;right:1px}.gb_b.gb_A,.gb_6a.gb_A,.gb_za.gb_A{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_7a.gb_8a .gb_Za{width:30px!important}.gb_p{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_9a .gb_p,.gb_ab .gb_p{right:0;top:0}.gb_b .gb_d{padding:4px}.gb_s{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.WIp7bmmdiMk.2019.O","co.in","en-GB","425",0,[4,2,"","","","659382899","0"],null,"3CazZo6gFIiop84PoJ-a4Qw",null,0,"og.qtm.ygvnjEuASRQ.L.W.O","AA2YrTu-AIDpJnMn8htQ-0aB0kDLbVpl1A","AA2YrTuZHf1FxnWSuni4yfYFm7DJbfG-0A","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,1],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","poojamadivalar00@gmail.com","","AONCo6rxjFSxVG5cLz1HeXpzZuz3ZGmNOaDPPyXeeRFYZnjPmm42dTDstAVJ3l6AaIb4P7tJp3YpwX6UhLVoHZjAKqyDLvHqsw",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0,0,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en-GB"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.MGCxJbnW_Xw.O/am=AAAg/d=1/rs=AHpOoo9xa4htLEVH9xe6c4ToUehtTaLWvA/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20240708.1_p2","en-GB",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en-GB","659382899.0",8,null,1,0,null,null,null,null,"3701241,3701244,3701387,3701439",null,null,null,"3CazZo6gFIiop84PoJ-a4Qw",0,0,0,null,2,5,"nn",110,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.WIp7bmmdiMk.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTu-AIDpJnMn8htQ-0aB0kDLbVpl1A"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.ygvnjEuASRQ.L.W.O/m=qcwid/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTuZHf1FxnWSuni4yfYFm7DJbfG-0A"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?yac=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert"],0,1,null,1,1,1,1,null,null,0,0,0,0,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en-GB",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026timeStmp=1723016924\u0026secTok=.AG5fkS-t8-W2KWbJHjqPurelyeXsLvHe1w\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",1,1,0,0],0,0,0,[null,"https://colab.research.google.com/",null,null,null,1,null,0,0,"","","47","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,0,86400,0],0,null,null,null,0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,0]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var fa,ha,ma,oa,pa,ya,za,Ba,Ca,Da,Ga,Wa,Va,Ya,$a,Za,ab,bb,eb,fb,jb,mb,gb,lb,kb,ib,hb,nb,ob,xb,zb,Ab,Bb,Cb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ca=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};fa=function(a){return da?ea?ea.brands.some(({brand:b})=>b&&b.indexOf(a)!=-1):!1:!1};
_.u=function(a){return _.ca().indexOf(a)!=-1};ha=function(){return da?!!ea&&ea.brands.length>0:!1};_.ja=function(){return ha()?!1:_.u("Opera")};_.ka=function(){return ha()?!1:_.u("Trident")||_.u("MSIE")};_.la=function(){return _.u("Firefox")||_.u("FxiOS")};_.na=function(){return _.u("Safari")&&!(ma()||(ha()?0:_.u("Coast"))||_.ja()||(ha()?0:_.u("Edge"))||(ha()?fa("Microsoft Edge"):_.u("Edg/"))||(ha()?fa("Opera"):_.u("OPR"))||_.la()||_.u("Silk")||_.u("Android"))};
ma=function(){return ha()?fa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(ha()?0:_.u("Edge"))||_.u("Silk")};oa=function(){return da?!!ea&&!!ea.platform:!1};pa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.qa=function(){return pa()||_.u("iPad")||_.u("iPod")};_.ra=function(){return oa()?ea.platform==="macOS":_.u("Macintosh")};_.ta=function(a,b){return _.sa(a,b)>=0};
_.ua=function(a){let b="",c=0;const d=a.length-10240;for(;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)};_.va=function(a){return a!=null&&a instanceof Uint8Array};_.wa=function(a){return Array.prototype.slice.call(a)};_.xa=function(a){return!!((a[_.v]|0)&2)};ya=function(a,b){b[_.v]=(a|0)&-14591};za=function(a,b){b[_.v]=(a|34)&-14557};Ba=function(a){return!(!a||typeof a!=="object"||a.i!==Aa)};
Ca=function(a){return a!==null&&typeof a==="object"&&!Array.isArray(a)&&a.constructor===Object};Da=function(a,b,c){if(!Array.isArray(a)||a.length)return!1;const d=a[_.v]|0;if(d&1)return!0;if(!(b&&(Array.isArray(b)?b.includes(c):b.has(c))))return!1;a[_.v]=d|1;return!0};_.Ea=function(a){if(a&2)throw Error();};Ga=function(a,b){(b=_.Fa?b[_.Fa]:void 0)&&(a[_.Fa]=_.wa(b))};_.Ia=function(){const a=Error();Ha(a,"incident");_.ba(a)};_.Ja=function(a){a=Error(a);Ha(a,"warning");return a};
_.La=function(a){if(typeof a!=="boolean")throw Error("s`"+_.Ka(a)+"`"+a);return a};_.Ma=function(a){if(!Number.isFinite(a))throw _.Ja("enum");return a|0};_.Na=function(a){if(typeof a!=="number")throw _.Ja("int32");if(!Number.isFinite(a))throw _.Ja("int32");return a|0};_.Oa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Pa=function(a){return a==null||typeof a==="string"?a:void 0};
_.Ra=function(a,b,c){if(a!=null&&typeof a==="object"&&a.Bd===_.Qa)return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;e===0&&(e|=c&32);e|=c&2;e!==d&&(a[_.v]=e);return new b(a)}};_.Ta=function(a,b){Sa=b;a=new a(b);Sa=void 0;return a};
_.Ua=function(a,b,c){a==null&&(a=Sa);Sa=void 0;if(a==null){var d=96;c?(a=[c],d|=512):a=[];b&&(d=d&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error("t");d=a[_.v]|0;if(d&2048)throw Error("u");if(d&64)return a;d|=64;if(c&&(d|=512,c!==a[0]))throw Error("v");a:{c=a;const e=c.length;if(e){const f=e-1;if(Ca(c[f])){d|=256;b=f-(+!!(d&512)-1);if(b>=1024)throw Error("w");d=d&-16760833|(b&1023)<<14;break a}}if(b){b=Math.max(b,e-(+!!(d&512)-1));if(b>1024)throw Error("x");d=d&-16760833|(b&1023)<<14}}}a[_.v]=
d;return a};Wa=function(a,b){return Va(b)};Va=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(Da(a,void 0,0))return}else{if(_.va(a))return _.ua(a);if("function"==typeof _.Xa&&a instanceof _.Xa)return a.j()}}return a};Ya=function(a,b,c){const d=_.wa(a);var e=d.length;const f=b&256?d[e-1]:void 0;e+=f?-1:0;for(b=b&512?1:0;b<e;b++)d[b]=c(d[b]);if(f){b=d[b]={};for(const g in f)b[g]=c(f[g])}Ga(d,a);return d};
$a=function(a,b,c,d,e){if(a!=null){if(Array.isArray(a))a=Da(a,void 0,0)?void 0:e&&(a[_.v]|0)&2?a:Za(a,b,c,d!==void 0,e);else if(Ca(a)){const f={};for(let g in a)f[g]=$a(a[g],b,c,d,e);a=f}else a=b(a,d);return a}};Za=function(a,b,c,d,e){const f=d||c?a[_.v]|0:0;d=d?!!(f&32):void 0;const g=_.wa(a);for(let h=0;h<g.length;h++)g[h]=$a(g[h],b,c,d,e);c&&(Ga(g,a),c(f,g));return g};ab=function(a){return a.Bd===_.Qa?a.toJSON():Va(a)};
bb=function(a,b,c=za){if(a!=null){if(a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=a[_.v]|0;if(d&2)return a;b&&(b=d===0||!!(d&32)&&!(d&64||!(d&16)));return b?(a[_.v]=(d|34)&-12293,a):Za(a,bb,d&4?za:c,!0,!0)}a.Bd===_.Qa&&(c=a.ha,d=c[_.v],a=d&2?a:_.Ta(a.constructor,_.cb(c,d,!0)));return a}};_.cb=function(a,b,c){const d=c||b&2?za:ya,e=!!(b&32);a=Ya(a,b,f=>bb(f,e,d));a[_.v]=a[_.v]|32|(c?2:0);return a};
_.db=function(a){const b=a.ha,c=b[_.v];return c&2?_.Ta(a.constructor,_.cb(b,c,!1)):a};eb=function(a){return a};fb=function(a){return a};jb=function(a,b,c,d){return gb(a,b,c,d,hb,ib)};mb=function(a,b,c,d){return gb(a,b,c,d,kb,lb)};
gb=function(a,b,c,d,e,f){if(!c.length&&!d)return 0;var g=0;let h=0,k=0;var l=0;let m=0;for(var p=c.length-1;p>=0;p--){var r=c[p];d&&p===c.length-1&&r===d||(l++,r!=null&&k++)}if(d)for(var q in d)p=+q,isNaN(p)||(m+=nb(p),h++,p>g&&(g=p));l=e(l,k)+f(h,g,m);q=k;p=h;r=g;let y=m;for(let E=c.length-1;E>=0;E--){var D=c[E];if(D==null||d&&E===c.length-1&&D===d)continue;D=E-b;const F=e(D,q)+f(p,r,y);F<l&&(a=1+D,l=F);p++;q--;y+=nb(D);r=Math.max(r,D)}b=e(0,0)+f(p,r,y);b<l&&(a=0,l=b);if(d){p=h;r=g;y=m;q=k;for(const E in d)d=
+E,isNaN(d)||d>=1024||(p--,q++,y-=E.length,g=e(d,q)+f(p,r,y),g<l&&(a=1+d,l=g))}return a};lb=function(a,b,c){return c+a*3+(a>1?a-1:0)};kb=function(a,b){return(a>1?a-1:0)+(a-b)*4};ib=function(a,b){return a==0?0:9*Math.max(1<<32-Math.clz32(a+a/2-1),4)<=b?a==0?0:a<4?100+(a-1)*16:a<6?148+(a-4)*16:a<12?244+(a-6)*16:a<22?436+(a-12)*19:a<44?820+(a-22)*17:52+32*a:40+4*b};hb=function(a){return 40+4*a};nb=function(a){return a>=100?a>=1E4?Math.ceil(Math.log10(1+a)):a<1E3?3:4:a<10?1:2};
ob=function(a,b,c,d){b=d+(+!!(b&512)-1);if(!(b<0||b>=a.length||b>=c))return a[b]};_.qb=function(a,b,c,d,e){const f=b>>14&1023||536870912;if(c>=f||e&&!pb){let g=b;if(b&256)e=a[a.length-1];else{if(d==null)return g;e=a[f+(+!!(b&512)-1)]={};g|=256}e[c]=d;c<f&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&(a[_.v]=g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b};_.sb=function(a,b,c,d){a=a.ha;let e=a[_.v];const f=_.rb(a,e,c,d);b=_.Ra(f,b,e);b!==f&&b!=null&&_.qb(a,e,c,b,d);return b};
_.tb=function(a,b){return a!=null?a:b};
xb=function(a){var b=ub?a.ha:Za(a.ha,ab,void 0,void 0,!1);{var c=!ub;var d=vb?void 0:a.constructor.wj;var e=(c?a.ha:b)[_.v];let B=b.length;if(B){var f=b[B-1],g=Ca(f);g?B--:f=void 0;a=+!!(e&512)-1;var h=B-a,k=!!wb&&pb&&!(e&512),l;e=(l=wb)!=null?l:fb;e=k?e(h,a,b,f):h;l=(h=k&&h!==e)?Array.prototype.slice.call(b,0,B):b;if(g||h){b:{var m=l;var p=f;g={};k=!1;if(h)for(var r=Math.max(0,e+a);r<m.length;r++){var q=m[r],y=r-a;q==null||Da(q,d,y)||Ba(q)&&q.size===0||(m[r]=void 0,g[y]=q,k=!0)}if(p)for(var D in p)if(r=
+D,isNaN(r))g[D]=p[D];else if(q=p[D],Array.isArray(q)&&(Da(q,d,+D)||Ba(q)&&q.size===0)&&(q=null),q==null&&(k=!0),h&&r<e){k=!0;q=r+a;for(y=m.length;y<=q;y++)m.push(void 0);m[q]=p[r]}else q!=null&&(g[D]=q);if(k){for(var E in g){p=g;break b}p=null}}m=p==null?f!=null:p!==f}h&&(B=l.length);for(var F;B>0;B--){E=B-1;D=l[E];E-=a;if(!(D==null||Da(D,d,E)||Ba(D)&&D.size===0))break;F=!0}if(l!==b||m||F){if(!h&&!c)l=Array.prototype.slice.call(l,0,B);else if(F||m||p)l.length=B;p&&l.push(p)}b=l}}return b};
_.w=function(a,b){return a!=null?!!a:!!b};_.x=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.yb=function(a){for(const b in a)return!1;return!0};zb=typeof Object.defineProperties=="function"?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
Ab=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Bb=Ab(this);Cb=function(a,b){if(b)a:{var c=Bb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&zb(c,a,{configurable:!0,writable:!0,value:b})}};
Cb("Symbol.dispose",function(a){return a?a:Symbol("b")});Cb("globalThis",function(a){return a||Bb});Cb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});var Fb,Gb,Jb;_.Db=_.Db||{};_.t=this||self;Fb=function(a,b){var c=_.Eb("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Gb=_.t._F_toggles||[];_.Eb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ka=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Hb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Ib="closure_uid_"+(Math.random()*1E9>>>0);
Jb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Jb;return _.z.apply(null,arguments)};_.A=function(a,b){a=a.split(".");var c=_.t;a[0]in c||typeof c.execScript=="undefined"||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};
_.C=function(a,b){function c(){}c.prototype=b.prototype;a.W=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.dj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.C(_.aa,Error);_.aa.prototype.name="CustomError";var Kb=!!(Gb[0]&4096),Lb=!!(Gb[0]&128),Mb=!!(Gb[0]&8192),Nb=!!(Gb[0]&64),Ob=!!(Gb[0]&16);var Pb=Fb(1,!0),da=Kb?Mb:Fb(610401301,!1),pb=Kb?Lb||!Ob:Fb(645172343,Pb);var vb=Kb?Lb||!Nb:Fb(188588736,!0);_.Qb=typeof TextDecoder!=="undefined";_.Rb=typeof TextEncoder!=="undefined";_.Sb=function(){return _.ca().toLowerCase().indexOf("webkit")!=-1};var ea,Tb=_.t.navigator;ea=Tb?Tb.userAgentData||null:null;_.sa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.Vb=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.Wb=function(a){_.Wb[" "](a);return a};_.Wb[" "]=function(){};var ic;_.Xb=_.ja();_.Yb=_.ka();_.Zb=_.u("Edge");_.$b=_.u("Gecko")&&!(_.Sb()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.ac=_.Sb()&&!_.u("Edge");_.bc=_.ra();_.cc=oa()?ea.platform==="Windows":_.u("Windows");_.dc=oa()?ea.platform==="Android":_.u("Android");_.ec=pa();_.fc=_.u("iPad");_.gc=_.u("iPod");_.hc=_.qa();
a:{var jc="",kc=function(){var a=_.ca();if(_.$b)return/rv:([^\);]+)(\)|;)/.exec(a);if(_.Zb)return/Edge\/([\d\.]+)/.exec(a);if(_.Yb)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(_.ac)return/WebKit\/(\S+)/.exec(a);if(_.Xb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();kc&&(jc=kc?kc[1]:"");if(_.Yb){var lc,mc=_.t.document;lc=mc?mc.documentMode:void 0;if(lc!=null&&lc>parseFloat(jc)){ic=String(lc);break a}}ic=jc}_.nc=ic;_.oc=_.la();_.pc=pa()||_.u("iPod");_.qc=_.u("iPad");_.rc=_.u("Android")&&!(ma()||_.la()||_.ja()||_.u("Silk"));_.sc=ma();_.tc=_.na()&&!_.qa();var uc;_.v=Symbol();uc=Symbol();_.vc=Symbol();_.wc=Symbol();var Aa,yc;_.Qa={};Aa={};yc=[];yc[_.v]=55;_.xc=Object.freeze(yc);_.zc=Object.freeze({});Object.freeze({});_.Ac=Object.freeze({});var Ha=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};var Bc;var Sa;_.Cc=function(a,b){a=a.ha;return _.rb(a,a[_.v],b)};_.rb=function(a,b,c,d){if(c===-1)return null;const e=b>>14&1023||536870912;if(c>=e){if(b&256)return a[a.length-1][c]}else{var f=a.length;if(d&&b&256&&(d=a[f-1][c],d!=null)){if(ob(a,b,e,c)&&uc!=null){var g;a=(g=Bc)!=null?g:Bc={};g=a[uc]||0;g>=4||(a[uc]=g+1,_.Ia())}return d}return ob(a,b,e,c)}};_.Dc=function(a,b,c){const d=a.ha;let e=d[_.v];_.Ea(e);_.qb(d,e,b,c);return a};
_.G=function(a,b,c,d=!1){b=_.sb(a,b,c,d);if(b==null)return b;a=a.ha;let e=a[_.v];if(!(e&2)){const f=_.db(b);f!==b&&(b=f,_.qb(a,e,c,b,d))}return b};_.H=function(a,b,c){c==null&&(c=void 0);return _.Dc(a,b,c)};_.I=function(a,b){a=_.Cc(a,b);return a==null||typeof a==="boolean"?a:typeof a==="number"?!!a:void 0};_.J=function(a,b){return _.Pa(_.Cc(a,b))};_.K=function(a,b,c=!1){return _.tb(_.I(a,b),c)};_.L=function(a,b){return _.tb(_.J(a,b),"")};_.M=function(a,b,c){return _.Dc(a,b,c==null?c:_.La(c))};
_.N=function(a,b,c){return _.Dc(a,b,c==null?c:_.Na(c))};_.O=function(a,b,c){return _.Dc(a,b,_.Oa(c))};_.P=function(a,b,c){return _.Dc(a,b,c==null?c:_.Ma(c))};var wb,ub;_.Q=class{constructor(a,b,c){this.ha=_.Ua(a,b,c)}toJSON(){return xb(this)}Ca(a){try{return ub=!0,a&&(wb=a===fb||a!==eb&&a!==jb&&a!==mb?fb:a),JSON.stringify(xb(this),Wa)}finally{a&&(wb=void 0),ub=!1}}rc(){return _.xa(this.ha)}};_.Q.prototype.Bd=_.Qa;_.Q.prototype.toString=function(){try{return ub=!0,xb(this).toString()}finally{ub=!1}};_.Ec=Symbol();_.Fc=Symbol();_.Gc=Symbol();_.Hc=Symbol();_.Ic=Symbol();var Jc=class extends _.Q{constructor(){super()}};_.Kc=class extends _.Q{constructor(){super()}D(a){return _.N(this,3,a)}};var Lc=class extends _.Q{constructor(a){super(a)}Jc(a){return _.O(this,24,a)}};_.Mc=class extends _.Q{constructor(a){super(a)}};_.R=function(){this.qa=this.qa;this.Y=this.Y};_.R.prototype.qa=!1;_.R.prototype.isDisposed=function(){return this.qa};_.R.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.R.prototype[Symbol.dispose]=function(){this.dispose()};_.R.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Nc=class extends _.R{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){var b=this.o;a=a.split(".");for(var c=a.length,d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}yb(){for(var a=this.i.length,b=this.i,c=[],d=0;d<a;++d){var e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].yb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Pc=class extends _.R{constructor(){var a=_.Oc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Qc=class extends _.Q{constructor(a){super(a)}};var Rc=class extends _.Q{constructor(a){super(a)}};var Uc;_.Sc=function(a,b,c=98,d=new _.Kc){if(a.i){const e=new Jc;_.O(e,1,b.message);_.O(e,2,b.stack);_.N(e,3,b.lineNumber);_.P(e,5,1);_.H(d,40,e);a.i.log(c,d)}};Uc=class{constructor(){var a=Tc;this.i=null;_.K(a,4,!0)}log(a,b,c=new _.Kc){_.Sc(this,a,98,c)}};var Vc,Wc;Vc=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.Vb(c,b,a)}catch(d){console.error(d)}}}};_.Xc=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new Wc(a,b,c));Vc(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("B");this.i=a;Vc(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("B");this.j=a;Vc(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
Wc=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.Yc=a=>{var b="oc";if(a.oc&&a.hasOwnProperty(b))return a.oc;b=new a;return a.oc=b};_.Zc=class{constructor(){this.v=new _.Xc;this.i=new _.Xc;this.D=new _.Xc;this.B=new _.Xc;this.C=new _.Xc;this.A=new _.Xc;this.o=new _.Xc;this.j=new _.Xc;this.F=new _.Xc}K(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}qa(){return this.C}Y(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.Yc(_.Zc)}};var dd;_.ad=function(){return _.G(_.$c,Lc,1)};_.bd=function(){return _.G(_.$c,_.Mc,5)};dd=class extends _.Q{constructor(){super(cd)}};var cd;window.gbar_&&window.gbar_.CONFIG?cd=window.gbar_.CONFIG[0]||{}:cd=[];_.$c=new dd;var Tc=_.G(_.$c,Rc,3)||new Rc;_.ad()||new Lc;_.Oc=new Uc;_.A("gbar_._DumpException",function(a){_.Oc?_.Oc.log(a):console.error(a)});_.ed=new Pc;var gd;_.hd=function(a,b){var c=_.fd.i();if(a in c.i){if(c.i[a]!=b)throw new gd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.yb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.fd=class{constructor(){this.i={};this.j={}}static i(){return _.Yc(_.fd)}};_.id=class extends _.aa{constructor(){super()}};gd=class extends _.id{};_.A("gbar.A",_.Xc);_.Xc.prototype.aa=_.Xc.prototype.then;_.A("gbar.B",_.Zc);_.Zc.prototype.ba=_.Zc.prototype.M;_.Zc.prototype.bb=_.Zc.prototype.N;_.Zc.prototype.bd=_.Zc.prototype.qa;_.Zc.prototype.bf=_.Zc.prototype.K;_.Zc.prototype.bg=_.Zc.prototype.L;_.Zc.prototype.bh=_.Zc.prototype.Y;_.Zc.prototype.bj=_.Zc.prototype.J;_.Zc.prototype.bk=_.Zc.prototype.G;_.A("gbar.a",_.Zc.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var jd=new Nc;_.hd("api",jd);
var kd=_.bd()||new _.Mc,ld=window,md=_.x(_.J(kd,8));ld.__PVT=md;_.hd("eq",_.ed);
}catch(e){_._DumpException(e)}
try{
_.nd=class extends _.Q{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var od=class extends _.Q{constructor(){super()}};var pd=class extends _.R{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b})}init(a,b,c){window.gapi={};var d=window.___jsl={};d.h=_.x(_.J(a,1));_.I(a,12)!=null&&(d.dpo=_.w(_.K(a,12)));d.ms=_.x(_.J(a,2));d.m=_.x(_.J(a,3));d.l=[];_.L(b,1)&&(a=_.J(b,3))&&this.i.push(a);_.L(c,1)&&(c=_.J(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var qd=_.G(_.$c,_.Qc,14);if(qd){var rd=_.G(_.$c,_.nd,9)||new _.nd,sd=new od,td=new pd;td.init(qd,rd,sd);_.hd("gs",td)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_poojamadivalar00@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./ML._files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20240805-060208_RC00_659502231'; var colabScsVersion = '52c9e49bbd7e48975c1e96705eb7b92f'; var hl = 'en-GB'; var colabExperiments = JSON.parse('\x7b\x22add_prompt_cell\x22: false, \x22ai_unsubscribed_warning\x22: false, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22aida_in_editor\x22: false, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22cell_tags\x22: false, \x22chat_model_id_override\x22: \x22\x22, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22commands_in_toolbar\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22compose_skip_suffix_check\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22crawler\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22dep_cells_commands\x22: false, \x22dep_graph\x22: false, \x22development\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22\x22, \x22drop_chat_links\x22: false, \x22embedded_connection_poll\x22: false, \x22embedded_one_pending_connect_request\x22: true, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: false, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs\x22, \x22file_browser_poll_interval_millis\x22: 60000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22gemini_rebrand\x22: true, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_duplicate_code\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22granular_browser_permissions\x22: true, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22import_data\x22: false, \x22interactive_sheet_next_steps\x22: true, \x22internal_chat\x22: false, \x22internal_schedule\x22: false, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22log_preferences_on_change\x22: true, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22lsrp\x22: 0, \x22ml_enabled\x22: true, \x22mlpp\x22: false, \x22mlpp_multiline\x22: false, \x22mlpp_on_by_default\x22: true, \x22mobile\x22: false, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: false, \x22no_fun\x22: false, \x22notebook_context_length\x22: 50000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22prereq_cells_next_steps\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduce_chat_not_answering\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr\x22: false, \x22rp_lsp\x22: true, \x22rp_serve_kernel_port\x22: false, \x22rp_term\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt\x22: false, \x22run_button_tooltip\x22: false, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting\x22: false, \x22session_resume_coalesce\x22: true, \x22show_create_gemini_api_key_link\x22: false, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_relnotes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.25\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22AmUpB2+Hlwk73pYiEMbnkef\/dprJi1I9rClec33apyFsbVOaCIRN29Rk9M4ht5Otgbp+thCc3MMD73GyCNfEWAkAAAB3eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OX0\x3d\x22, \x22suspicious_code_matches\x22: \x22\x22, \x22suspicious_code_regexs\x22: \x22\x22, \x22term4all\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_deprecation_warning\x22: true, \x22tpu_node_redirect\x22: true, \x22tpu_node_selector_grayed_out\x22: true, \x22tpu_node_selector_visible\x22: false, \x22tpu_vm\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_corplogin\x22: true, \x22use_dm_sql_lsp\x22: false, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22waffle\x22: false, \x22workstations\x22: false, \x22ids\x22: \x5b20730185, 20730177, 20730265, 20730129, 20730150, 20730268, 20730230, 20730159, 20730262, 20730271, 20730182\x5d, \x22flag_ids\x22: \x7b\x22add_prompt_cell\x22: 45644995, \x22ai_unsubscribed_warning\x22: 45504730, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_in_editor\x22: 45425507, \x22allowed_public_url_domains\x22: 45425558, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22cell_tags\x22: 45425779, \x22chat_model_id_override\x22: 45631876, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22compose_skip_suffix_check\x22: 45615470, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22crawler\x22: 45425491, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22dep_cells_commands\x22: 45622249, \x22dep_graph\x22: 45629071, \x22development\x22: 45425544, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22embedded_connection_poll\x22: 45491618, \x22embedded_one_pending_connect_request\x22: 45640470, \x22enable_adhoc_backends\x22: 45425506, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_more_reprs\x22: 45613354, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22gemini_rebrand\x22: 45631310, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_duplicate_code\x22: 45646291, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22granular_browser_permissions\x22: 45630936, \x22hats_surveys\x22: 45425559, \x22import_data\x22: 45430411, \x22interactive_sheet_next_steps\x22: 45634324, \x22internal_chat\x22: 45622872, \x22internal_schedule\x22: 45425578, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22log_preferences_on_change\x22: 45643817, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22lsrp\x22: 45425612, \x22ml_enabled\x22: 45425493, \x22mlpp\x22: 45425608, \x22mlpp_multiline\x22: 45425623, \x22mlpp_on_by_default\x22: 45425609, \x22mobile\x22: 45425562, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22prereq_cells_next_steps\x22: 45640400, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduce_chat_not_answering\x22: 45640977, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr\x22: 45491686, \x22rp_lsp\x22: 45462965, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_term\x22: 45426219, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt\x22: 45425624, \x22run_button_tooltip\x22: 45646515, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting\x22: 45647313, \x22session_resume_coalesce\x22: 45425603, \x22show_create_gemini_api_key_link\x22: 45644190, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_relnotes_on_open\x22: 45428128, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22suspicious_code_matches\x22: 45425615, \x22suspicious_code_regexs\x22: 45425616, \x22term4all\x22: 45425542, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_deprecation_warning\x22: 45630619, \x22tpu_node_redirect\x22: 45634372, \x22tpu_node_selector_grayed_out\x22: 45630664, \x22tpu_node_selector_visible\x22: 45630663, \x22tpu_vm\x22: 45614812, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_corplogin\x22: 45425606, \x22use_dm_sql_lsp\x22: 45425610, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22waffle\x22: 45446491, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'poojamadivalar00@gmail.com'; var colabRenderDataToken = 'AFWLbD2sOWCKGTuybtY_1w8kO8ThL7AKGGHGXGwY-bh95WJpnXpyN0ASFoHhigjOE9FF0Rb4ZmVhRAhZZgBWsvkMVXRABhX2pQQwQC2b'; var colabConfig = '\x5b\x5b\x22poojamadivalar00@gmail.com\x22,\x5b1,\x22AHXL0D3hp1faBg\/qjGTNVpW7MBFPNOsJgdpJ0aDylrkE0yG3RUo2Y3FANRhWEIXF7\/qbaZlf5\/s3N165laj1UZXylU2bB39\/pdMz9LfWPft8eUDTivtb2eAH+yeYk0RMEYu5ilM5qxoWR4V7vcEpb0MqmyjFLf\/S9Ii\/wyyLUSCZ4zim6tqOdqFESFcRxXuAcoZ40pLtdBidXin7tf6FV4Z3e4ZU6+49a5i3ZItLP0hzaP1mXzdx6RyqKrqp3WPALBff\/Pd+6ZNtYcXKfwa5EHbHvhDYCtoQviNWqaC4VXxUeTslidlnw4DlcPupBp0UASXh9y7lwyxXnv5h28+N5Tp\/ZOAQ0eTu8TO3BSSwDA+V0l5h9DW01fa5XddJaAYMbWzeDtGofd442x8aEBUg9Olv+O5mbNEfizPVZPel8JXR728nstay6TXSIl9Hmpagn7NLqDEmlpt6+A3ZzI+h7z84+f3WkwfMslTSMT4Z5KY5PGx68OWTiz05stWi8qTU+1ME8W9g4a7yTp3RYq8TgFuKIhULugkovWAu9blzh6lTEp2Z0+Dr24Qc2ULsy1G0hdoHiw2P7y7zHvztIQCBQQiXH\/kR7zWrdsZtOykSDF5GBsrIHH35m+MrQVzee0F3QeJutX9Wu45DVDK9LhhUCJiPUc8tFUYldhXA1S1ERBy1jjEx0q+GqR2XR+tUHbNTLHgdAamAdYLq2IOYhUg6hwyrzVYF5vn+4O\/13uMcrTX9gwuJKchljFQ1ftXeOT3FCuS31ZD8ja01sIYu8XiKAZ0y+\/J69+j7sfgqbDnfHd4q4MEjFCm5qJ\/AEmDwlfTWvaGIRLOp8lC4VcouGfjf5ylGWidXQsVzasj70nuEE7mwrIia8QReKer4zdbxwuWIexVjJWGmdDdtL3cv1nYOwszhdj9KlGn7JiJHFtm5epjAUFncBTvq+D4SQc1ivjfBX6Oyi1vaFrnt8z19sHrYnv4GKLrCzgU4k\/W537A1J+9noa869y7RgtJhVDReAGy8Fw4GtL+Hk21UVGF6a3CuLKqlysr29\/mYKOiDH+qqwZ4+Li3JJ5oKbDG\/nm4D6n6MTOVLAiQT430t4lOywZBVuTtmXNT+dlZ24BtdQDN+5fgqCj2tyFpedEkCfqldC29FrWLg6B9sH1SuVd1ahJB2KJWMVEQW5PoS8JYG5+8qsAduldKunDhc+3S\/SogRgiWrijoURu4hLyXFsnyxaCpXPZMX0GzyXGGb8elVMgUKUkrla3QZ4dMQ4lE9RLor5+eSgLudp8ywcZhfuO738SfBcD+v31bbMpAFjWV04AdhUAl1Lx44JwPdDOfG1+9F03\/AI7uAuX\/igotrMUNfQqnmbkc0rEWvsccCZNDI6C9+\/fDyDAJTn7xoEW4L9jM6HmnsYWjdMhR9xxJMEwG5+M9FN\/L\/zz6Fm2qoPNpmv4rZ9dvceEuVTbY5JBX65HdcHuZqXTBAl98Zre9Uiv9GU6ewwjyCRFv7aV\/b1nT+rYdyQ31sPZpuljV3acxGzvYnTfbf0y\/Ghgx0RPXjq\/nmQF4QThbqzC9ycFhEoPh0rilz7DGitfUTI9X8QdCbAApUZTOUFk9vNcyt83LklUP\/aT3u2++WiQOp7E0EHp7KRrsmq9Bu6\/o6YpDM5js3FZhp\/fBMgUaBV+gXpdAvnFkrid3bXfE+T+xmqVXWApfUmCSFM30inBten1WIM8eMsWREgk229JHwJfmmJlbbNkpRDXLe51F9crvUUdFeBuGg9xoP6+WzTsueV3NcFsOnDbNFdxPpfLG08fKWbuLTx+NtyB2ylSqBjqJj7gb4\/eP+qa0KgIDTvUtT83Xmpf\/DL2N1UUv7CyW3uznP1eLLRzVWSFkQGcu9YMKsC5amGv8bCkxiF+CBp9Kt9UFSiPI\x3d\x22,\x22AJ9oCCzOZOrqdCzpKMac92Wc9Vdkohaibs\/+kkXOhkZ0d7ZnZwKREs0AF3+cDlC2lWknPkM2uQGAyUsp5IiEhUQcYpe\/e4g+Wb6+wyyEU7r84aIEZdoaezbH3hyp\/dx588zS\/kKBtOgn\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22\x5d,\x5b1,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/52c9e49bbd7e48975c1e96705eb7b92f/img%2Ffavicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="-wL8iYJTC7X0zF9qBNDQUAd-P1ZkQUK-OhSgv4Wkf1M"><meta name="google-site-verification" content="o-EECwEDQeUpZv0jTmoGfCDX7dUI8Kul4ESepXmDnO0"><meta name="google-site-verification" content="sNOroO9gXrazN-oMODOm0Bs0_vw1R5QwZ-BfrSHn8Io"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="AmUpB2+Hlwk73pYiEMbnkef/dprJi1I9rClec33apyFsbVOaCIRN29Rk9M4ht5Otgbp+thCc3MMD73GyCNfEWAkAAAB3eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OX0="><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./ML._files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="async" type="text/javascript" src="./ML._files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./ML._files/rs=AA2YrTu-AIDpJnMn8htQ-0aB0kDLbVpl1A" nonce=""></script><link type="text/css" href="./ML._files/rs=AA2YrTuZHf1FxnWSuni4yfYFm7DJbfG-0A" rel="stylesheet"><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./ML._files/editor.main.css"><script async="async" type="text/javascript" src="./ML._files/editor.main.nls.js.download"></script><script async="async" type="text/javascript" src="./ML._files/markdown.js.download"></script><script src="./ML._files/api.js.download" nonce=""></script><script src="./ML._files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #f7f7f7; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor { --vscode-foreground: #616161;
--vscode-disabledForeground: rgba(97, 97, 97, 0.5);
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textPreformat-foreground: #a31515;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-foreground: #616161;
--vscode-dropdown-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-sash-hoverBorder: #0090f1;
--vscode-editor-background: #f7f7f7;
--vscode-editor-foreground: #000000;
--vscode-editorStickyScroll-background: #f7f7f7;
--vscode-editorStickyScrollHover-background: #f0f0f0;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: #616161;
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editorInlayHint-foreground: #616161;
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-typeForeground: #616161;
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-parameterForeground: #616161;
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.3);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-diffEditor-insertedTextBackground: rgba(155, 185, 85, 0.09);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.03);
--vscode-diffEditor-insertedLineBackground: rgba(155, 185, 85, 0.09);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.03);
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #e4e4e4;
--vscode-diffEditor-unchangedRegionForeground: #4d4c4c;
--vscode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #d6ebff;
--vscode-list-activeSelectionForeground: #000000;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #0066bf;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #f3f3f3;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.16);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-inactiveIndentGuidesStroke: rgba(169, 169, 169, 0.4);
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-selectBackground: #f3f3f3;
--vscode-checkbox-foreground: #616161;
--vscode-checkbox-border: #cecece;
--vscode-checkbox-selectBorder: #424242;
--vscode-quickInputList-focusForeground: #000000;
--vscode-quickInputList-focusBackground: #d6ebff;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #000000;
--vscode-menu-selectionBackground: #d6ebff;
--vscode-menu-separatorBackground: #d4d4d4;
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #f7f7f7;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(0, 0, 0, 0);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background: #d3d3d3;
--vscode-editorIndentGuide-activeBackground: #939393;
--vscode-editorLineNumber-foreground: #999999;
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #f7f7f7;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #cea33d;
--vscode-editorUnicodeHighlight-background: rgba(206, 163, 61, 0.08);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: #d6ebff;
--vscode-editor-wordHighlightTextBackground: rgba(173, 214, 255, 0.45);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(0, 0, 0, 0);
--vscode-peekViewTitle-background: #f3f3f3;
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewEditorStickyScroll-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #f7f7f7;
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #000000;
--vscode-editorSuggestWidget-selectedBackground: #d6ebff;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #0066bf;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editorGutter-foldingControlForeground: #424242; }

.mtk1 { color: #000000; }
.mtk2 { color: #f7f7f7; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #811f3f; }
.mtk11 { color: #e00000; }
.mtk12 { color: #116644; }
.mtk13 { color: #383838; }
.mtk14 { color: #257693; }
.mtk15 { color: #795e26; }
.mtk16 { color: #001080; }
.mtk17 { color: #cd3131; }
.mtk18 { color: #863b00; }
.mtk19 { color: #af00db; }
.mtk20 { color: #c43b3b; }
.mtk21 { color: #800000; }
.mtk22 { color: #3030c0; }
.mtk23 { color: #666666; }
.mtk24 { color: #778899; }
.mtk25 { color: #c700c7; }
.mtk26 { color: #a31515; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #008080; }
.mtk29 { color: #001188; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script src="./ML._files/api(2).js.download" nonce=""></script><script src="./ML._files/api(3).js.download" nonce=""></script><script async="async" type="text/javascript" src="./ML._files/python.js.download"></script></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./ML._files/gapi_loader.js.download" nonce=""></script><script src="./ML._files/socketio_binary.js.download" nonce=""></script><script src="./ML._files/analytics_binary.js.download" nonce=""></script><script src="./ML._files/MathJax.js.download" nonce=""></script><script src="./ML._files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./ML._files/external_binary_l10n__en_gb.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$972977003$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$972977003$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$972977003$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$972977003$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Loading…</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_s" ng-non-bindable=""><div class="gb_xc"><div>Google Account</div><div class="gb_xb">Pooja Madivalar</div><div>poojamadivalar00@gmail.com</div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var xd;xd=class extends _.id{};_.yd=function(a,b){if(b in a.i)return a.i[b];throw new xd;};_.zd=function(a){return _.yd(_.fd.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 SPDX-License-Identifier: Apache-2.0
*/
var Fd,Pd,Rd;_.Ad=function(a){if(a==null)return a;if(typeof a==="string"){if(!a)return;a=+a}if(typeof a==="number")return Number.isFinite(a)?a|0:void 0};_.Bd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};_.Dd=function(a){if(a instanceof _.Cd)return a.i;throw Error("D");};Fd=function(a){return new Ed(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};
_.Hd=function(a,b=_.Gd){if(a instanceof _.Cd)return a;for(let c=0;c<b.length;++c){const d=b[c];if(d instanceof Ed&&d.Vg(a))return new _.Cd(a)}};_.Jd=function(a){if(Id.test(a))return a};_.Kd=function(a){return a instanceof _.Cd?_.Dd(a):_.Jd(a)};_.Ld=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.Md=function(a,b,c){return _.sb(a,b,c,!1)!==void 0};_.Nd=function(a,b){return _.Ad(_.Cc(a,b))};
_.S=function(a,b){a=_.Cc(a,b);return a==null?a:Number.isFinite(a)?a|0:void 0};_.T=function(a,b,c=0){return _.tb(_.Nd(a,b),c)};_.Od=function(a,b,c=0){return _.tb(_.S(a,b),c)};Pd=0;_.Qd=function(a){return Object.prototype.hasOwnProperty.call(a,_.Ib)&&a[_.Ib]||(a[_.Ib]=++Pd)};Rd=function(a){return a};_.Sd=function(a){var b=null,c=_.t.trustedTypes;if(!c||!c.createPolicy)return b;try{b=c.createPolicy(a,{createHTML:Rd,createScript:Rd,createScriptURL:Rd})}catch(d){_.t.console&&_.t.console.error(d.message)}return b};
_.Td=function(a,b){return a.lastIndexOf(b,0)==0};_.Ud=function(a,b){return Array.prototype.some.call(a,b,void 0)};var Vd;_.Wd=function(){Vd===void 0&&(Vd=_.Sd("ogb-qtm#html"));return Vd};var Zd;_.Xd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Yd=function(a){return a instanceof _.Xd&&a.constructor===_.Xd?a.i:"type_error:TrustedResourceUrl"};Zd={};_.$d=function(a){const b=_.Wd();a=b?b.createScriptURL(a):a;return new _.Xd(a,Zd)};_.Cd=class{constructor(a){this.i=a}toString(){return this.i}};_.ae=new _.Cd("about:invalid#zClosurez");var Ed,Id;Ed=class{constructor(a){this.Vg=a}};_.Gd=[Fd("data"),Fd("http"),Fd("https"),Fd("mailto"),Fd("ftp"),new Ed(a=>/^[^:]*([/?#]|$)/.test(a))];Id=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;_.be={};_.ce=class{constructor(a){this.i=a}toString(){return this.i.toString()}};_.de=new _.ce("",_.be);_.ee=RegExp("^[-+,.\"'%_!#/ a-zA-Z0-9\\[\\]]+$");_.fe=RegExp("\\b(url\\([ \t\n]*)('[ -&(-\\[\\]-~]*'|\"[ !#-\\[\\]-~]*\"|[!#-&*-\\[\\]-~]*)([ \t\n]*\\))","g");_.ge=RegExp("\\b(calc|cubic-bezier|fit-content|hsl|hsla|linear-gradient|matrix|minmax|radial-gradient|repeat|rgb|rgba|(rotate|scale|translate)(X|Y|Z|3d)?|steps|var)\\([-+*/0-9a-zA-Z.%#\\[\\], ]+\\)","g");_.he={};_.je=function(a){return a instanceof _.ie&&a.constructor===_.ie?a.i:"type_error:SafeHtml"};_.ie=class{constructor(a){this.i=a}toString(){return this.i.toString()}};_.ke=new _.ie(_.t.trustedTypes&&_.t.trustedTypes.emptyHTML||"",_.he);_.le=function(a){let b=!1,c;return function(){b||(c=a(),b=!0);return c}}(function(){var a=document.createElement("div"),b=document.createElement("div");b.appendChild(document.createElement("div"));a.appendChild(b);b=a.firstChild.firstChild;a.innerHTML=_.je(_.ke);return!b.parentElement});_.me=function(a,b){this.width=a;this.height=b};_.n=_.me.prototype;_.n.aspectRatio=function(){return this.width/this.height};_.n.Bb=function(){return!(this.width*this.height)};_.n.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};_.n.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};_.n.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};_.U=function(a,b){var c=b||document;if(c.getElementsByClassName)a=c.getElementsByClassName(a)[0];else{c=document;var d=b||c;a=d.querySelectorAll&&d.querySelector&&a?d.querySelector(a?"."+a:""):_.ne(c,a,b)[0]||null}return a||null};
_.ne=function(a,b,c){var d;a=c||a;if(a.querySelectorAll&&a.querySelector&&b)return a.querySelectorAll(b?"."+b:"");if(b&&a.getElementsByClassName){var e=a.getElementsByClassName(b);return e}e=a.getElementsByTagName("*");if(b){var f={};for(c=d=0;a=e[c];c++){var g=a.className;typeof g.split=="function"&&_.ta(g.split(/\s+/),b)&&(f[d++]=a)}f.length=d;return f}return e};_.pe=function(a){return _.oe(document,a)};
_.oe=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.qe=function(a){for(var b;b=a.firstChild;)a.removeChild(b)};_.re=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};
}catch(e){_._DumpException(e)}
try{
_.Oi=function(a,b){let c,d;return(b=(d=(c=b.document).querySelector)==null?void 0:d.call(c,`${a}[nonce]`))?b.nonce||b.getAttribute("nonce")||"":""};_.Pi=function(a){const b=_.Oi("script",a.ownerDocument&&a.ownerDocument.defaultView||window);b&&a.setAttribute("nonce",b)};_.Qi=function(a){if(!a)return null;a=_.J(a,4);var b;a===null||a===void 0?b=null:b=_.$d(a);return b};_.Ri=class extends _.Q{constructor(a){super(a)}};_.Si=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Ui=function(a,b,c){a<b?Ti(a+1,b):_.Oc.log(Error("ca`"+a+"`"+b),{url:c})},Ti=function(a,b){if(Vi){const c=_.pe("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.Yd(Vi);_.Pi(c);c.onerror=_.Ld(Ui,a,b,c.src);_.Si("HEAD")[0].appendChild(c)}},Wi=class extends _.Q{constructor(a){super(a)}};var Xi=_.G(_.$c,Wi,17)||new Wi,Yi,Vi=(Yi=_.G(Xi,_.Ri,1))?_.Qi(Yi):null,Zi,$i=(Zi=_.G(Xi,_.Ri,2))?_.Qi(Zi):null,aj=function(){Ti(1,2);if($i){const a=_.pe("LINK");a.setAttribute("type","text/css");a.href=_.Yd($i).toString();a.rel="stylesheet";let b=_.Oi("style",window);b&&a.setAttribute("nonce",b);_.Si("HEAD")[0].appendChild(a)}};(function(){const a=_.ad();if(_.I(a,18))aj();else{const b=_.Nd(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(aj,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><iframe id="apiproxy59b2073d82bfa5c564f0ce0efec1e606d5c893d10.218078006" name="apiproxy59b2073d82bfa5c564f0ce0efec1e606d5c893d10.218078006" src="./ML._files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><iframe src="./ML._files/bscframe.html" style="display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-ldfzmmx2v3sm" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./ML._files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./ML._files/saved_resource(1).html"></iframe></div><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./ML._files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <div class="top-floater"><div role="banner">
    <colab-header-skip-button><template shadowrootmode="open"><!----><a id="skiplink" class="skip-link" href="https://colab.research.google.com/drive/1y4539Hc4d28v2fttdrFJlC1Ky7LOvWeo#top-toolbar"><!--?lit$972977003$-->Skip to main content</a></template></colab-header-skip-button>
    <!--?lit$972977003$-->
    <!--?lit$972977003$-->
    <!--?lit$972977003$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning hidden">
            <!--?lit$972977003$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1y4539Hc4d28v2fttdrFJlC1Ky7LOvWeo#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
          <mwc-icon-button class="close" icon="close" title="Close"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Close"><!--?lit$972977003$-->
    <!--?lit$972977003$--><i class="material-icons"><!--?lit$972977003$-->close</i>
    <span><slot></slot></span>
  </button></template></mwc-icon-button></div>
        

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><div id="header-logo">
              <!--?lit$972977003$--> <!--?lit$972977003$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$972977003$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$972977003$--> <!--?lit$972977003$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 140.788px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Untitled3.ipynbS_</colab-input-sizer>
            <!--?lit$972977003$-->
                  <div class="screenreader-only" id="star-status" aria-live="polite">Notebook unstarred</div>
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$972977003$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$972977003$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$972977003$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$972977003$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$972977003$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$972977003$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$972977003$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$972977003$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div>
    <div id="colab-menu-cover" style="left: 65px; top: 60px; width: 34px; display: none;"> </div></div><!----><colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$972977003$-->All changes saved</button></template></colab-last-saved-indicator></div></div>
        <div id="header-right">
          <!--?lit$972977003$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$972977003$-->
      <!--?lit$972977003$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$972977003$--> <md-text-button id="comments" command="open-comments-thread" aria-describedby="comments-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
                <!--?lit$972977003$-->Comment
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$972977003$--> <md-text-button id="share-toolbar-button" command="share" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->people</md-icon>
                <!--?lit$972977003$-->Share
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$972977003$--> <md-icon-button id="settings-cog" command="preferences" title="Open settings" data-aria-label="Open settings" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button>
          <div class="header-onegoogle-container"></div>
        </div>
      </div>
    </div>
  </div></div><div class="notebook-horizontal">
        <!--?lit$972977003$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$972977003$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$972977003$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$972977003$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->search</md-icon>
    </md-icon-button> <!--?lit$972977003$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$972977003$--><md-icon-button toggle="" command="show-variables" data-aria-label="Variables" title="Variables" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Variables" aria-pressed="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
    </md-icon-button> <!--?lit$972977003$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$972977003$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$972977003$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$972977003$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->folder</md-icon>
    </md-icon-button> <!--?lit$972977003$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$972977003$--><md-icon-button command="snippets" data-aria-label="Code snippets" title="Code snippets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->code</md-icon>
    </md-icon-button> <!--?lit$972977003$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$972977003$--><md-icon-button command="show-command-palette" data-aria-label="Command palette" title="Command palette" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Command palette">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$-->
      <path d="M21,3H3A2,2,0,0,0,1,5V17a2,2,0,0,0,2,2H21a2,2,0,0,0,2-2V5A2,2,0,0,0,21,3Zm0,2V17H3V5"></path>
      <rect x="5" y="12" width="11" height="2"></rect>
      <rect x="5" y="8" width="11" height="2"></rect>
      <rect x="17" y="8" width="2" height="2"></rect>
      <rect x="17" y="12" width="2" height="2"></rect></svg></md-icon>
    </md-icon-button> <!--?lit$972977003$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$972977003$--><md-icon-button command="show-terminal" data-aria-label="Terminal" title="Terminal" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terminal">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->terminal</md-icon>
    </md-icon-button> <!--?lit$972977003$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$972977003$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
        <!--?lit$972977003$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$972977003$--><span class="screenreader-only"><!--?lit$972977003$-->Insert code cell below <!--?lit$972977003$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$972977003$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$972977003$-->Code
          </colab-toolbar-button>
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
        <!--?lit$972977003$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$972977003$--><span class="screenreader-only"><!--?lit$972977003$-->Add text cell <!--?lit$972977003$--></span>
      </md-text-button>
      <!--?lit$972977003$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$972977003$-->Text
          </colab-toolbar-button>
          <!--?lit$972977003$-->
        
    <!--?lit$972977003$-->
    <!--?lit$972977003$-->
    <!--?lit$972977003$-->
    <!--?lit$972977003$-->
    <!--?lit$972977003$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$972977003$-->All changes saved</button></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$972977003$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$972977003$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$972977003$--><!--?lit$972977003$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$972977003$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Focus the last run cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Focus the last run cell">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Focus the last run cell"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connected to

          Python 3 Google Compute Engine backend

          

RAM: 1.35 GB/12.67 GB
Disk: 30.94 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
        <!--?lit$972977003$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$972977003$--><span class="screenreader-only"><!--?lit$972977003$-->Connected to

          Python 3 Google Compute Engine backend

          

RAM: 1.35 GB/12.67 GB
Disk: 30.94 GB/107.72 GB <!--?lit$972977003$--></span>
      </md-text-button>
      <!--?lit$972977003$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connected to

          Python 3 Google Compute Engine backend

          

RAM: 1.35 GB/12.67 GB
Disk: 30.94 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Connected to</div><!----><!----><div><!--?lit$972977003$--></div><!----><!----><div><!--?lit$972977003$-->          Python 3 Google Compute Engine backend</div><!----><!----><div><!--?lit$972977003$--></div><!----><!----><div><!--?lit$972977003$-->          </div><!----><!----><div><!--?lit$972977003$--></div><!----><!----><div><!--?lit$972977003$-->RAM: 1.35 GB/12.67 GB</div><!----><!----><div><!--?lit$972977003$-->Disk: 30.94 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$972977003$--> <div id="connect-button-resource-display">
        <!--?lit$972977003$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$972977003$-->RAM</div>
      <!--?lit$972977003$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        <!--?lit$972977003$--><colab-usage-sparkline class="disks" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$972977003$-->Disk</div>
      <!--?lit$972977003$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
      </div>
      </colab-toolbar-button>
      <!--?lit$972977003$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$972977003$--> <span class="colab-separator"></span>
          <colab-toolbar-button command="show-chat" icon="spark"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
        <!--?lit$972977003$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->spark</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$972977003$--><span class="screenreader-only"><!--?lit$972977003$--> <!--?lit$972977003$--></span>
      </md-text-button>
      <!--?lit$972977003$--><!--?--></template>
            <!--?lit$972977003$-->Gemini
          </colab-toolbar-button>
    <!--?lit$972977003$-->
    <span class="collapsed-options">
      <!--?lit$972977003$--><span class="colab-separator"></span>
      <!--?lit$972977003$--> <md-icon-button command="share" title="Share notebook" data-aria-label="Share notebook" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->people</md-icon>
          </md-icon-button><md-icon-button command="preferences" data-aria-label="Open settings" title="Open settings" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$972977003$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----><div><!--?lit$972977003$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$972977003$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$972977003$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-LMm0ETAp0C4M" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$972977003$--><div class="indicator"></div>
      </div>
      <!--?lit$972977003$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-LMm0ETAp0C4M"><!--?lit$972977003$--><!--?lit$972977003$-->Notebook<!--?--></span>
            <!--?lit$972977003$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$972977003$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Show more" data-aria-label="Show more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show more" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" role="main" class="notebook-container" aria-label="Notebook" tabindex="-1">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$972977003$-->
              <div class="notebook-content ">
                <!--?lit$972977003$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Text
        </md-outlined-button>
        <!--?lit$972977003$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code icon-scrolling code-has-output" id="cell-wkisi9Hm6GDj" role="region" aria-label="Cell 0: Code cell: " tabindex="-1" style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button title="Run cell (Ctrl+Enter)
cell executed since last change

executed by Pooja Madivalar
13:50 (24 minutes ago)
executed in 0.691 s"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button aria-label="Run cell">
        <span class="execution-count"><!--?lit$972977003$-->[7]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$972977003$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$972977003$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$972977003$--><div id="status">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$972977003$-->0s</div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab" data-lang="notebook-python"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;tree</span></span><br><span><span class="mtk1">features&nbsp;=&nbsp;[[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">],[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">],[</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">],[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">],[</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">]]</span></span><br><span><span class="mtk1">labels&nbsp;=&nbsp;[</span><span class="mtk26">"TCC"</span><span class="mtk1">,</span><span class="mtk26">"CC"</span><span class="mtk1">,</span><span class="mtk26">"TCC"</span><span class="mtk1">,</span><span class="mtk26">"CC"</span><span class="mtk1">,</span><span class="mtk26">"cc"</span><span class="mtk1">]</span></span><br><span><span class="mtk1">myClassifier=tree.DecisionTreeClassifier()</span></span><br><span><span class="mtk1">myModel=myClassifier.fit(features,labels)</span></span><br><span><span class="mtk1">myModel.predict([[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">]])</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$972977003$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Code cell output actions" data-aria-label="Code cell output actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
    </md-icon-button></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="execute_result output-id-1 output_text"><pre>array(['cc'], dtype='&lt;U3')</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Text
        </md-outlined-button>
        <!--?lit$972977003$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-_4lfSarW7SIM" tabindex="-1" role="region" aria-label="Cell 1: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button title="Run cell (Ctrl+Enter)
cell executed since last change

executed by Pooja Madivalar
13:53 (21 minutes ago)
executed in 0.538 s"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button aria-label="Run cell">
        <span class="execution-count"><!--?lit$972977003$-->[9]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$972977003$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$972977003$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$972977003$--><div id="status">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$972977003$-->0s</div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;tree</span></span><br><span><span class="mtk1">features&nbsp;=&nbsp;[[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">],[</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">],[</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">]]</span></span><br><span><span class="mtk1">labels&nbsp;=&nbsp;[</span><span class="mtk26">"TCC"</span><span class="mtk1">,</span><span class="mtk26">"CC"</span><span class="mtk1">,</span><span class="mtk26">"TCC"</span><span class="mtk1">]</span></span><br><span><span class="mtk1">myClassifier=tree.DecisionTreeClassifier()</span></span><br><span><span class="mtk1">myModel=myClassifier.fit(features,labels)</span></span><br><span><span class="mtk1">myModel.predict([[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">]])</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$972977003$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 1 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Code cell output actions" data-aria-label="Code cell output actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
    </md-icon-button></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="execute_result output-id-1 output_text"><pre>array(['CC'], dtype='&lt;U3')</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Text
        </md-outlined-button>
        <!--?lit$972977003$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-nAP7D8gv7_Bv" tabindex="-1" role="region" aria-label="Cell 2: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button title="Run cell (Ctrl+Enter)
cell executed since last change

executed by Pooja Madivalar
13:56 (18 minutes ago)
executed in 0.679 s"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button aria-label="Run cell">
        <span class="execution-count"><!--?lit$972977003$-->[11]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$972977003$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$972977003$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$972977003$--><div id="status">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$972977003$-->0s</div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;tree</span></span><br><span><span class="mtk1">features&nbsp;=&nbsp;[[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">],[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">],[</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">],[</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">],[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">,</span><span class="mtk12">1</span><span class="mtk1">]]</span></span><br><span><span class="mtk1">labels&nbsp;=&nbsp;[</span><span class="mtk26">"TCC"</span><span class="mtk1">,</span><span class="mtk26">"CC"</span><span class="mtk1">,</span><span class="mtk26">"TCC"</span><span class="mtk1">,</span><span class="mtk26">"CC"</span><span class="mtk1">,</span><span class="mtk26">"TCC"</span><span class="mtk1">]</span></span><br><span><span class="mtk1">myClassifier=tree.DecisionTreeClassifier()</span></span><br><span><span class="mtk1">myModel=myClassifier.fit(features,labels)</span></span><br><span><span class="mtk1">myModel.predict([[</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">,</span><span class="mtk12">0</span><span class="mtk1">]])</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$972977003$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Code cell output actions" data-aria-label="Code cell output actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
    </md-icon-button></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="execute_result output-id-1 output_text"><pre>array(['CC'], dtype='&lt;U3')</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Text
        </md-outlined-button>
        <!--?lit$972977003$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling" id="cell-LLZGECm396WK" tabindex="-1" role="region" aria-label="Cell 3: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button title="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button aria-label="Run cell">
        <span class="execution-count"><!--?lit$972977003$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$972977003$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$972977003$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$972977003$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: block;"><template shadowrootmode="open"><!----><div><!--?lit$972977003$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 3 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> <div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Text
        </md-outlined-button>
        <!--?lit$972977003$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling code-has-output" id="cell-9oaP168K97Rh" tabindex="-1" role="region" aria-label="Cell 4: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button title="Run cell (Ctrl+Enter)
cell executed since last change

executed by Pooja Madivalar
14:02 (12 minutes ago)
executed in 14.967 s"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button aria-label="Run cell">
        <span class="execution-count"><!--?lit$972977003$-->[12]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$972977003$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$972977003$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$972977003$--><div id="status">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$972977003$-->14s</div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk1">pip&nbsp;install&nbsp;gradio</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$972977003$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 4 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Code cell output actions" data-aria-label="Code cell output actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
    </md-icon-button></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-16 output_text"><pre>Collecting gradio
  Downloading gradio-4.40.0-py3-none-any.whl.metadata (15 kB)
Collecting aiofiles&lt;24.0,&gt;=22.0 (from gradio)
  Downloading aiofiles-23.2.1-py3-none-any.whl.metadata (9.7 kB)
Requirement already satisfied: anyio&lt;5.0,&gt;=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.7.1)
Collecting fastapi (from gradio)
  Downloading fastapi-0.112.0-py3-none-any.whl.metadata (27 kB)
Collecting ffmpy (from gradio)
  Downloading ffmpy-0.4.0-py3-none-any.whl.metadata (2.9 kB)
Collecting gradio-client==1.2.0 (from gradio)
  Downloading gradio_client-1.2.0-py3-none-any.whl.metadata (7.1 kB)
Collecting httpx&gt;=0.24.1 (from gradio)
  Downloading httpx-0.27.0-py3-none-any.whl.metadata (7.2 kB)
Requirement already satisfied: huggingface-hub&gt;=0.19.3 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.23.5)
Requirement already satisfied: importlib-resources&lt;7.0,&gt;=1.3 in /usr/local/lib/python3.10/dist-packages (from gradio) (6.4.0)
Requirement already satisfied: jinja2&lt;4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.1.4)
Requirement already satisfied: markupsafe~=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.1.5)
Requirement already satisfied: matplotlib~=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.7.1)
Requirement already satisfied: numpy&lt;3.0,&gt;=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (1.26.4)
Collecting orjson~=3.0 (from gradio)
  Downloading orjson-3.10.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (50 kB)
     <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">50.4/50.4 kB</span><span> </span><span style="color: var(--ansi-red);">3.7 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from gradio) (24.1)
Requirement already satisfied: pandas&lt;3.0,&gt;=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.1.4)
Requirement already satisfied: pillow&lt;11.0,&gt;=8.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (9.4.0)
Requirement already satisfied: pydantic&gt;=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.8.2)
Collecting pydub (from gradio)
  Downloading pydub-0.25.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting python-multipart&gt;=0.0.9 (from gradio)
  Downloading python_multipart-0.0.9-py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: pyyaml&lt;7.0,&gt;=5.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (6.0.1)
Collecting ruff&gt;=0.2.2 (from gradio)
  Downloading ruff-0.5.6-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (24 kB)
Collecting semantic-version~=2.0 (from gradio)
  Downloading semantic_version-2.10.0-py2.py3-none-any.whl.metadata (9.7 kB)
Collecting tomlkit==0.12.0 (from gradio)
  Downloading tomlkit-0.12.0-py3-none-any.whl.metadata (2.7 kB)
Requirement already satisfied: typer&lt;1.0,&gt;=0.12 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.12.3)
Requirement already satisfied: typing-extensions~=4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (4.12.2)
Requirement already satisfied: urllib3~=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.0.7)
Collecting uvicorn&gt;=0.14.0 (from gradio)
  Downloading uvicorn-0.30.5-py3-none-any.whl.metadata (6.6 kB)
Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from gradio-client==1.2.0-&gt;gradio) (2024.6.1)
Collecting websockets&lt;13.0,&gt;=10.0 (from gradio-client==1.2.0-&gt;gradio)
  Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Requirement already satisfied: idna&gt;=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio&lt;5.0,&gt;=3.0-&gt;gradio) (3.7)
Requirement already satisfied: sniffio&gt;=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio&lt;5.0,&gt;=3.0-&gt;gradio) (1.3.1)
Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio&lt;5.0,&gt;=3.0-&gt;gradio) (1.2.2)
Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx&gt;=0.24.1-&gt;gradio) (2024.7.4)
Collecting httpcore==1.* (from httpx&gt;=0.24.1-&gt;gradio)
  Downloading httpcore-1.0.5-py3-none-any.whl.metadata (20 kB)
Collecting h11&lt;0.15,&gt;=0.13 (from httpcore==1.*-&gt;httpx&gt;=0.24.1-&gt;gradio)
  Downloading h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)
Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub&gt;=0.19.3-&gt;gradio) (3.15.4)
Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface-hub&gt;=0.19.3-&gt;gradio) (2.31.0)
Requirement already satisfied: tqdm&gt;=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub&gt;=0.19.3-&gt;gradio) (4.66.4)
Requirement already satisfied: contourpy&gt;=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0-&gt;gradio) (1.2.1)
Requirement already satisfied: cycler&gt;=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0-&gt;gradio) (0.12.1)
Requirement already satisfied: fonttools&gt;=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0-&gt;gradio) (4.53.1)
Requirement already satisfied: kiwisolver&gt;=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0-&gt;gradio) (1.4.5)
Requirement already satisfied: pyparsing&gt;=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0-&gt;gradio) (3.1.2)
Requirement already satisfied: python-dateutil&gt;=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0-&gt;gradio) (2.8.2)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas&lt;3.0,&gt;=1.0-&gt;gradio) (2024.1)
Requirement already satisfied: tzdata&gt;=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas&lt;3.0,&gt;=1.0-&gt;gradio) (2024.1)
Requirement already satisfied: annotated-types&gt;=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic&gt;=2.0-&gt;gradio) (0.7.0)
Requirement already satisfied: pydantic-core==2.20.1 in /usr/local/lib/python3.10/dist-packages (from pydantic&gt;=2.0-&gt;gradio) (2.20.1)
Requirement already satisfied: click&gt;=8.0.0 in /usr/local/lib/python3.10/dist-packages (from typer&lt;1.0,&gt;=0.12-&gt;gradio) (8.1.7)
Requirement already satisfied: shellingham&gt;=1.3.0 in /usr/local/lib/python3.10/dist-packages (from typer&lt;1.0,&gt;=0.12-&gt;gradio) (1.5.4)
Requirement already satisfied: rich&gt;=10.11.0 in /usr/local/lib/python3.10/dist-packages (from typer&lt;1.0,&gt;=0.12-&gt;gradio) (13.7.1)
Collecting starlette&lt;0.38.0,&gt;=0.37.2 (from fastapi-&gt;gradio)
  Downloading starlette-0.37.2-py3-none-any.whl.metadata (5.9 kB)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil&gt;=2.7-&gt;matplotlib~=3.0-&gt;gradio) (1.16.0)
Requirement already satisfied: markdown-it-py&gt;=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich&gt;=10.11.0-&gt;typer&lt;1.0,&gt;=0.12-&gt;gradio) (3.0.0)
Requirement already satisfied: pygments&lt;3.0.0,&gt;=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich&gt;=10.11.0-&gt;typer&lt;1.0,&gt;=0.12-&gt;gradio) (2.16.1)
Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in /usr/local/lib/python3.10/dist-packages (from requests-&gt;huggingface-hub&gt;=0.19.3-&gt;gradio) (3.3.2)
Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py&gt;=2.2.0-&gt;rich&gt;=10.11.0-&gt;typer&lt;1.0,&gt;=0.12-&gt;gradio) (0.1.2)
Downloading gradio-4.40.0-py3-none-any.whl (12.5 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">12.5/12.5 MB</span><span> </span><span style="color: var(--ansi-red);">46.6 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading gradio_client-1.2.0-py3-none-any.whl (318 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">318.6/318.6 kB</span><span> </span><span style="color: var(--ansi-red);">18.7 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading tomlkit-0.12.0-py3-none-any.whl (37 kB)
Downloading aiofiles-23.2.1-py3-none-any.whl (15 kB)
Downloading httpx-0.27.0-py3-none-any.whl (75 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">75.6/75.6 kB</span><span> </span><span style="color: var(--ansi-red);">5.1 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading httpcore-1.0.5-py3-none-any.whl (77 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">77.9/77.9 kB</span><span> </span><span style="color: var(--ansi-red);">6.0 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading orjson-3.10.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (141 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">141.1/141.1 kB</span><span> </span><span style="color: var(--ansi-red);">10.0 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading python_multipart-0.0.9-py3-none-any.whl (22 kB)
Downloading ruff-0.5.6-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.2 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">10.2/10.2 MB</span><span> </span><span style="color: var(--ansi-red);">48.8 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)
Downloading uvicorn-0.30.5-py3-none-any.whl (62 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">62.8/62.8 kB</span><span> </span><span style="color: var(--ansi-red);">4.3 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading fastapi-0.112.0-py3-none-any.whl (93 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">93.1/93.1 kB</span><span> </span><span style="color: var(--ansi-red);">6.8 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading ffmpy-0.4.0-py3-none-any.whl (5.8 kB)
Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)
Downloading h11-0.14.0-py3-none-any.whl (58 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">58.3/58.3 kB</span><span> </span><span style="color: var(--ansi-red);">3.7 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading starlette-0.37.2-py3-none-any.whl (71 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">71.9/71.9 kB</span><span> </span><span style="color: var(--ansi-red);">5.0 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (130 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">130.2/130.2 kB</span><span> </span><span style="color: var(--ansi-red);">8.9 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Installing collected packages: pydub, websockets, tomlkit, semantic-version, ruff, python-multipart, orjson, h11, ffmpy, aiofiles, uvicorn, starlette, httpcore, httpx, fastapi, gradio-client, gradio
  Attempting uninstall: tomlkit
    Found existing installation: tomlkit 0.13.0
    Uninstalling tomlkit-0.13.0:
      Successfully uninstalled tomlkit-0.13.0
Successfully installed aiofiles-23.2.1 fastapi-0.112.0 ffmpy-0.4.0 gradio-4.40.0 gradio-client-1.2.0 h11-0.14.0 httpcore-1.0.5 httpx-0.27.0 orjson-3.10.6 pydub-0.25.1 python-multipart-0.0.9 ruff-0.5.6 semantic-version-2.10.0 starlette-0.37.2 tomlkit-0.12.0 uvicorn-0.30.5 websockets-12.0
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Text
        </md-outlined-button>
        <!--?lit$972977003$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling focused code-has-output" id="cell-hF7y1D3u_GO5" tabindex="-1" role="region" aria-label="Cell 5: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$972977003$--><!----> <md-icon-button class="colab-icon" title="Move cell up
Ctrl+M K" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->arrow_upward</md-icon>
          <!--?lit$972977003$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Move cell down
Ctrl+M J" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" disabled="">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->arrow_downward</md-icon>
          <!--?lit$972977003$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Copy link to cell" data-aria-label="Copy link to cell" command="copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->link</md-icon>
          <!--?lit$972977003$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Add a comment
Ctrl+Alt+M" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->comment</md-icon>
          <!--?lit$972977003$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Open editor settings" data-aria-label="Open editor settings" command="editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
          <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->settings</md-icon>
          <!--?lit$972977003$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Edit" data-aria-label="Edit" command="toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->edit</md-icon>
          <!--?lit$972977003$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->edit_off</md-icon>
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Mirror cell in tab" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
          <!--?lit$972977003$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Delete cell
Ctrl+M D" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->delete</md-icon>
          <!--?lit$972977003$-->
        </md-icon-button><!----><!--?lit$972977003$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More cell actions" data-aria-label="More cell actions" class="colab-icon cell-toolbar-more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button title="Run cell (Ctrl+Enter)
cell executed since last change

executed by Pooja Madivalar
14:07 (7 minutes ago)
executed in 8.099 s"><template shadowrootmode="open"><!----> <div class="cell-execution focused">
      <button aria-label="Run cell">
        <span class="execution-count"><!--?lit$972977003$-->[13]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$972977003$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$972977003$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$972977003$--><div id="status">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$972977003$-->8s</div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="14" data-mode-id="notebook-python" style="height: 409px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/30" style="width: 1411px; height: 409px;"><div data-mprt="3" class="overflow-guard" style="width: 1411px; height: 409px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 409px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 409px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 409px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1405px; height: 409px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 409px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1405px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"><div class="current-line" style="width:1405px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 409px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1405px; height: 409px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;gradio&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;gr</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;tree</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Define&nbsp;the&nbsp;features&nbsp;and&nbsp;labels</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">features&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk1">labels&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk26">"TCC"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"CC"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"TCC"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"CC"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"cc"</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Train&nbsp;the&nbsp;decision&nbsp;tree&nbsp;classifier</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">myClassifier&nbsp;=&nbsp;tree.DecisionTreeClassifier</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">myModel&nbsp;=&nbsp;myClassifier.fit</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">features,&nbsp;labels</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Create&nbsp;the&nbsp;Gradio&nbsp;interface</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">inputs&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">gr.Number</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">label=</span><span class="mtk26">"Feature&nbsp;1"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,&nbsp;gr.Number</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">label=</span><span class="mtk26">"Feature&nbsp;2"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,&nbsp;gr.Number</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">label=</span><span class="mtk26">"Feature&nbsp;3"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">outputs&nbsp;=&nbsp;gr.Textbox</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">label=</span><span class="mtk26">"Prediction"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">gr.Interface</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">fn=</span><span class="mtk6">lambda</span><span class="mtk1">&nbsp;f1,&nbsp;f2,&nbsp;f3:&nbsp;myModel.predict</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk1 bracket-highlighting-3">[</span><span class="mtk1">f1,&nbsp;f2,&nbsp;f3</span><span class="mtk1 bracket-highlighting-3">]</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inputs=inputs,&nbsp;</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outputs=outputs,&nbsp;</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;title=</span><span class="mtk26">"Decision&nbsp;Tree&nbsp;Classifier"</span><span class="mtk1">,&nbsp;</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description=</span><span class="mtk26">"Predict&nbsp;the&nbsp;label&nbsp;based&nbsp;on&nbsp;the&nbsp;features"</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">.launch</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 380px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1391px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1391px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="511" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 409px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 409px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 409px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1411px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 380px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1411px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 409px;"><div class="minimap-shadow-hidden" style="height: 409px;"></div><canvas width="0" height="511" style="position: absolute; left: 0px; width: 0px; height: 409px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="511" style="position: absolute; left: 0px; width: 0px; height: 409px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1536px; top: 163.85px; left: 393.4px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal disabled" style="top: 8px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" style="width: 0px; height: 0px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 931.26px; max-height: 250px; width: 0px; height: 0px;"><div class="hover-row markdown-hover"><div class="hover-contents"><div class="rendered-markdown"><p>Loading...</p></div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 5 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Code cell output actions" data-aria-label="Code cell output actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
    </md-icon-button></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 626px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals allow-popups-to-escape-sandbox" src="./ML._files/outputframe.html" class="" style="height: 626px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$972977003$-->Text
        </md-outlined-button>
        <!--?lit$972977003$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$972977003$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$972977003$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$972977003$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -2px inset;"></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$972977003$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$972977003$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Show more" data-aria-label="Show more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show more" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$972977003$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$972977003$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$972977003$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Show more" data-aria-label="Show more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show more" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$972977003$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$972977003$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Show more" data-aria-label="Show more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show more" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./ML._files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals allow-popups-to-escape-sandbox" src="./ML._files/outputframe(2).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar" style="min-height: inherit;"><template shadowrootmode="open"><!----> <!--?lit$972977003$--> <div class="connect-status">
        <md-icon status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$--><svg viewBox="0 0 24 24"><!--?lit$972977003$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
        <div aria-atomic="true" aria-live="polite"><!--?lit$972977003$-->Connected to Python 3 Google Compute Engine backend</div>
      </div>
      <md-icon-button class="visible-on-closed" title="Connected" disabled="" value="" data-aria-label="Connected"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Connected" disabled="">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$972977003$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <!--?lit$972977003$-->
      <md-icon-button title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$972977003$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$972977003$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$972977003$--><span class="icon"><slot></slot></span>
        <!--?lit$972977003$-->
        <!--?lit$972977003$--><span class="touch"></span>
        <!--?lit$972977003$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu colab-styled-scroller" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 664px; visibility: visible; left: 64px; top: 61px; display: none;"><!--?lit$972977003$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":33" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Locate in Drive<!--?lit$972977003$--></div></div><div command="open-in-playground" class="goog-menuitem" role="menuitem" id=":34" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Open in playground mode<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":35" style="user-select: none;"></div><div command="new" class="goog-menuitem" role="menuitem" id=":36" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->New notebook in Drive<!--?lit$972977003$--></div></div><div command="open" class="goog-menuitem" role="menuitem" id=":37" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Open notebook<!--?lit$972977003$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class="goog-menuitem" role="menuitem" id=":38" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Upload notebook<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":39" style="user-select: none;"></div><div command="rename" class="goog-menuitem" role="menuitem" id=":3a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Rename<!--?lit$972977003$--></div></div><div command="move-notebook" class="goog-menuitem " role="menuitem" id=":3b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Move<!--?lit$972977003$--></div></div><div command="trash" class="goog-menuitem " role="menuitem" id=":3c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Move to the bin<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3d" style="user-select: none;"></div><div command="clone" class="goog-menuitem " role="menuitem" id=":3e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Save a copy in Drive<!--?lit$972977003$--></div></div><div command="copy-to-gist" class="goog-menuitem " role="menuitem" id=":3f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Save a copy as a GitHub Gist<!--?lit$972977003$--></div></div><div command="copy-to-github" class="goog-menuitem " role="menuitem" id=":3g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Save a copy in GitHub<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3h" style="user-select: none;"></div><div command="save" class="goog-menuitem " role="menuitem" id=":3i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Save<!--?lit$972977003$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class="goog-menuitem " role="menuitem" id=":3j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Save and pin revision<!--?lit$972977003$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class="goog-menuitem " role="menuitem" id=":3k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Revision history<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3l" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$972977003$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class="goog-menuitem " role="menuitem" id=":3p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Print<!--?lit$972977003$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$972977003$--><div command="download-ipynb" class="goog-menuitem " role="menuitem" id=":3n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Download .ipynb<!--?lit$972977003$--></div></div><div command="download-python" class="goog-menuitem " role="menuitem" id=":3o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Download .py<!--?lit$972977003$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$972977003$--><div command="undo" class="goog-menuitem " role="menuitem" id=":3r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Undo<!--?lit$972977003$--></div></div><div command="redo" class="goog-menuitem " role="menuitem" id=":3s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Redo<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3t" style="user-select: none;"></div><div command="select-all" class="goog-menuitem " role="menuitem" id=":3u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Select all cells<!--?lit$972977003$--></div></div><div command="cut" class="goog-menuitem " role="menuitem" id=":3v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Cut cell or selection<!--?lit$972977003$--></div></div><div command="copy" class="goog-menuitem " role="menuitem" id=":3w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Copy cell or selection<!--?lit$972977003$--></div></div><div command="paste" class="goog-menuitem " role="menuitem" id=":3x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Paste<!--?lit$972977003$--></div></div><div command="delete-cell-or-selection" class="goog-menuitem " role="menuitem" id=":3y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Delete selected cells<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3z" style="user-select: none;"></div><div command="find" class="goog-menuitem " role="menuitem" id=":40" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Find and replace<!--?lit$972977003$--></div></div><div command="find-next" class="goog-menuitem " role="menuitem" id=":41" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Find next<!--?lit$972977003$--></div></div><div command="find-previous" class="goog-menuitem " role="menuitem" id=":42" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Find previous<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":43" style="user-select: none;"></div><div command="notebook-settings" class="goog-menuitem " role="menuitem" id=":44" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Notebook settings<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":45" style="user-select: none;"></div><div command="clear-outputs" class="goog-menuitem " role="menuitem" id=":46" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Clear all outputs<!--?lit$972977003$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$972977003$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":48" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$972977003$-->Table of contents<!--?lit$972977003$--></div></div><div command="show-fileinfo" class="goog-menuitem " role="menuitem" id=":49" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Notebook info<!--?lit$972977003$--></div></div><div command="show-executedcode" class="goog-menuitem " role="menuitem" id=":4a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Executed code history<!--?lit$972977003$--></div></div><div command="toggle-comments-visibility" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":4b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$972977003$-->Comments sidebar<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4c" style="user-select: none;"></div><div command="collapse-sections" class="goog-menuitem " role="menuitem" id=":4d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Collapse sections<!--?lit$972977003$--></div></div><div command="expand-sections" class="goog-menuitem " role="menuitem" id=":4e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Expand sections<!--?lit$972977003$--></div></div><div command="save-section-layout" class="goog-menuitem " role="menuitem" id=":4f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Save collapsed section layout<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4g" style="user-select: none;"></div><div command="hide-code" class="goog-menuitem " role="menuitem" id=":4h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Show/hide code<!--?lit$972977003$--></div></div><div command="toggle-output" class="goog-menuitem " role="menuitem" id=":4i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Show/hide output<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4j" style="user-select: none;"></div><div command="focus-next-tab" class="goog-menuitem " role="menuitem" id=":4k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Focus next tab<!--?lit$972977003$--></div></div><div command="focus-previous-tab" class="goog-menuitem " role="menuitem" id=":4l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Focus previous tab<!--?lit$972977003$--></div></div><div command="move-tab-to-next" class="goog-menuitem " role="menuitem" id=":4m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Move tab to next pane<!--?lit$972977003$--></div></div><div command="move-tab-to-prev" class="goog-menuitem " role="menuitem" id=":4n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Move tab to previous pane<!--?lit$972977003$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$972977003$--><div command="insert-cell-below" class="goog-menuitem " role="menuitem" id=":4p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Code cell<!--?lit$972977003$--></div></div><div command="add-text" class="goog-menuitem " role="menuitem" id=":4q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Text cell<!--?lit$972977003$--></div></div><div command="add-section-header" class="goog-menuitem " role="menuitem" id=":4r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Section header cell<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4s" style="user-select: none;"></div><div command="open-scratch-code-cell" class="goog-menuitem " role="menuitem" id=":4t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Scratch code cell<!--?lit$972977003$--></div></div><div command="snippets" class="goog-menuitem " role="menuitem" id=":4u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Code snippets<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4v" style="user-select: none;"></div><div command="add-form-field" class="goog-menuitem " role="menuitem" id=":4w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Add a form field<!--?lit$972977003$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$972977003$--><div command="runall" class="goog-menuitem " role="menuitem" id=":4y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Run all<!--?lit$972977003$--></div></div><div command="runbefore" class="goog-menuitem " role="menuitem" id=":4z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Run before<!--?lit$972977003$--></div></div><div command="runfocused" class="goog-menuitem " role="menuitem" id=":50" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Run the focused cell<!--?lit$972977003$--></div></div><div command="runselected" class="goog-menuitem " role="menuitem" id=":51" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Run selection<!--?lit$972977003$--></div></div><div command="runafter" class="goog-menuitem " role="menuitem" id=":52" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Run after<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":53" style="user-select: none;"></div><div command="interrupt" class="goog-menuitem " role="menuitem" id=":54" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Interrupt execution<!--?lit$972977003$--></div></div><div command="restart" class="goog-menuitem " role="menuitem" id=":55" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Restart session<!--?lit$972977003$--></div></div><div command="restart-and-run-all" class="goog-menuitem " role="menuitem" id=":56" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Restart session and run all<!--?lit$972977003$--></div></div><div command="powerwash-current-vm" class="goog-menuitem " role="menuitem" id=":57" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Disconnect and delete runtime<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":58" style="user-select: none;"></div><div command="change-runtime-type" class="goog-menuitem " role="menuitem" id=":59" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Change runtime type<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5a" style="user-select: none;"></div><div command="manage-sessions" class="goog-menuitem " role="menuitem" id=":5b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Manage sessions<!--?lit$972977003$--></div></div><div command="open-resource-viewer" class="goog-menuitem " role="menuitem" id=":5c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->View resources<!--?lit$972977003$--></div></div><div command="view-runtime-logs" class="goog-menuitem " role="menuitem" id=":5d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->View runtime logs<!--?lit$972977003$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$972977003$--><div command="show-command-palette" class="goog-menuitem " role="menuitem" id=":5f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Command palette<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5g" style="user-select: none;"></div><div command="preferences" class="goog-menuitem " role="menuitem" id=":5h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Settings<!--?lit$972977003$--></div></div><div command="shortcuts" class="goog-menuitem " role="menuitem" id=":5i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Keyboard shortcuts<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5j" style="user-select: none;"></div><div command="open-differ" class="goog-menuitem " role="menuitem" id=":5k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Diff notebooks<!--?lit$972977003$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$972977003$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$972977003$--><div command="faq" class="goog-menuitem " role="menuitem" id=":5m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Frequently asked questions<!--?lit$972977003$--></div></div><div command="view-relnotes" class="goog-menuitem " role="menuitem" id=":5n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->View release notes<!--?lit$972977003$--></div></div><div command="snippets" class="goog-menuitem " role="menuitem" id=":5o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Search code snippets<!--?lit$972977003$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5p" style="user-select: none;"></div><div command="report-bug" class="goog-menuitem " role="menuitem" id=":5q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Report a bug<!--?lit$972977003$--></div></div><div command="report-abuse" class="goog-menuitem " role="menuitem" id=":5r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Report Drive abuse<!--?lit$972977003$--></div></div><div command="send-feedback" class="goog-menuitem " role="menuitem" id=":5s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->Send feedback<!--?lit$972977003$--></div></div><div command="view-tos" class="goog-menuitem " role="menuitem" id=":5t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->View Terms of Service<!--?lit$972977003$--></div></div><div command="view-in-english" class="goog-menuitem " role="menuitem" id=":5u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$972977003$-->View in English<!--?lit$972977003$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$972977003$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$972977003$--><button id="button" class="button">
      <!--?lit$972977003$-->
      <span class="touch"></span>
      <!--?lit$972977003$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$972977003$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$972977003$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;"></div><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;">X: Any, Predict class or regression value for X.

For a classification model, the predicted class for each sample in X is
returned. For a regression model, the predicted value based on X is
returned.

Parameters
----------
X : {array-like, sparse matrix} of shape (n\_samples, n\_features)  
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;The input samples. Internally, it will be converted to
`dtype=np.float32` and if a sparse matrix is provided
to a sparse `csr_matrix`.

check\_input : bool, default=True  
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;Allow to bypass several input checking.
Don't use this parameter unless you know what you're doing.

Returns
-------
y : array-like of shape (n\_samples,) or (n\_samples, n\_outputs)  
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;The predicted classes, or the predict values., hint</div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><div><div class="grecaptcha-badge" data-style="none" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-9gnxewdyjx6y" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./ML._files/anchor(1).html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100001" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div></div></body></html>
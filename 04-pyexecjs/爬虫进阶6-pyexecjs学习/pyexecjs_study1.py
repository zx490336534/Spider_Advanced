#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import execjs

ctx = execjs.compile(r"""
passport._define("login.js", function() {
    function _(e) {
        alert("undefined:" + e)
    }
    var passport = passport || window.passport || {}
      , baidu = passport.tangramInst || baidu || window.baidu;
    !function(e) {
        e.apiDomain = {
            staticDomain: window.location ? "http:" == window.location.protocol.toLowerCase() ? "http://passport.bdimg.com" : "https://passport.baidu.com" : "http:" == document.location.protocol.toLowerCase() ? "http://passport.bdimg.com" : "https://passport.baidu.com"
        }
    }(passport);
    var magic = null;
    if ("function" != typeof magic)
        var magic = function() {};
    magic._baiduInstName = magic._baiduInstName || "bdInst_" + (new Date).getTime();
    var baiduInstance = baiduInstance || baidu.baiduInstance || window.baiduInstance;
    window[magic._baiduInstName] = window[magic._baiduInstName] || baiduInstance,
    magic.resourcePath = "",
    magic.skinName = "default",
    magic.version = "1.0.0.0",
    /msie 6/i.test(navigator.userAgent) && document.execCommand("BackgroundImageCache", !1, !0),
    baidu.form = baidu.form || {},
    baidu.url = baidu.url || {},
    baidu.url.escapeSymbol = baidu.url.escapeSymbol || function(e) {
        return String(e).replace(/[#%&+=\/\\\ \　\f\r\n\t]/g, function(e) {
            return "%" + (256 + e.charCodeAt()).toString(16).substring(1).toUpperCase()
        })
    }
    ,
    baidu.form.json = baidu.form.json || function(e, t) {
        function n(e, t) {
            var n = p[e];
            n ? (n.push || (p[e] = [n]),
            p[e].push(t)) : p[e] = t
        }
        for (var i, s, o, r, a, c, l, d, u = e.elements, t = t || function(e) {
            return e
        }
        , p = {}, g = 0, h = u.length; h > g; g++)
            if (i = u[g],
            o = i.name,
            !i.disabled && o)
                switch (s = i.type,
                r = baidu.url.escapeSymbol(i.value),
                s) {
                case "radio":
                case "checkbox":
                    if (!i.checked)
                        break;
                case "textarea":
                case "text":
                case "password":
                case "hidden":
                case "file":
                case "select-one":
                    n(o, t(r, o));
                    break;
                case "select-multiple":
                    for (a = i.options,
                    l = a.length,
                    c = 0; l > c; c++)
                        d = a[c],
                        d.selected && n(o, t(d.value, o))
                }
        return p
    }
    ,
    magic.Base = function() {
        baidu.lang.Class.call(this),
        this._ids = {},
        this._eid = this.guid + "__"
    }
    ,
    baidu.lang.inherits(magic.Base, baidu.lang.Class, "magic.Base").extend({
        getElement: function(e) {
            return document.getElementById(this.$getId(e))
        },
        getElements: function() {
            var e = {}
              , t = this._ids;
            for (var n in t)
                e[n] = this.getElement(n);
            return e
        },
        $getId: function(e) {
            return e = baidu.lang.isString(e) ? e : "",
            this._ids[e] || (this._ids[e] = this._eid + e)
        },
        $mappingDom: function(e, t) {
            return baidu.lang.isString(t) ? this._ids[e] = t : t && t.nodeType && (t.id ? this._ids[e] = t.id : t.id = this.$getId(e)),
            this
        },
        $hide: function(e) {
            return ("string" == (typeof e).toLowerCase() || "" === e) && (e = this.getElement(e)),
            e && e.style && (e.style.display = "none",
            e.style.visibility = "hidden"),
            this
        },
        $show: function(e) {
            return ("string" == (typeof e).toLowerCase() || "" === e) && (e = this.getElement(e)),
            e && e.style && (e.style.display = "block",
            e.style.visibility = "visible",
            e.style.opacity = "1"),
            this
        },
        $dispose: function() {
            this.fire("ondispose") && baidu.lang.Class.prototype.dispose.call(this)
        }
    }),
    magic.control = magic.control || {},
    function() {
        function e(e, t) {
            var i, s = e.getAttribute(t), o = !1;
            if (s && (i = s.match(n[0]))) {
                o = {};
                for (var r, a = 0; a < i.length; a++)
                    r = i[a].match(n[1]),
                    !isNaN(r[2]) && (r[2] = +r[2]),
                    n[2].test(r[2]) && (r[2] = r[2].replace(n[3], "$2")),
                    n[4].test(r[2]) && (r[2] = n[5].test(r[2])),
                    o[r[1]] = r[2]
            }
            return o
        }
        function t(t, n) {
            var i = e(t, "tang-event");
            if (i)
                for (var s in i) {
                    var o = i[s].substr(1);
                    o.indexOf("(") < 0 && (o += "()"),
                    baidu.dom(t).on(s, new Function(magic._baiduInstName + "('" + n + "') && " + magic._baiduInstName + "('" + n + "')" + o))
                }
        }
        magic.setup = magic.setup || function(n, i, s) {
            var o = e(n, "tang-param") || {};
            for (var r in s)
                o[r] = s[r];
            var a = new i(o);
            a.$mappingDom("", n),
            t(n, a.guid);
            for (var c = n.getElementsByTagName("*"), r = c.length - 1; r >= 0; r--)
                t(c[r], a.guid);
            return a
        }
        ;
        var n = [/\b[\w\$\-]+\s*:\s*[^;]+/g, /([\w\$\-]+)\s*:\s*([^;]+)\s*/, /\'|\"/, /^\s*(\'|\")([^\1]*)\1\s*/, /^(true|false)\s*$/i, /\btrue\b/i]
    }(),
    passport = passport || {},
    passport.lib = passport.lib || {},
    passport.lib.RSAExport = {},
    function(e) {
        function t(e, t, n) {
            null != e && ("number" == typeof e ? this.fromNumber(e, t, n) : null == t && "string" != typeof e ? this.fromString(e, 256) : this.fromString(e, t))
        }
        function n() {
            return new t(null)
        }
        function i(e, t, n, i, s, o) {
            for (; --o >= 0; ) {
                var r = t * this[e++] + n[i] + s;
                s = Math.floor(r / 67108864),
                n[i++] = 67108863 & r
            }
            return s
        }
        function s(e, t, n, i, s, o) {
            for (var r = 32767 & t, a = t >> 15; --o >= 0; ) {
                var c = 32767 & this[e]
                  , l = this[e++] >> 15
                  , d = a * c + l * r;
                c = r * c + ((32767 & d) << 15) + n[i] + (1073741823 & s),
                s = (c >>> 30) + (d >>> 15) + a * l + (s >>> 30),
                n[i++] = 1073741823 & c
            }
            return s
        }
        function o(e, t, n, i, s, o) {
            for (var r = 16383 & t, a = t >> 14; --o >= 0; ) {
                var c = 16383 & this[e]
                  , l = this[e++] >> 14
                  , d = a * c + l * r;
                c = r * c + ((16383 & d) << 14) + n[i] + s,
                s = (c >> 28) + (d >> 14) + a * l,
                n[i++] = 268435455 & c
            }
            return s
        }
        function r(e) {
            return kn.charAt(e)
        }
        function a(e, t) {
            var n = Ln[e.charCodeAt(t)];
            return null == n ? -1 : n
        }
        function c(e) {
            for (var t = this.t - 1; t >= 0; --t)
                e[t] = this[t];
            e.t = this.t,
            e.s = this.s
        }
        function l(e) {
            this.t = 1,
            this.s = 0 > e ? -1 : 0,
            e > 0 ? this[0] = e : -1 > e ? this[0] = e + DV : this.t = 0
        }
        function d(e) {
            var t = n();
            return t.fromInt(e),
            t
        }
        function u(e, n) {
            var i;
            if (16 == n)
                i = 4;
            else if (8 == n)
                i = 3;
            else if (256 == n)
                i = 8;
            else if (2 == n)
                i = 1;
            else if (32 == n)
                i = 5;
            else {
                if (4 != n)
                    return void this.fromRadix(e, n);
                i = 2
            }
            this.t = 0,
            this.s = 0;
            for (var s = e.length, o = !1, r = 0; --s >= 0; ) {
                var c = 8 == i ? 255 & e[s] : a(e, s);
                0 > c ? "-" == e.charAt(s) && (o = !0) : (o = !1,
                0 == r ? this[this.t++] = c : r + i > this.DB ? (this[this.t - 1] |= (c & (1 << this.DB - r) - 1) << r,
                this[this.t++] = c >> this.DB - r) : this[this.t - 1] |= c << r,
                r += i,
                r >= this.DB && (r -= this.DB))
            }
            8 == i && 0 != (128 & e[0]) && (this.s = -1,
            r > 0 && (this[this.t - 1] |= (1 << this.DB - r) - 1 << r)),
            this.clamp(),
            o && t.ZERO.subTo(this, this)
        }
        function p() {
            for (var e = this.s & this.DM; this.t > 0 && this[this.t - 1] == e; )
                --this.t
        }
        function g(e) {
            if (this.s < 0)
                return "-" + this.negate().toString(e);
            var t;
            if (16 == e)
                t = 4;
            else if (8 == e)
                t = 3;
            else if (2 == e)
                t = 1;
            else if (32 == e)
                t = 5;
            else {
                if (4 != e)
                    return this.toRadix(e);
                t = 2
            }
            var n, i = (1 << t) - 1, s = !1, o = "", a = this.t, c = this.DB - a * this.DB % t;
            if (a-- > 0)
                for (c < this.DB && (n = this[a] >> c) > 0 && (s = !0,
                o = r(n)); a >= 0; )
                    t > c ? (n = (this[a] & (1 << c) - 1) << t - c,
                    n |= this[--a] >> (c += this.DB - t)) : (n = this[a] >> (c -= t) & i,
                    0 >= c && (c += this.DB,
                    --a)),
                    n > 0 && (s = !0),
                    s && (o += r(n));
            return s ? o : "0"
        }
        function h() {
            var e = n();
            return t.ZERO.subTo(this, e),
            e
        }
        function f() {
            return this.s < 0 ? this.negate() : this
        }
        function m(e) {
            var t = this.s - e.s;
            if (0 != t)
                return t;
            var n = this.t;
            if (t = n - e.t,
            0 != t)
                return this.s < 0 ? -t : t;
            for (; --n >= 0; )
                if (0 != (t = this[n] - e[n]))
                    return t;
            return 0
        }
        function b(e) {
            var t, n = 1;
            return 0 != (t = e >>> 16) && (e = t,
            n += 16),
            0 != (t = e >> 8) && (e = t,
            n += 8),
            0 != (t = e >> 4) && (e = t,
            n += 4),
            0 != (t = e >> 2) && (e = t,
            n += 2),
            0 != (t = e >> 1) && (e = t,
            n += 1),
            n
        }
        function y() {
            return this.t <= 0 ? 0 : this.DB * (this.t - 1) + b(this[this.t - 1] ^ this.s & this.DM)
        }
        function _(e, t) {
            var n;
            for (n = this.t - 1; n >= 0; --n)
                t[n + e] = this[n];
            for (n = e - 1; n >= 0; --n)
                t[n] = 0;
            t.t = this.t + e,
            t.s = this.s
        }
        function E(e, t) {
            for (var n = e; n < this.t; ++n)
                t[n - e] = this[n];
            t.t = Math.max(this.t - e, 0),
            t.s = this.s
        }
        function C(e, t) {
            var n, i = e % this.DB, s = this.DB - i, o = (1 << s) - 1, r = Math.floor(e / this.DB), a = this.s << i & this.DM;
            for (n = this.t - 1; n >= 0; --n)
                t[n + r + 1] = this[n] >> s | a,
                a = (this[n] & o) << i;
            for (n = r - 1; n >= 0; --n)
                t[n] = 0;
            t[r] = a,
            t.t = this.t + r + 1,
            t.s = this.s,
            t.clamp()
        }
        function w(e, t) {
            t.s = this.s;
            var n = Math.floor(e / this.DB);
            if (n >= this.t)
                return void (t.t = 0);
            var i = e % this.DB
              , s = this.DB - i
              , o = (1 << i) - 1;
            t[0] = this[n] >> i;
            for (var r = n + 1; r < this.t; ++r)
                t[r - n - 1] |= (this[r] & o) << s,
                t[r - n] = this[r] >> i;
            i > 0 && (t[this.t - n - 1] |= (this.s & o) << s),
            t.t = this.t - n,
            t.clamp()
        }
        function I(e, t) {
            for (var n = 0, i = 0, s = Math.min(e.t, this.t); s > n; )
                i += this[n] - e[n],
                t[n++] = i & this.DM,
                i >>= this.DB;
            if (e.t < this.t) {
                for (i -= e.s; n < this.t; )
                    i += this[n],
                    t[n++] = i & this.DM,
                    i >>= this.DB;
                i += this.s
            } else {
                for (i += this.s; n < e.t; )
                    i -= e[n],
                    t[n++] = i & this.DM,
                    i >>= this.DB;
                i -= e.s
            }
            t.s = 0 > i ? -1 : 0,
            -1 > i ? t[n++] = this.DV + i : i > 0 && (t[n++] = i),
            t.t = n,
            t.clamp()
        }
        function S(e, n) {
            var i = this.abs()
              , s = e.abs()
              , o = i.t;
            for (n.t = o + s.t; --o >= 0; )
                n[o] = 0;
            for (o = 0; o < s.t; ++o)
                n[o + i.t] = i.am(0, s[o], n, o, 0, i.t);
            n.s = 0,
            n.clamp(),
            this.s != e.s && t.ZERO.subTo(n, n)
        }
        function T(e) {
            for (var t = this.abs(), n = e.t = 2 * t.t; --n >= 0; )
                e[n] = 0;
            for (n = 0; n < t.t - 1; ++n) {
                var i = t.am(n, t[n], e, 2 * n, 0, 1);
                (e[n + t.t] += t.am(n + 1, 2 * t[n], e, 2 * n + 1, i, t.t - n - 1)) >= t.DV && (e[n + t.t] -= t.DV,
                e[n + t.t + 1] = 1)
            }
            e.t > 0 && (e[e.t - 1] += t.am(n, t[n], e, 2 * n, 0, 1)),
            e.s = 0,
            e.clamp()
        }
        function D(e, i, s) {
            var o = e.abs();
            if (!(o.t <= 0)) {
                var r = this.abs();
                if (r.t < o.t)
                    return null != i && i.fromInt(0),
                    void (null != s && this.copyTo(s));
                null == s && (s = n());
                var a = n()
                  , c = this.s
                  , l = e.s
                  , d = this.DB - b(o[o.t - 1]);
                d > 0 ? (o.lShiftTo(d, a),
                r.lShiftTo(d, s)) : (o.copyTo(a),
                r.copyTo(s));
                var u = a.t
                  , p = a[u - 1];
                if (0 != p) {
                    var g = p * (1 << this.F1) + (u > 1 ? a[u - 2] >> this.F2 : 0)
                      , h = this.FV / g
                      , f = (1 << this.F1) / g
                      , m = 1 << this.F2
                      , v = s.t
                      , y = v - u
                      , _ = null == i ? n() : i;
                    for (a.dlShiftTo(y, _),
                    s.compareTo(_) >= 0 && (s[s.t++] = 1,
                    s.subTo(_, s)),
                    t.ONE.dlShiftTo(u, _),
                    _.subTo(a, a); a.t < u; )
                        a[a.t++] = 0;
                    for (; --y >= 0; ) {
                        var E = s[--v] == p ? this.DM : Math.floor(s[v] * h + (s[v - 1] + m) * f);
                        if ((s[v] += a.am(0, E, s, y, 0, u)) < E)
                            for (a.dlShiftTo(y, _),
                            s.subTo(_, s); s[v] < --E; )
                                s.subTo(_, s)
                    }
                    null != i && (s.drShiftTo(u, i),
                    c != l && t.ZERO.subTo(i, i)),
                    s.t = u,
                    s.clamp(),
                    d > 0 && s.rShiftTo(d, s),
                    0 > c && t.ZERO.subTo(s, s)
                }
            }
        }
        function R(e) {
            var i = n();
            return this.abs().divRemTo(e, null, i),
            this.s < 0 && i.compareTo(t.ZERO) > 0 && e.subTo(i, i),
            i
        }
        function x(e) {
            this.m = e
        }
        function k(e) {
            return e.s < 0 || e.compareTo(this.m) >= 0 ? e.mod(this.m) : e
        }
        function L(e) {
            return e
        }
        function P(e) {
            e.divRemTo(this.m, null, e)
        }
        function A(e, t, n) {
            e.multiplyTo(t, n),
            this.reduce(n)
        }
        function B(e, t) {
            e.squareTo(t),
            this.reduce(t)
        }
        function M() {
            if (this.t < 1)
                return 0;
            var e = this[0];
            if (0 == (1 & e))
                return 0;
            var t = 3 & e;
            return t = t * (2 - (15 & e) * t) & 15,
            t = t * (2 - (255 & e) * t) & 255,
            t = t * (2 - ((65535 & e) * t & 65535)) & 65535,
            t = t * (2 - e * t % this.DV) % this.DV,
            t > 0 ? this.DV - t : -t
        }
        function V(e) {
            this.m = e,
            this.mp = e.invDigit(),
            this.mpl = 32767 & this.mp,
            this.mph = this.mp >> 15,
            this.um = (1 << e.DB - 15) - 1,
            this.mt2 = 2 * e.t
        }
        function $(e) {
            var i = n();
            return e.abs().dlShiftTo(this.m.t, i),
            i.divRemTo(this.m, null, i),
            e.s < 0 && i.compareTo(t.ZERO) > 0 && this.m.subTo(i, i),
            i
        }
        function O(e) {
            var t = n();
            return e.copyTo(t),
            this.reduce(t),
            t
        }
        function N(e) {
            for (; e.t <= this.mt2; )
                e[e.t++] = 0;
            for (var t = 0; t < this.m.t; ++t) {
                var n = 32767 & e[t]
                  , i = n * this.mpl + ((n * this.mph + (e[t] >> 15) * this.mpl & this.um) << 15) & e.DM;
                for (n = t + this.m.t,
                e[n] += this.m.am(0, i, e, t, 0, this.m.t); e[n] >= e.DV; )
                    e[n] -= e.DV,
                    e[++n]++
            }
            e.clamp(),
            e.drShiftTo(this.m.t, e),
            e.compareTo(this.m) >= 0 && e.subTo(this.m, e)
        }
        function U(e, t) {
            e.squareTo(t),
            this.reduce(t)
        }
        function q(e, t, n) {
            e.multiplyTo(t, n),
            this.reduce(n)
        }
        function F() {
            return 0 == (this.t > 0 ? 1 & this[0] : this.s)
        }
        function W(e, i) {
            if (e > 4294967295 || 1 > e)
                return t.ONE;
            var s = n()
              , o = n()
              , r = i.convert(this)
              , a = b(e) - 1;
            for (r.copyTo(s); --a >= 0; )
                if (i.sqrTo(s, o),
                (e & 1 << a) > 0)
                    i.mulTo(o, r, s);
                else {
                    var c = s;
                    s = o,
                    o = c
                }
            return i.revert(s)
        }
        function H(e, t) {
            var n;
            return n = 256 > e || t.isEven() ? new x(t) : new V(t),
            this.exp(e, n)
        }
        function K() {
            var e = n();
            return this.copyTo(e),
            e
        }
        function j() {
            if (this.s < 0) {
                if (1 == this.t)
                    return this[0] - this.DV;
                if (0 == this.t)
                    return -1
            } else {
                if (1 == this.t)
                    return this[0];
                if (0 == this.t)
                    return 0
            }
            return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
        }
        function J() {
            return 0 == this.t ? this.s : this[0] << 24 >> 24
        }
        function G() {
            return 0 == this.t ? this.s : this[0] << 16 >> 16
        }
        function Q(e) {
            return Math.floor(Math.LN2 * this.DB / Math.log(e))
        }
        function z() {
            return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
        }
        function Z(e) {
            if (null == e && (e = 10),
            0 == this.signum() || 2 > e || e > 36)
                return "0";
            var t = this.chunkSize(e)
              , i = Math.pow(e, t)
              , s = d(i)
              , o = n()
              , r = n()
              , a = "";
            for (this.divRemTo(s, o, r); o.signum() > 0; )
                a = (i + r.intValue()).toString(e).substr(1) + a,
                o.divRemTo(s, o, r);
            return r.intValue().toString(e) + a
        }
        function Y(e, n) {
            this.fromInt(0),
            null == n && (n = 10);
            for (var i = this.chunkSize(n), s = Math.pow(n, i), o = !1, r = 0, c = 0, l = 0; l < e.length; ++l) {
                var d = a(e, l);
                0 > d ? "-" == e.charAt(l) && 0 == this.signum() && (o = !0) : (c = n * c + d,
                ++r >= i && (this.dMultiply(s),
                this.dAddOffset(c, 0),
                r = 0,
                c = 0))
            }
            r > 0 && (this.dMultiply(Math.pow(n, r)),
            this.dAddOffset(c, 0)),
            o && t.ZERO.subTo(this, this)
        }
        function X(e, n, i) {
            if ("number" == typeof n)
                if (2 > e)
                    this.fromInt(1);
                else
                    for (this.fromNumber(e, i),
                    this.testBit(e - 1) || this.bitwiseTo(t.ONE.shiftLeft(e - 1), at, this),
                    this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(n); )
                        this.dAddOffset(2, 0),
                        this.bitLength() > e && this.subTo(t.ONE.shiftLeft(e - 1), this);
            else {
                var s = new Array
                  , o = 7 & e;
                s.length = (e >> 3) + 1,
                n.nextBytes(s),
                o > 0 ? s[0] &= (1 << o) - 1 : s[0] = 0,
                this.fromString(s, 256)
            }
        }
        function et() {
            var e = this.t
              , t = new Array;
            t[0] = this.s;
            var n, i = this.DB - e * this.DB % 8, s = 0;
            if (e-- > 0)
                for (i < this.DB && (n = this[e] >> i) != (this.s & this.DM) >> i && (t[s++] = n | this.s << this.DB - i); e >= 0; )
                    8 > i ? (n = (this[e] & (1 << i) - 1) << 8 - i,
                    n |= this[--e] >> (i += this.DB - 8)) : (n = this[e] >> (i -= 8) & 255,
                    0 >= i && (i += this.DB,
                    --e)),
                    0 != (128 & n) && (n |= -256),
                    0 == s && (128 & this.s) != (128 & n) && ++s,
                    (s > 0 || n != this.s) && (t[s++] = n);
            return t
        }
        function tt(e) {
            return 0 == this.compareTo(e)
        }
        function nt(e) {
            return this.compareTo(e) < 0 ? this : e
        }
        function it(e) {
            return this.compareTo(e) > 0 ? this : e
        }
        function st(e, t, n) {
            var i, s, o = Math.min(e.t, this.t);
            for (i = 0; o > i; ++i)
                n[i] = t(this[i], e[i]);
            if (e.t < this.t) {
                for (s = e.s & this.DM,
                i = o; i < this.t; ++i)
                    n[i] = t(this[i], s);
                n.t = this.t
            } else {
                for (s = this.s & this.DM,
                i = o; i < e.t; ++i)
                    n[i] = t(s, e[i]);
                n.t = e.t
            }
            n.s = t(this.s, e.s),
            n.clamp()
        }
        function ot(e, t) {
            return e & t
        }
        function rt(e) {
            var t = n();
            return this.bitwiseTo(e, ot, t),
            t
        }
        function at(e, t) {
            return e | t
        }
        function ct(e) {
            var t = n();
            return this.bitwiseTo(e, at, t),
            t
        }
        function lt(e, t) {
            return e ^ t
        }
        function dt(e) {
            var t = n();
            return this.bitwiseTo(e, lt, t),
            t
        }
        function ut(e, t) {
            return e & ~t
        }
        function pt(e) {
            var t = n();
            return this.bitwiseTo(e, ut, t),
            t
        }
        function gt() {
            for (var e = n(), t = 0; t < this.t; ++t)
                e[t] = this.DM & ~this[t];
            return e.t = this.t,
            e.s = ~this.s,
            e
        }
        function ht(e) {
            var t = n();
            return 0 > e ? this.rShiftTo(-e, t) : this.lShiftTo(e, t),
            t
        }
        function ft(e) {
            var t = n();
            return 0 > e ? this.lShiftTo(-e, t) : this.rShiftTo(e, t),
            t
        }
        function mt(e) {
            if (0 == e)
                return -1;
            var t = 0;
            return 0 == (65535 & e) && (e >>= 16,
            t += 16),
            0 == (255 & e) && (e >>= 8,
            t += 8),
            0 == (15 & e) && (e >>= 4,
            t += 4),
            0 == (3 & e) && (e >>= 2,
            t += 2),
            0 == (1 & e) && ++t,
            t
        }
        function vt() {
            for (var e = 0; e < this.t; ++e)
                if (0 != this[e])
                    return e * this.DB + mt(this[e]);
            return this.s < 0 ? this.t * this.DB : -1
        }
        function bt(e) {
            for (var t = 0; 0 != e; )
                e &= e - 1,
                ++t;
            return t
        }
        function yt() {
            for (var e = 0, t = this.s & this.DM, n = 0; n < this.t; ++n)
                e += bt(this[n] ^ t);
            return e
        }
        function _t(e) {
            var t = Math.floor(e / this.DB);
            return t >= this.t ? 0 != this.s : 0 != (this[t] & 1 << e % this.DB)
        }
        function Et(e, n) {
            var i = t.ONE.shiftLeft(e);
            return this.bitwiseTo(i, n, i),
            i
        }
        function Ct(e) {
            return this.changeBit(e, at)
        }
        function wt(e) {
            return this.changeBit(e, ut)
        }
        function It(e) {
            return this.changeBit(e, lt)
        }
        function St(e, t) {
            for (var n = 0, i = 0, s = Math.min(e.t, this.t); s > n; )
                i += this[n] + e[n],
                t[n++] = i & this.DM,
                i >>= this.DB;
            if (e.t < this.t) {
                for (i += e.s; n < this.t; )
                    i += this[n],
                    t[n++] = i & this.DM,
                    i >>= this.DB;
                i += this.s
            } else {
                for (i += this.s; n < e.t; )
                    i += e[n],
                    t[n++] = i & this.DM,
                    i >>= this.DB;
                i += e.s
            }
            t.s = 0 > i ? -1 : 0,
            i > 0 ? t[n++] = i : -1 > i && (t[n++] = this.DV + i),
            t.t = n,
            t.clamp()
        }
        function Tt(e) {
            var t = n();
            return this.addTo(e, t),
            t
        }
        function Dt(e) {
            var t = n();
            return this.subTo(e, t),
            t
        }
        function Rt(e) {
            var t = n();
            return this.multiplyTo(e, t),
            t
        }
        function xt() {
            var e = n();
            return this.squareTo(e),
            e
        }
        function kt(e) {
            var t = n();
            return this.divRemTo(e, t, null),
            t
        }
        function Lt(e) {
            var t = n();
            return this.divRemTo(e, null, t),
            t
        }
        function Pt(e) {
            var t = n()
              , i = n();
            return this.divRemTo(e, t, i),
            new Array(t,i)
        }
        function At(e) {
            this[this.t] = this.am(0, e - 1, this, 0, 0, this.t),
            ++this.t,
            this.clamp()
        }
        function Bt(e, t) {
            if (0 != e) {
                for (; this.t <= t; )
                    this[this.t++] = 0;
                for (this[t] += e; this[t] >= this.DV; )
                    this[t] -= this.DV,
                    ++t >= this.t && (this[this.t++] = 0),
                    ++this[t]
            }
        }
        function Mt() {}
        function Vt(e) {
            return e
        }
        function $t(e, t, n) {
            e.multiplyTo(t, n)
        }
        function Ot(e, t) {
            e.squareTo(t)
        }
        function Nt(e) {
            return this.exp(e, new Mt)
        }
        function Ut(e, t, n) {
            var i = Math.min(this.t + e.t, t);
            for (n.s = 0,
            n.t = i; i > 0; )
                n[--i] = 0;
            var s;
            for (s = n.t - this.t; s > i; ++i)
                n[i + this.t] = this.am(0, e[i], n, i, 0, this.t);
            for (s = Math.min(e.t, t); s > i; ++i)
                this.am(0, e[i], n, i, 0, t - i);
            n.clamp()
        }
        function qt(e, t, n) {
            --t;
            var i = n.t = this.t + e.t - t;
            for (n.s = 0; --i >= 0; )
                n[i] = 0;
            for (i = Math.max(t - this.t, 0); i < e.t; ++i)
                n[this.t + i - t] = this.am(t - i, e[i], n, 0, 0, this.t + i - t);
            n.clamp(),
            n.drShiftTo(1, n)
        }
        function Ft(e) {
            this.r2 = n(),
            this.q3 = n(),
            t.ONE.dlShiftTo(2 * e.t, this.r2),
            this.mu = this.r2.divide(e),
            this.m = e
        }
        function Wt(e) {
            if (e.s < 0 || e.t > 2 * this.m.t)
                return e.mod(this.m);
            if (e.compareTo(this.m) < 0)
                return e;
            var t = n();
            return e.copyTo(t),
            this.reduce(t),
            t
        }
        function Ht(e) {
            return e
        }
        function Kt(e) {
            for (e.drShiftTo(this.m.t - 1, this.r2),
            e.t > this.m.t + 1 && (e.t = this.m.t + 1,
            e.clamp()),
            this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
            this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); e.compareTo(this.r2) < 0; )
                e.dAddOffset(1, this.m.t + 1);
            for (e.subTo(this.r2, e); e.compareTo(this.m) >= 0; )
                e.subTo(this.m, e)
        }
        function jt(e, t) {
            e.squareTo(t),
            this.reduce(t)
        }
        function Jt(e, t, n) {
            e.multiplyTo(t, n),
            this.reduce(n)
        }
        function Gt(e, t) {
            var i, s, o = e.bitLength(), r = d(1);
            if (0 >= o)
                return r;
            i = 18 > o ? 1 : 48 > o ? 3 : 144 > o ? 4 : 768 > o ? 5 : 6,
            s = 8 > o ? new x(t) : t.isEven() ? new Ft(t) : new V(t);
            var a = new Array
              , c = 3
              , l = i - 1
              , u = (1 << i) - 1;
            if (a[1] = s.convert(this),
            i > 1) {
                var p = n();
                for (s.sqrTo(a[1], p); u >= c; )
                    a[c] = n(),
                    s.mulTo(p, a[c - 2], a[c]),
                    c += 2
            }
            var g, h, f = e.t - 1, m = !0, v = n();
            for (o = b(e[f]) - 1; f >= 0; ) {
                for (o >= l ? g = e[f] >> o - l & u : (g = (e[f] & (1 << o + 1) - 1) << l - o,
                f > 0 && (g |= e[f - 1] >> this.DB + o - l)),
                c = i; 0 == (1 & g); )
                    g >>= 1,
                    --c;
                if ((o -= c) < 0 && (o += this.DB,
                --f),
                m)
                    a[g].copyTo(r),
                    m = !1;
                else {
                    for (; c > 1; )
                        s.sqrTo(r, v),
                        s.sqrTo(v, r),
                        c -= 2;
                    c > 0 ? s.sqrTo(r, v) : (h = r,
                    r = v,
                    v = h),
                    s.mulTo(v, a[g], r)
                }
                for (; f >= 0 && 0 == (e[f] & 1 << o); )
                    s.sqrTo(r, v),
                    h = r,
                    r = v,
                    v = h,
                    --o < 0 && (o = this.DB - 1,
                    --f)
            }
            return s.revert(r)
        }
        function Qt(e) {
            var t = this.s < 0 ? this.negate() : this.clone()
              , n = e.s < 0 ? e.negate() : e.clone();
            if (t.compareTo(n) < 0) {
                var i = t;
                t = n,
                n = i
            }
            var s = t.getLowestSetBit()
              , o = n.getLowestSetBit();
            if (0 > o)
                return t;
            for (o > s && (o = s),
            o > 0 && (t.rShiftTo(o, t),
            n.rShiftTo(o, n)); t.signum() > 0; )
                (s = t.getLowestSetBit()) > 0 && t.rShiftTo(s, t),
                (s = n.getLowestSetBit()) > 0 && n.rShiftTo(s, n),
                t.compareTo(n) >= 0 ? (t.subTo(n, t),
                t.rShiftTo(1, t)) : (n.subTo(t, n),
                n.rShiftTo(1, n));
            return o > 0 && n.lShiftTo(o, n),
            n
        }
        function zt(e) {
            if (0 >= e)
                return 0;
            var t = this.DV % e
              , n = this.s < 0 ? e - 1 : 0;
            if (this.t > 0)
                if (0 == t)
                    n = this[0] % e;
                else
                    for (var i = this.t - 1; i >= 0; --i)
                        n = (t * n + this[i]) % e;
            return n
        }
        function Zt(e) {
            var n = e.isEven();
            if (this.isEven() && n || 0 == e.signum())
                return t.ZERO;
            for (var i = e.clone(), s = this.clone(), o = d(1), r = d(0), a = d(0), c = d(1); 0 != i.signum(); ) {
                for (; i.isEven(); )
                    i.rShiftTo(1, i),
                    n ? (o.isEven() && r.isEven() || (o.addTo(this, o),
                    r.subTo(e, r)),
                    o.rShiftTo(1, o)) : r.isEven() || r.subTo(e, r),
                    r.rShiftTo(1, r);
                for (; s.isEven(); )
                    s.rShiftTo(1, s),
                    n ? (a.isEven() && c.isEven() || (a.addTo(this, a),
                    c.subTo(e, c)),
                    a.rShiftTo(1, a)) : c.isEven() || c.subTo(e, c),
                    c.rShiftTo(1, c);
                i.compareTo(s) >= 0 ? (i.subTo(s, i),
                n && o.subTo(a, o),
                r.subTo(c, r)) : (s.subTo(i, s),
                n && a.subTo(o, a),
                c.subTo(r, c))
            }
            return 0 != s.compareTo(t.ONE) ? t.ZERO : c.compareTo(e) >= 0 ? c.subtract(e) : c.signum() < 0 ? (c.addTo(e, c),
            c.signum() < 0 ? c.add(e) : c) : c
        }
        function Yt(e) {
            var t, n = this.abs();
            if (1 == n.t && n[0] <= Pn[Pn.length - 1]) {
                for (t = 0; t < Pn.length; ++t)
                    if (n[0] == Pn[t])
                        return !0;
                return !1
            }
            if (n.isEven())
                return !1;
            for (t = 1; t < Pn.length; ) {
                for (var i = Pn[t], s = t + 1; s < Pn.length && An > i; )
                    i *= Pn[s++];
                for (i = n.modInt(i); s > t; )
                    if (i % Pn[t++] == 0)
                        return !1
            }
            return n.millerRabin(e)
        }
        function Xt(e) {
            var i = this.subtract(t.ONE)
              , s = i.getLowestSetBit();
            if (0 >= s)
                return !1;
            var o = i.shiftRight(s);
            e = e + 1 >> 1,
            e > Pn.length && (e = Pn.length);
            for (var r = n(), a = 0; e > a; ++a) {
                r.fromInt(Pn[Math.floor(Math.random() * Pn.length)]);
                var c = r.modPow(o, this);
                if (0 != c.compareTo(t.ONE) && 0 != c.compareTo(i)) {
                    for (var l = 1; l++ < s && 0 != c.compareTo(i); )
                        if (c = c.modPowInt(2, this),
                        0 == c.compareTo(t.ONE))
                            return !1;
                    if (0 != c.compareTo(i))
                        return !1
                }
            }
            return !0
        }
        function en() {
            this.i = 0,
            this.j = 0,
            this.S = new Array
        }
        function tn(e) {
            var t, n, i;
            for (t = 0; 256 > t; ++t)
                this.S[t] = t;
            for (n = 0,
            t = 0; 256 > t; ++t)
                n = n + this.S[t] + e[t % e.length] & 255,
                i = this.S[t],
                this.S[t] = this.S[n],
                this.S[n] = i;
            this.i = 0,
            this.j = 0
        }
        function nn() {
            var e;
            return this.i = this.i + 1 & 255,
            this.j = this.j + this.S[this.i] & 255,
            e = this.S[this.i],
            this.S[this.i] = this.S[this.j],
            this.S[this.j] = e,
            this.S[e + this.S[this.i] & 255]
        }
        function sn() {
            return new en
        }
        function on(e) {
            Mn[Vn++] ^= 255 & e,
            Mn[Vn++] ^= e >> 8 & 255,
            Mn[Vn++] ^= e >> 16 & 255,
            Mn[Vn++] ^= e >> 24 & 255,
            Vn >= $n && (Vn -= $n)
        }
        function rn() {
            on((new Date).getTime())
        }
        function an() {
            if (null == Bn) {
                for (rn(),
                Bn = sn(),
                Bn.init(Mn),
                Vn = 0; Vn < Mn.length; ++Vn)
                    Mn[Vn] = 0;
                Vn = 0
            }
            return Bn.next()
        }
        function cn(e) {
            var t;
            for (t = 0; t < e.length; ++t)
                e[t] = an()
        }
        function ln() {}
        function dn(e, n) {
            return new t(e,n)
        }
        function un(e, n) {
            if (n < e.length + 11)
                return console.error("Message too long for RSA"),
                null;
            for (var i = new Array, s = e.length - 1; s >= 0 && n > 0; ) {
                var o = e.charCodeAt(s--);
                128 > o ? i[--n] = o : o > 127 && 2048 > o ? (i[--n] = 63 & o | 128,
                i[--n] = o >> 6 | 192) : (i[--n] = 63 & o | 128,
                i[--n] = o >> 6 & 63 | 128,
                i[--n] = o >> 12 | 224)
            }
            i[--n] = 0;
            for (var r = new ln, a = new Array; n > 2; ) {
                for (a[0] = 0; 0 == a[0]; )
                    r.nextBytes(a);
                i[--n] = a[0]
            }
            return i[--n] = 2,
            i[--n] = 0,
            new t(i)
        }
        function pn() {
            this.n = null,
            this.e = 0,
            this.d = null,
            this.p = null,
            this.q = null,
            this.dmp1 = null,
            this.dmq1 = null,
            this.coeff = null
        }
        function gn(e, t) {
            null != e && null != t && e.length > 0 && t.length > 0 ? (this.n = dn(e, 16),
            this.e = parseInt(t, 16)) : console.error("Invalid RSA public key")
        }
        function hn(e) {
            return e.modPowInt(this.e, this.n)
        }
        function fn(e) {
            var t = un(e, this.n.bitLength() + 7 >> 3);
            if (null == t)
                return null;
            var n = this.doPublic(t);
            if (null == n)
                return null;
            var i = n.toString(16);
            return 0 == (1 & i.length) ? i : "0" + i
        }
        function mn(e, t) {
            for (var n = e.toByteArray(), i = 0; i < n.length && 0 == n[i]; )
                ++i;
            if (n.length - i != t - 1 || 2 != n[i])
                return null;
            for (++i; 0 != n[i]; )
                if (++i >= n.length)
                    return null;
            for (var s = ""; ++i < n.length; ) {
                var o = 255 & n[i];
                128 > o ? s += String.fromCharCode(o) : o > 191 && 224 > o ? (s += String.fromCharCode((31 & o) << 6 | 63 & n[i + 1]),
                ++i) : (s += String.fromCharCode((15 & o) << 12 | (63 & n[i + 1]) << 6 | 63 & n[i + 2]),
                i += 2)
            }
            return s
        }
        function vn(e, t, n) {
            null != e && null != t && e.length > 0 && t.length > 0 ? (this.n = dn(e, 16),
            this.e = parseInt(t, 16),
            this.d = dn(n, 16)) : console.error("Invalid RSA private key")
        }
        function bn(e, t, n, i, s, o, r, a) {
            null != e && null != t && e.length > 0 && t.length > 0 ? (this.n = dn(e, 16),
            this.e = parseInt(t, 16),
            this.d = dn(n, 16),
            this.p = dn(i, 16),
            this.q = dn(s, 16),
            this.dmp1 = dn(o, 16),
            this.dmq1 = dn(r, 16),
            this.coeff = dn(a, 16)) : console.error("Invalid RSA private key")
        }
        function yn(e, n) {
            var i = new ln
              , s = e >> 1;
            this.e = parseInt(n, 16);
            for (var o = new t(n,16); ; ) {
                for (; this.p = new t(e - s,1,i),
                0 != this.p.subtract(t.ONE).gcd(o).compareTo(t.ONE) || !this.p.isProbablePrime(10); )
                    ;
                for (; this.q = new t(s,1,i),
                0 != this.q.subtract(t.ONE).gcd(o).compareTo(t.ONE) || !this.q.isProbablePrime(10); )
                    ;
                if (this.p.compareTo(this.q) <= 0) {
                    var r = this.p;
                    this.p = this.q,
                    this.q = r
                }
                var a = this.p.subtract(t.ONE)
                  , c = this.q.subtract(t.ONE)
                  , l = a.multiply(c);
                if (0 == l.gcd(o).compareTo(t.ONE)) {
                    this.n = this.p.multiply(this.q),
                    this.d = o.modInverse(l),
                    this.dmp1 = this.d.mod(a),
                    this.dmq1 = this.d.mod(c),
                    this.coeff = this.q.modInverse(this.p);
                    break
                }
            }
        }
        function _n(e) {
            if (null == this.p || null == this.q)
                return e.modPow(this.d, this.n);
            for (var t = e.mod(this.p).modPow(this.dmp1, this.p), n = e.mod(this.q).modPow(this.dmq1, this.q); t.compareTo(n) < 0; )
                t = t.add(this.p);
            return t.subtract(n).multiply(this.coeff).mod(this.p).multiply(this.q).add(n)
        }
        function En(e) {
            var t = dn(e, 16)
              , n = this.doPrivate(t);
            return null == n ? null : mn(n, this.n.bitLength() + 7 >> 3)
        }
        function Cn(e) {
            var t, n, i = "";
            for (t = 0; t + 3 <= e.length; t += 3)
                n = parseInt(e.substring(t, t + 3), 16),
                i += Un.charAt(n >> 6) + Un.charAt(63 & n);
            for (t + 1 == e.length ? (n = parseInt(e.substring(t, t + 1), 16),
            i += Un.charAt(n << 2)) : t + 2 == e.length && (n = parseInt(e.substring(t, t + 2), 16),
            i += Un.charAt(n >> 2) + Un.charAt((3 & n) << 4)); (3 & i.length) > 0; )
                i += qn;
            return i
        }
        function wn(e) {
            var t, n, i = "", s = 0;
            for (t = 0; t < e.length && e.charAt(t) != qn; ++t)
                v = Un.indexOf(e.charAt(t)),
                0 > v || (0 == s ? (i += r(v >> 2),
                n = 3 & v,
                s = 1) : 1 == s ? (i += r(n << 2 | v >> 4),
                n = 15 & v,
                s = 2) : 2 == s ? (i += r(n),
                i += r(v >> 2),
                n = 3 & v,
                s = 3) : (i += r(n << 2 | v >> 4),
                i += r(15 & v),
                s = 0));
            return 1 == s && (i += r(n << 2)),
            i
        }
        var In, Sn = 0xdeadbeefcafe, Tn = 15715070 == (16777215 & Sn);
        Tn && "Microsoft Internet Explorer" == navigator.appName ? (t.prototype.am = s,
        In = 30) : Tn && "Netscape" != navigator.appName ? (t.prototype.am = i,
        In = 26) : (t.prototype.am = o,
        In = 28),
        t.prototype.DB = In,
        t.prototype.DM = (1 << In) - 1,
        t.prototype.DV = 1 << In;
        var Dn = 52;
        t.prototype.FV = Math.pow(2, Dn),
        t.prototype.F1 = Dn - In,
        t.prototype.F2 = 2 * In - Dn;
        var Rn, xn, kn = "0123456789abcdefghijklmnopqrstuvwxyz", Ln = new Array;
        for (Rn = "0".charCodeAt(0),
        xn = 0; 9 >= xn; ++xn)
            Ln[Rn++] = xn;
        for (Rn = "a".charCodeAt(0),
        xn = 10; 36 > xn; ++xn)
            Ln[Rn++] = xn;
        for (Rn = "A".charCodeAt(0),
        xn = 10; 36 > xn; ++xn)
            Ln[Rn++] = xn;
        x.prototype.convert = k,
        x.prototype.revert = L,
        x.prototype.reduce = P,
        x.prototype.mulTo = A,
        x.prototype.sqrTo = B,
        V.prototype.convert = $,
        V.prototype.revert = O,
        V.prototype.reduce = N,
        V.prototype.mulTo = q,
        V.prototype.sqrTo = U,
        t.prototype.copyTo = c,
        t.prototype.fromInt = l,
        t.prototype.fromString = u,
        t.prototype.clamp = p,
        t.prototype.dlShiftTo = _,
        t.prototype.drShiftTo = E,
        t.prototype.lShiftTo = C,
        t.prototype.rShiftTo = w,
        t.prototype.subTo = I,
        t.prototype.multiplyTo = S,
        t.prototype.squareTo = T,
        t.prototype.divRemTo = D,
        t.prototype.invDigit = M,
        t.prototype.isEven = F,
        t.prototype.exp = W,
        t.prototype.toString = g,
        t.prototype.negate = h,
        t.prototype.abs = f,
        t.prototype.compareTo = m,
        t.prototype.bitLength = y,
        t.prototype.mod = R,
        t.prototype.modPowInt = H,
        t.ZERO = d(0),
        t.ONE = d(1),
        Mt.prototype.convert = Vt,
        Mt.prototype.revert = Vt,
        Mt.prototype.mulTo = $t,
        Mt.prototype.sqrTo = Ot,
        Ft.prototype.convert = Wt,
        Ft.prototype.revert = Ht,
        Ft.prototype.reduce = Kt,
        Ft.prototype.mulTo = Jt,
        Ft.prototype.sqrTo = jt;
        var Pn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
          , An = (1 << 26) / Pn[Pn.length - 1];
        t.prototype.chunkSize = Q,
        t.prototype.toRadix = Z,
        t.prototype.fromRadix = Y,
        t.prototype.fromNumber = X,
        t.prototype.bitwiseTo = st,
        t.prototype.changeBit = Et,
        t.prototype.addTo = St,
        t.prototype.dMultiply = At,
        t.prototype.dAddOffset = Bt,
        t.prototype.multiplyLowerTo = Ut,
        t.prototype.multiplyUpperTo = qt,
        t.prototype.modInt = zt,
        t.prototype.millerRabin = Xt,
        t.prototype.clone = K,
        t.prototype.intValue = j,
        t.prototype.byteValue = J,
        t.prototype.shortValue = G,
        t.prototype.signum = z,
        t.prototype.toByteArray = et,
        t.prototype.equals = tt,
        t.prototype.min = nt,
        t.prototype.max = it,
        t.prototype.and = rt,
        t.prototype.or = ct,
        t.prototype.xor = dt,
        t.prototype.andNot = pt,
        t.prototype.not = gt,
        t.prototype.shiftLeft = ht,
        t.prototype.shiftRight = ft,
        t.prototype.getLowestSetBit = vt,
        t.prototype.bitCount = yt,
        t.prototype.testBit = _t,
        t.prototype.setBit = Ct,
        t.prototype.clearBit = wt,
        t.prototype.flipBit = It,
        t.prototype.add = Tt,
        t.prototype.subtract = Dt,
        t.prototype.multiply = Rt,
        t.prototype.divide = kt,
        t.prototype.remainder = Lt,
        t.prototype.divideAndRemainder = Pt,
        t.prototype.modPow = Gt,
        t.prototype.modInverse = Zt,
        t.prototype.pow = Nt,
        t.prototype.gcd = Qt,
        t.prototype.isProbablePrime = Yt,
        t.prototype.square = xt,
        en.prototype.init = tn,
        en.prototype.next = nn;
        var Bn, Mn, Vn, $n = 256;
        if (null == Mn) {
            Mn = new Array,
            Vn = 0;
            var On;
            if ("Netscape" == navigator.appName && navigator.appVersion < "5" && window.crypto) {
                var Nn = window.crypto.random(32);
                for (On = 0; On < Nn.length; ++On)
                    Mn[Vn++] = 255 & Nn.charCodeAt(On)
            }
            for (; $n > Vn; )
                On = Math.floor(65536 * Math.random()),
                Mn[Vn++] = On >>> 8,
                Mn[Vn++] = 255 & On;
            Vn = 0,
            rn()
        }
        ln.prototype.nextBytes = cn,
        pn.prototype.doPublic = hn,
        pn.prototype.setPublic = gn,
        pn.prototype.encrypt = fn,
        pn.prototype.doPrivate = _n,
        pn.prototype.setPrivate = vn,
        pn.prototype.setPrivateEx = bn,
        pn.prototype.generate = yn,
        pn.prototype.decrypt = En,
        function() {
            var e = function(e, i, s) {
                var o = new ln
                  , r = e >> 1;
                this.e = parseInt(i, 16);
                var a = new t(i,16)
                  , c = this
                  , l = function() {
                    var i = function() {
                        if (c.p.compareTo(c.q) <= 0) {
                            var e = c.p;
                            c.p = c.q,
                            c.q = e
                        }
                        var n = c.p.subtract(t.ONE)
                          , i = c.q.subtract(t.ONE)
                          , o = n.multiply(i);
                        0 == o.gcd(a).compareTo(t.ONE) ? (c.n = c.p.multiply(c.q),
                        c.d = a.modInverse(o),
                        c.dmp1 = c.d.mod(n),
                        c.dmq1 = c.d.mod(i),
                        c.coeff = c.q.modInverse(c.p),
                        setTimeout(function() {
                            s()
                        }, 0)) : setTimeout(l, 0)
                    }
                      , d = function() {
                        c.q = n(),
                        c.q.fromNumberAsync(r, 1, o, function() {
                            c.q.subtract(t.ONE).gcda(a, function(e) {
                                0 == e.compareTo(t.ONE) && c.q.isProbablePrime(10) ? setTimeout(i, 0) : setTimeout(d, 0)
                            })
                        })
                    }
                      , u = function() {
                        c.p = n(),
                        c.p.fromNumberAsync(e - r, 1, o, function() {
                            c.p.subtract(t.ONE).gcda(a, function(e) {
                                0 == e.compareTo(t.ONE) && c.p.isProbablePrime(10) ? setTimeout(d, 0) : setTimeout(u, 0)
                            })
                        })
                    };
                    setTimeout(u, 0)
                };
                setTimeout(l, 0)
            };
            pn.prototype.generateAsync = e;
            var i = function(e, t) {
                var n = this.s < 0 ? this.negate() : this.clone()
                  , i = e.s < 0 ? e.negate() : e.clone();
                if (n.compareTo(i) < 0) {
                    var s = n;
                    n = i,
                    i = s
                }
                var o = n.getLowestSetBit()
                  , r = i.getLowestSetBit();
                if (0 > r)
                    return void t(n);
                r > o && (r = o),
                r > 0 && (n.rShiftTo(r, n),
                i.rShiftTo(r, i));
                var a = function() {
                    (o = n.getLowestSetBit()) > 0 && n.rShiftTo(o, n),
                    (o = i.getLowestSetBit()) > 0 && i.rShiftTo(o, i),
                    n.compareTo(i) >= 0 ? (n.subTo(i, n),
                    n.rShiftTo(1, n)) : (i.subTo(n, i),
                    i.rShiftTo(1, i)),
                    n.signum() > 0 ? setTimeout(a, 0) : (r > 0 && i.lShiftTo(r, i),
                    setTimeout(function() {
                        t(i)
                    }, 0))
                };
                setTimeout(a, 10)
            };
            t.prototype.gcda = i;
            var s = function(e, n, i, s) {
                if ("number" == typeof n)
                    if (2 > e)
                        this.fromInt(1);
                    else {
                        this.fromNumber(e, i),
                        this.testBit(e - 1) || this.bitwiseTo(t.ONE.shiftLeft(e - 1), at, this),
                        this.isEven() && this.dAddOffset(1, 0);
                        var o = this
                          , r = function() {
                            o.dAddOffset(2, 0),
                            o.bitLength() > e && o.subTo(t.ONE.shiftLeft(e - 1), o),
                            o.isProbablePrime(n) ? setTimeout(function() {
                                s()
                            }, 0) : setTimeout(r, 0)
                        };
                        setTimeout(r, 0)
                    }
                else {
                    var a = new Array
                      , c = 7 & e;
                    a.length = (e >> 3) + 1,
                    n.nextBytes(a),
                    c > 0 ? a[0] &= (1 << c) - 1 : a[0] = 0,
                    this.fromString(a, 256)
                }
            };
            t.prototype.fromNumberAsync = s
        }();
        var Un = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
          , qn = "="
          , Fn = Fn || {};
        Fn.env = Fn.env || {};
        var Wn = Fn
          , Hn = Object.prototype
          , Kn = "[object Function]"
          , jn = ["toString", "valueOf"];
        Fn.env.parseUA = function(e) {
            var t, n = function(e) {
                var t = 0;
                return parseFloat(e.replace(/\./g, function() {
                    return 1 == t++ ? "" : "."
                }))
            }, i = navigator, s = {
                ie: 0,
                opera: 0,
                gecko: 0,
                webkit: 0,
                chrome: 0,
                mobile: null,
                air: 0,
                ipad: 0,
                iphone: 0,
                ipod: 0,
                ios: null,
                android: 0,
                webos: 0,
                caja: i && i.cajaVersion,
                secure: !1,
                os: null
            }, o = e || navigator && navigator.userAgent, r = window && window.location, a = r && r.href;
            return s.secure = a && 0 === a.toLowerCase().indexOf("https"),
            o && (/windows|win32/i.test(o) ? s.os = "windows" : /macintosh/i.test(o) ? s.os = "macintosh" : /rhino/i.test(o) && (s.os = "rhino"),
            /KHTML/.test(o) && (s.webkit = 1),
            t = o.match(/AppleWebKit\/([^\s]*)/),
            t && t[1] && (s.webkit = n(t[1]),
            / Mobile\//.test(o) ? (s.mobile = "Apple",
            t = o.match(/OS ([^\s]*)/),
            t && t[1] && (t = n(t[1].replace("_", "."))),
            s.ios = t,
            s.ipad = s.ipod = s.iphone = 0,
            t = o.match(/iPad|iPod|iPhone/),
            t && t[0] && (s[t[0].toLowerCase()] = s.ios)) : (t = o.match(/NokiaN[^\/]*|Android \d\.\d|webOS\/\d\.\d/),
            t && (s.mobile = t[0]),
            /webOS/.test(o) && (s.mobile = "WebOS",
            t = o.match(/webOS\/([^\s]*);/),
            t && t[1] && (s.webos = n(t[1]))),
            / Android/.test(o) && (s.mobile = "Android",
            t = o.match(/Android ([^\s]*);/),
            t && t[1] && (s.android = n(t[1])))),
            t = o.match(/Chrome\/([^\s]*)/),
            t && t[1] ? s.chrome = n(t[1]) : (t = o.match(/AdobeAIR\/([^\s]*)/),
            t && (s.air = t[0]))),
            s.webkit || (t = o.match(/Opera[\s\/]([^\s]*)/),
            t && t[1] ? (s.opera = n(t[1]),
            t = o.match(/Version\/([^\s]*)/),
            t && t[1] && (s.opera = n(t[1])),
            t = o.match(/Opera Mini[^;]*/),
            t && (s.mobile = t[0])) : (t = o.match(/MSIE\s([^;]*)/),
            t && t[1] ? s.ie = n(t[1]) : (t = o.match(/Gecko\/([^\s]*)/),
            t && (s.gecko = 1,
            t = o.match(/rv:([^\s\)]*)/),
            t && t[1] && (s.gecko = n(t[1]))))))),
            s
        }
        ,
        Fn.env.ua = Fn.env.parseUA(),
        Fn.isFunction = function(e) {
            return "function" == typeof e || Hn.toString.apply(e) === Kn
        }
        ,
        Fn._IEEnumFix = Fn.env.ua.ie ? function(e, t) {
            var n, i, s;
            for (n = 0; n < jn.length; n += 1)
                i = jn[n],
                s = t[i],
                Wn.isFunction(s) && s != Hn[i] && (e[i] = s)
        }
        : function() {}
        ,
        Fn.extend = function(e, t, n) {
            if (!t || !e)
                throw new Error("extend failed, please check that all dependencies are included.");
            var i, s = function() {};
            if (s.prototype = t.prototype,
            e.prototype = new s,
            e.prototype.constructor = e,
            e.superclass = t.prototype,
            t.prototype.constructor == Hn.constructor && (t.prototype.constructor = t),
            n) {
                for (i in n)
                    Wn.hasOwnProperty(n, i) && (e.prototype[i] = n[i]);
                Wn._IEEnumFix(e.prototype, n)
            }
        }
        ,
        "undefined" != typeof KJUR && KJUR || (KJUR = {}),
        "undefined" != typeof KJUR.asn1 && KJUR.asn1 || (KJUR.asn1 = {}),
        KJUR.asn1.ASN1Util = new function() {
            this.integerToByteHex = function(e) {
                var t = e.toString(16);
                return t.length % 2 == 1 && (t = "0" + t),
                t
            }
            ,
            this.bigIntToMinTwosComplementsHex = function(e) {
                var n = e.toString(16);
                if ("-" != n.substr(0, 1))
                    n.length % 2 == 1 ? n = "0" + n : n.match(/^[0-7]/) || (n = "00" + n);
                else {
                    var i = n.substr(1)
                      , s = i.length;
                    s % 2 == 1 ? s += 1 : n.match(/^[0-7]/) || (s += 2);
                    for (var o = "", r = 0; s > r; r++)
                        o += "f";
                    var a = new t(o,16)
                      , c = a.xor(e).add(t.ONE);
                    n = c.toString(16).replace(/^-/, "")
                }
                return n
            }
            ,
            this.getPEMStringFromHex = function(e, t) {
                var n = CryptoJS.enc.Hex.parse(e)
                  , i = CryptoJS.enc.Base64.stringify(n)
                  , s = i.replace(/(.{64})/g, "$1\r\n");
                return s = s.replace(/\r\n$/, ""),
                "-----BEGIN " + t + "-----\r\n" + s + "\r\n-----END " + t + "-----\r\n"
            }
        }
        ,
        KJUR.asn1.ASN1Object = function() {
            var e = "";
            this.getLengthHexFromValue = function() {
                if ("undefined" == typeof this.hV || null == this.hV)
                    throw "this.hV is null or undefined.";
                if (this.hV.length % 2 == 1)
                    throw "value hex must be even length: n=" + e.length + ",v=" + this.hV;
                var t = this.hV.length / 2
                  , n = t.toString(16);
                if (n.length % 2 == 1 && (n = "0" + n),
                128 > t)
                    return n;
                var i = n.length / 2;
                if (i > 15)
                    throw "ASN.1 length too long to represent by 8x: n = " + t.toString(16);
                var s = 128 + i;
                return s.toString(16) + n
            }
            ,
            this.getEncodedHex = function() {
                return (null == this.hTLV || this.isModified) && (this.hV = this.getFreshValueHex(),
                this.hL = this.getLengthHexFromValue(),
                this.hTLV = this.hT + this.hL + this.hV,
                this.isModified = !1),
                this.hTLV
            }
            ,
            this.getValueHex = function() {
                return this.getEncodedHex(),
                this.hV
            }
            ,
            this.getFreshValueHex = function() {
                return ""
            }
        }
        ,
        KJUR.asn1.DERAbstractString = function(e) {
            KJUR.asn1.DERAbstractString.superclass.constructor.call(this),
            this.getString = function() {
                return this.s
            }
            ,
            this.setString = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.s = e,
                this.hV = stohex(this.s)
            }
            ,
            this.setStringHex = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.s = null,
                this.hV = e
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            "undefined" != typeof e && ("undefined" != typeof e.str ? this.setString(e.str) : "undefined" != typeof e.hex && this.setStringHex(e.hex))
        }
        ,
        Fn.extend(KJUR.asn1.DERAbstractString, KJUR.asn1.ASN1Object),
        KJUR.asn1.DERAbstractTime = function() {
            KJUR.asn1.DERAbstractTime.superclass.constructor.call(this),
            this.localDateToUTC = function(e) {
                utc = e.getTime() + 6e4 * e.getTimezoneOffset();
                var t = new Date(utc);
                return t
            }
            ,
            this.formatDate = function(e, t) {
                var n = this.zeroPadding
                  , i = this.localDateToUTC(e)
                  , s = String(i.getFullYear());
                "utc" == t && (s = s.substr(2, 2));
                var o = n(String(i.getMonth() + 1), 2)
                  , r = n(String(i.getDate()), 2)
                  , a = n(String(i.getHours()), 2)
                  , c = n(String(i.getMinutes()), 2)
                  , l = n(String(i.getSeconds()), 2);
                return s + o + r + a + c + l + "Z"
            }
            ,
            this.zeroPadding = function(e, t) {
                return e.length >= t ? e : new Array(t - e.length + 1).join("0") + e
            }
            ,
            this.getString = function() {
                return this.s
            }
            ,
            this.setString = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.s = e,
                this.hV = stohex(this.s)
            }
            ,
            this.setByDateValue = function(e, t, n, i, s, o) {
                var r = new Date(Date.UTC(e, t - 1, n, i, s, o, 0));
                this.setByDate(r)
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
        }
        ,
        Fn.extend(KJUR.asn1.DERAbstractTime, KJUR.asn1.ASN1Object),
        KJUR.asn1.DERAbstractStructured = function(e) {
            KJUR.asn1.DERAbstractString.superclass.constructor.call(this),
            this.setByASN1ObjectArray = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.asn1Array = e
            }
            ,
            this.appendASN1Object = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.asn1Array.push(e)
            }
            ,
            this.asn1Array = new Array,
            "undefined" != typeof e && "undefined" != typeof e.array && (this.asn1Array = e.array)
        }
        ,
        Fn.extend(KJUR.asn1.DERAbstractStructured, KJUR.asn1.ASN1Object),
        KJUR.asn1.DERBoolean = function() {
            KJUR.asn1.DERBoolean.superclass.constructor.call(this),
            this.hT = "01",
            this.hTLV = "0101ff"
        }
        ,
        Fn.extend(KJUR.asn1.DERBoolean, KJUR.asn1.ASN1Object),
        KJUR.asn1.DERInteger = function(e) {
            KJUR.asn1.DERInteger.superclass.constructor.call(this),
            this.hT = "02",
            this.setByBigInteger = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.hV = KJUR.asn1.ASN1Util.bigIntToMinTwosComplementsHex(e)
            }
            ,
            this.setByInteger = function(e) {
                var n = new t(String(e),10);
                this.setByBigInteger(n)
            }
            ,
            this.setValueHex = function(e) {
                this.hV = e
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            "undefined" != typeof e && ("undefined" != typeof e.bigint ? this.setByBigInteger(e.bigint) : "undefined" != typeof e["int"] ? this.setByInteger(e["int"]) : "undefined" != typeof e.hex && this.setValueHex(e.hex))
        }
        ,
        Fn.extend(KJUR.asn1.DERInteger, KJUR.asn1.ASN1Object),
        KJUR.asn1.DERBitString = function(e) {
            KJUR.asn1.DERBitString.superclass.constructor.call(this),
            this.hT = "03",
            this.setHexValueIncludingUnusedBits = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.hV = e
            }
            ,
            this.setUnusedBitsAndHexValue = function(e, t) {
                if (0 > e || e > 7)
                    throw "unused bits shall be from 0 to 7: u = " + e;
                var n = "0" + e;
                this.hTLV = null,
                this.isModified = !0,
                this.hV = n + t
            }
            ,
            this.setByBinaryString = function(e) {
                e = e.replace(/0+$/, "");
                var t = 8 - e.length % 8;
                8 == t && (t = 0);
                for (var n = 0; t >= n; n++)
                    e += "0";
                for (var i = "", n = 0; n < e.length - 1; n += 8) {
                    var s = e.substr(n, 8)
                      , o = parseInt(s, 2).toString(16);
                    1 == o.length && (o = "0" + o),
                    i += o
                }
                this.hTLV = null,
                this.isModified = !0,
                this.hV = "0" + t + i
            }
            ,
            this.setByBooleanArray = function(e) {
                for (var t = "", n = 0; n < e.length; n++)
                    t += 1 == e[n] ? "1" : "0";
                this.setByBinaryString(t)
            }
            ,
            this.newFalseArray = function(e) {
                for (var t = new Array(e), n = 0; e > n; n++)
                    t[n] = !1;
                return t
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            "undefined" != typeof e && ("undefined" != typeof e.hex ? this.setHexValueIncludingUnusedBits(e.hex) : "undefined" != typeof e.bin ? this.setByBinaryString(e.bin) : "undefined" != typeof e.array && this.setByBooleanArray(e.array))
        }
        ,
        Fn.extend(KJUR.asn1.DERBitString, KJUR.asn1.ASN1Object),
        KJUR.asn1.DEROctetString = function(e) {
            KJUR.asn1.DEROctetString.superclass.constructor.call(this, e),
            this.hT = "04"
        }
        ,
        Fn.extend(KJUR.asn1.DEROctetString, KJUR.asn1.DERAbstractString),
        KJUR.asn1.DERNull = function() {
            KJUR.asn1.DERNull.superclass.constructor.call(this),
            this.hT = "05",
            this.hTLV = "0500"
        }
        ,
        Fn.extend(KJUR.asn1.DERNull, KJUR.asn1.ASN1Object),
        KJUR.asn1.DERObjectIdentifier = function(e) {
            var n = function(e) {
                var t = e.toString(16);
                return 1 == t.length && (t = "0" + t),
                t
            }
              , i = function(e) {
                var i = ""
                  , s = new t(e,10)
                  , o = s.toString(2)
                  , r = 7 - o.length % 7;
                7 == r && (r = 0);
                for (var a = "", c = 0; r > c; c++)
                    a += "0";
                o = a + o;
                for (var c = 0; c < o.length - 1; c += 7) {
                    var l = o.substr(c, 7);
                    c != o.length - 7 && (l = "1" + l),
                    i += n(parseInt(l, 2))
                }
                return i
            };
            KJUR.asn1.DERObjectIdentifier.superclass.constructor.call(this),
            this.hT = "06",
            this.setValueHex = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.s = null,
                this.hV = e
            }
            ,
            this.setValueOidString = function(e) {
                if (!e.match(/^[0-9.]+$/))
                    throw "malformed oid string: " + e;
                var t = ""
                  , s = e.split(".")
                  , o = 40 * parseInt(s[0]) + parseInt(s[1]);
                t += n(o),
                s.splice(0, 2);
                for (var r = 0; r < s.length; r++)
                    t += i(s[r]);
                this.hTLV = null,
                this.isModified = !0,
                this.s = null,
                this.hV = t
            }
            ,
            this.setValueName = function(e) {
                if ("undefined" == typeof KJUR.asn1.x509.OID.name2oidList[e])
                    throw "DERObjectIdentifier oidName undefined: " + e;
                var t = KJUR.asn1.x509.OID.name2oidList[e];
                this.setValueOidString(t)
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            "undefined" != typeof e && ("undefined" != typeof e.oid ? this.setValueOidString(e.oid) : "undefined" != typeof e.hex ? this.setValueHex(e.hex) : "undefined" != typeof e.name && this.setValueName(e.name))
        }
        ,
        Fn.extend(KJUR.asn1.DERObjectIdentifier, KJUR.asn1.ASN1Object),
        KJUR.asn1.DERUTF8String = function(e) {
            KJUR.asn1.DERUTF8String.superclass.constructor.call(this, e),
            this.hT = "0c"
        }
        ,
        Fn.extend(KJUR.asn1.DERUTF8String, KJUR.asn1.DERAbstractString),
        KJUR.asn1.DERNumericString = function(e) {
            KJUR.asn1.DERNumericString.superclass.constructor.call(this, e),
            this.hT = "12"
        }
        ,
        Fn.extend(KJUR.asn1.DERNumericString, KJUR.asn1.DERAbstractString),
        KJUR.asn1.DERPrintableString = function(e) {
            KJUR.asn1.DERPrintableString.superclass.constructor.call(this, e),
            this.hT = "13"
        }
        ,
        Fn.extend(KJUR.asn1.DERPrintableString, KJUR.asn1.DERAbstractString),
        KJUR.asn1.DERTeletexString = function(e) {
            KJUR.asn1.DERTeletexString.superclass.constructor.call(this, e),
            this.hT = "14"
        }
        ,
        Fn.extend(KJUR.asn1.DERTeletexString, KJUR.asn1.DERAbstractString),
        KJUR.asn1.DERIA5String = function(e) {
            KJUR.asn1.DERIA5String.superclass.constructor.call(this, e),
            this.hT = "16"
        }
        ,
        Fn.extend(KJUR.asn1.DERIA5String, KJUR.asn1.DERAbstractString),
        KJUR.asn1.DERUTCTime = function(e) {
            KJUR.asn1.DERUTCTime.superclass.constructor.call(this, e),
            this.hT = "17",
            this.setByDate = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.date = e,
                this.s = this.formatDate(this.date, "utc"),
                this.hV = stohex(this.s)
            }
            ,
            "undefined" != typeof e && ("undefined" != typeof e.str ? this.setString(e.str) : "undefined" != typeof e.hex ? this.setStringHex(e.hex) : "undefined" != typeof e.date && this.setByDate(e.date))
        }
        ,
        Fn.extend(KJUR.asn1.DERUTCTime, KJUR.asn1.DERAbstractTime),
        KJUR.asn1.DERGeneralizedTime = function(e) {
            KJUR.asn1.DERGeneralizedTime.superclass.constructor.call(this, e),
            this.hT = "18",
            this.setByDate = function(e) {
                this.hTLV = null,
                this.isModified = !0,
                this.date = e,
                this.s = this.formatDate(this.date, "gen"),
                this.hV = stohex(this.s)
            }
            ,
            "undefined" != typeof e && ("undefined" != typeof e.str ? this.setString(e.str) : "undefined" != typeof e.hex ? this.setStringHex(e.hex) : "undefined" != typeof e.date && this.setByDate(e.date))
        }
        ,
        Fn.extend(KJUR.asn1.DERGeneralizedTime, KJUR.asn1.DERAbstractTime),
        KJUR.asn1.DERSequence = function(e) {
            KJUR.asn1.DERSequence.superclass.constructor.call(this, e),
            this.hT = "30",
            this.getFreshValueHex = function() {
                for (var e = "", t = 0; t < this.asn1Array.length; t++) {
                    var n = this.asn1Array[t];
                    e += n.getEncodedHex()
                }
                return this.hV = e,
                this.hV
            }
        }
        ,
        Fn.extend(KJUR.asn1.DERSequence, KJUR.asn1.DERAbstractStructured),
        KJUR.asn1.DERSet = function(e) {
            KJUR.asn1.DERSet.superclass.constructor.call(this, e),
            this.hT = "31",
            this.getFreshValueHex = function() {
                for (var e = new Array, t = 0; t < this.asn1Array.length; t++) {
                    var n = this.asn1Array[t];
                    e.push(n.getEncodedHex())
                }
                return e.sort(),
                this.hV = e.join(""),
                this.hV
            }
        }
        ,
        Fn.extend(KJUR.asn1.DERSet, KJUR.asn1.DERAbstractStructured),
        KJUR.asn1.DERTaggedObject = function(e) {
            KJUR.asn1.DERTaggedObject.superclass.constructor.call(this),
            this.hT = "a0",
            this.hV = "",
            this.isExplicit = !0,
            this.asn1Object = null,
            this.setASN1Object = function(e, t, n) {
                this.hT = t,
                this.isExplicit = e,
                this.asn1Object = n,
                this.isExplicit ? (this.hV = this.asn1Object.getEncodedHex(),
                this.hTLV = null,
                this.isModified = !0) : (this.hV = null,
                this.hTLV = n.getEncodedHex(),
                this.hTLV = this.hTLV.replace(/^../, t),
                this.isModified = !1)
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            "undefined" != typeof e && ("undefined" != typeof e.tag && (this.hT = e.tag),
            "undefined" != typeof e.explicit && (this.isExplicit = e.explicit),
            "undefined" != typeof e.obj && (this.asn1Object = e.obj,
            this.setASN1Object(this.isExplicit, this.hT, this.asn1Object)))
        }
        ,
        Fn.extend(KJUR.asn1.DERTaggedObject, KJUR.asn1.ASN1Object),
        function(e) {
            "use strict";
            var t, n = {};
            n.decode = function(n) {
                var i;
                if (t === e) {
                    var s = "0123456789ABCDEF"
                      , o = " \f\n\r	 \u2028\u2029";
                    for (t = [],
                    i = 0; 16 > i; ++i)
                        t[s.charAt(i)] = i;
                    for (s = s.toLowerCase(),
                    i = 10; 16 > i; ++i)
                        t[s.charAt(i)] = i;
                    for (i = 0; i < o.length; ++i)
                        t[o.charAt(i)] = -1
                }
                var r = []
                  , a = 0
                  , c = 0;
                for (i = 0; i < n.length; ++i) {
                    var l = n.charAt(i);
                    if ("=" == l)
                        break;
                    if (l = t[l],
                    -1 != l) {
                        if (l === e)
                            throw "Illegal character at offset " + i;
                        a |= l,
                        ++c >= 2 ? (r[r.length] = a,
                        a = 0,
                        c = 0) : a <<= 4
                    }
                }
                if (c)
                    throw "Hex encoding incomplete: 4 bits missing";
                return r
            }
            ,
            window.Hex = n
        }(),
        function(e) {
            "use strict";
            var t, n = {};
            n.decode = function(n) {
                var i;
                if (t === e) {
                    var s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
                      , o = "= \f\n\r	 \u2028\u2029";
                    for (t = [],
                    i = 0; 64 > i; ++i)
                        t[s.charAt(i)] = i;
                    for (i = 0; i < o.length; ++i)
                        t[o.charAt(i)] = -1
                }
                var r = []
                  , a = 0
                  , c = 0;
                for (i = 0; i < n.length; ++i) {
                    var l = n.charAt(i);
                    if ("=" == l)
                        break;
                    if (l = t[l],
                    -1 != l) {
                        if (l === e)
                            throw "Illegal character at offset " + i;
                        a |= l,
                        ++c >= 4 ? (r[r.length] = a >> 16,
                        r[r.length] = a >> 8 & 255,
                        r[r.length] = 255 & a,
                        a = 0,
                        c = 0) : a <<= 6
                    }
                }
                switch (c) {
                case 1:
                    throw "Base64 encoding incomplete: at least 2 bits missing";
                case 2:
                    r[r.length] = a >> 10;
                    break;
                case 3:
                    r[r.length] = a >> 16,
                    r[r.length] = a >> 8 & 255
                }
                return r
            }
            ,
            n.re = /-----BEGIN [^-]+-----([A-Za-z0-9+\/=\s]+)-----END [^-]+-----|begin-base64[^\n]+\n([A-Za-z0-9+\/=\s]+)====/,
            n.unarmor = function(e) {
                var t = n.re.exec(e);
                if (t)
                    if (t[1])
                        e = t[1];
                    else {
                        if (!t[2])
                            throw "RegExp out of sync";
                        e = t[2]
                    }
                return n.decode(e)
            }
            ,
            window.Base64 = n
        }(),
        function(e) {
            "use strict";
            function t(e, n) {
                e instanceof t ? (this.enc = e.enc,
                this.pos = e.pos) : (this.enc = e,
                this.pos = n)
            }
            function n(e, t, n, i, s) {
                this.stream = e,
                this.header = t,
                this.length = n,
                this.tag = i,
                this.sub = s
            }
            var i = 100
              , s = "…"
              , o = {
                tag: function(e, t) {
                    var n = document.createElement(e);
                    return n.className = t,
                    n
                },
                text: function(e) {
                    return document.createTextNode(e)
                }
            };
            t.prototype.get = function(t) {
                if (t === e && (t = this.pos++),
                t >= this.enc.length)
                    throw "Requesting byte offset " + t + " on a stream of length " + this.enc.length;
                return this.enc[t]
            }
            ,
            t.prototype.hexDigits = "0123456789ABCDEF",
            t.prototype.hexByte = function(e) {
                return this.hexDigits.charAt(e >> 4 & 15) + this.hexDigits.charAt(15 & e)
            }
            ,
            t.prototype.hexDump = function(e, t, n) {
                for (var i = "", s = e; t > s; ++s)
                    if (i += this.hexByte(this.get(s)),
                    n !== !0)
                        switch (15 & s) {
                        case 7:
                            i += "  ";
                            break;
                        case 15:
                            i += "\n";
                            break;
                        default:
                            i += " "
                        }
                return i
            }
            ,
            t.prototype.parseStringISO = function(e, t) {
                for (var n = "", i = e; t > i; ++i)
                    n += String.fromCharCode(this.get(i));
                return n
            }
            ,
            t.prototype.parseStringUTF = function(e, t) {
                for (var n = "", i = e; t > i; ) {
                    var s = this.get(i++);
                    n += String.fromCharCode(128 > s ? s : s > 191 && 224 > s ? (31 & s) << 6 | 63 & this.get(i++) : (15 & s) << 12 | (63 & this.get(i++)) << 6 | 63 & this.get(i++))
                }
                return n
            }
            ,
            t.prototype.parseStringBMP = function(e, t) {
                for (var n = "", i = e; t > i; i += 2) {
                    var s = this.get(i)
                      , o = this.get(i + 1);
                    n += String.fromCharCode((s << 8) + o)
                }
                return n
            }
            ,
            t.prototype.reTime = /^((?:1[89]|2\d)?\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/,
            t.prototype.parseTime = function(e, t) {
                var n = this.parseStringISO(e, t)
                  , i = this.reTime.exec(n);
                return i ? (n = i[1] + "-" + i[2] + "-" + i[3] + " " + i[4],
                i[5] && (n += ":" + i[5],
                i[6] && (n += ":" + i[6],
                i[7] && (n += "." + i[7]))),
                i[8] && (n += " UTC",
                "Z" != i[8] && (n += i[8],
                i[9] && (n += ":" + i[9]))),
                n) : "Unrecognized time: " + n
            }
            ,
            t.prototype.parseInteger = function(e, t) {
                var n = t - e;
                if (n > 4) {
                    n <<= 3;
                    var i = this.get(e);
                    if (0 === i)
                        n -= 8;
                    else
                        for (; 128 > i; )
                            i <<= 1,
                            --n;
                    return "(" + n + " bit)"
                }
                for (var s = 0, o = e; t > o; ++o)
                    s = s << 8 | this.get(o);
                return s
            }
            ,
            t.prototype.parseBitString = function(e, t) {
                var n = this.get(e)
                  , i = (t - e - 1 << 3) - n
                  , s = "(" + i + " bit)";
                if (20 >= i) {
                    var o = n;
                    s += " ";
                    for (var r = t - 1; r > e; --r) {
                        for (var a = this.get(r), c = o; 8 > c; ++c)
                            s += a >> c & 1 ? "1" : "0";
                        o = 0
                    }
                }
                return s
            }
            ,
            t.prototype.parseOctetString = function(e, t) {
                var n = t - e
                  , o = "(" + n + " byte) ";
                n > i && (t = e + i);
                for (var r = e; t > r; ++r)
                    o += this.hexByte(this.get(r));
                return n > i && (o += s),
                o
            }
            ,
            t.prototype.parseOID = function(e, t) {
                for (var n = "", i = 0, s = 0, o = e; t > o; ++o) {
                    var r = this.get(o);
                    if (i = i << 7 | 127 & r,
                    s += 7,
                    !(128 & r)) {
                        if ("" === n) {
                            var a = 80 > i ? 40 > i ? 0 : 1 : 2;
                            n = a + "." + (i - 40 * a)
                        } else
                            n += "." + (s >= 31 ? "bigint" : i);
                        i = s = 0
                    }
                }
                return n
            }
            ,
            n.prototype.typeName = function() {
                if (this.tag === e)
                    return "unknown";
                var t = this.tag >> 6
                  , n = (this.tag >> 5 & 1,
                31 & this.tag);
                switch (t) {
                case 0:
                    switch (n) {
                    case 0:
                        return "EOC";
                    case 1:
                        return "BOOLEAN";
                    case 2:
                        return "INTEGER";
                    case 3:
                        return "BIT_STRING";
                    case 4:
                        return "OCTET_STRING";
                    case 5:
                        return "NULL";
                    case 6:
                        return "OBJECT_IDENTIFIER";
                    case 7:
                        return "ObjectDescriptor";
                    case 8:
                        return "EXTERNAL";
                    case 9:
                        return "REAL";
                    case 10:
                        return "ENUMERATED";
                    case 11:
                        return "EMBEDDED_PDV";
                    case 12:
                        return "UTF8String";
                    case 16:
                        return "SEQUENCE";
                    case 17:
                        return "SET";
                    case 18:
                        return "NumericString";
                    case 19:
                        return "PrintableString";
                    case 20:
                        return "TeletexString";
                    case 21:
                        return "VideotexString";
                    case 22:
                        return "IA5String";
                    case 23:
                        return "UTCTime";
                    case 24:
                        return "GeneralizedTime";
                    case 25:
                        return "GraphicString";
                    case 26:
                        return "VisibleString";
                    case 27:
                        return "GeneralString";
                    case 28:
                        return "UniversalString";
                    case 30:
                        return "BMPString";
                    default:
                        return "Universal_" + n.toString(16)
                    }
                case 1:
                    return "Application_" + n.toString(16);
                case 2:
                    return "[" + n + "]";
                case 3:
                    return "Private_" + n.toString(16)
                }
            }
            ,
            n.prototype.reSeemsASCII = /^[ -~]+$/,
            n.prototype.content = function() {
                if (this.tag === e)
                    return null;
                var t = this.tag >> 6
                  , n = 31 & this.tag
                  , o = this.posContent()
                  , r = Math.abs(this.length);
                if (0 !== t) {
                    if (null !== this.sub)
                        return "(" + this.sub.length + " elem)";
                    var a = this.stream.parseStringISO(o, o + Math.min(r, i));
                    return this.reSeemsASCII.test(a) ? a.substring(0, 2 * i) + (a.length > 2 * i ? s : "") : this.stream.parseOctetString(o, o + r)
                }
                switch (n) {
                case 1:
                    return 0 === this.stream.get(o) ? "false" : "true";
                case 2:
                    return this.stream.parseInteger(o, o + r);
                case 3:
                    return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseBitString(o, o + r);
                case 4:
                    return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(o, o + r);
                case 6:
                    return this.stream.parseOID(o, o + r);
                case 16:
                case 17:
                    return "(" + this.sub.length + " elem)";
                case 12:
                    return this.stream.parseStringUTF(o, o + r);
                case 18:
                case 19:
                case 20:
                case 21:
                case 22:
                case 26:
                    return this.stream.parseStringISO(o, o + r);
                case 30:
                    return this.stream.parseStringBMP(o, o + r);
                case 23:
                case 24:
                    return this.stream.parseTime(o, o + r)
                }
                return null
            }
            ,
            n.prototype.toString = function() {
                return this.typeName() + "@" + this.stream.pos + "[header:" + this.header + ",length:" + this.length + ",sub:" + (null === this.sub ? "null" : this.sub.length) + "]"
            }
            ,
            n.prototype.print = function(t) {
                if (t === e && (t = ""),
                document.writeln(t + this),
                null !== this.sub) {
                    t += "  ";
                    for (var n = 0, i = this.sub.length; i > n; ++n)
                        this.sub[n].print(t)
                }
            }
            ,
            n.prototype.toPrettyString = function(t) {
                t === e && (t = "");
                var n = t + this.typeName() + " @" + this.stream.pos;
                if (this.length >= 0 && (n += "+"),
                n += this.length,
                32 & this.tag ? n += " (constructed)" : 3 != this.tag && 4 != this.tag || null === this.sub || (n += " (encapsulates)"),
                n += "\n",
                null !== this.sub) {
                    t += "  ";
                    for (var i = 0, s = this.sub.length; s > i; ++i)
                        n += this.sub[i].toPrettyString(t)
                }
                return n
            }
            ,
            n.prototype.toDOM = function() {
                var e = o.tag("div", "node");
                e.asn1 = this;
                var t = o.tag("div", "head")
                  , n = this.typeName().replace(/_/g, " ");
                t.innerHTML = n;
                var i = this.content();
                if (null !== i) {
                    i = String(i).replace(/</g, "&lt;");
                    var s = o.tag("span", "preview");
                    s.appendChild(o.text(i)),
                    t.appendChild(s)
                }
                e.appendChild(t),
                this.node = e,
                this.head = t;
                var r = o.tag("div", "value");
                if (n = "Offset: " + this.stream.pos + "<br/>",
                n += "Length: " + this.header + "+",
                n += this.length >= 0 ? this.length : -this.length + " (undefined)",
                32 & this.tag ? n += "<br/>(constructed)" : 3 != this.tag && 4 != this.tag || null === this.sub || (n += "<br/>(encapsulates)"),
                null !== i && (n += "<br/>Value:<br/><b>" + i + "</b>",
                "object" == typeof oids && 6 == this.tag)) {
                    var a = oids[i];
                    a && (a.d && (n += "<br/>" + a.d),
                    a.c && (n += "<br/>" + a.c),
                    a.w && (n += "<br/>(warning!)"))
                }
                r.innerHTML = n,
                e.appendChild(r);
                var c = o.tag("div", "sub");
                if (null !== this.sub)
                    for (var l = 0, d = this.sub.length; d > l; ++l)
                        c.appendChild(this.sub[l].toDOM());
                return e.appendChild(c),
                t.onclick = function() {
                    e.className = "node collapsed" == e.className ? "node" : "node collapsed"
                }
                ,
                e
            }
            ,
            n.prototype.posStart = function() {
                return this.stream.pos
            }
            ,
            n.prototype.posContent = function() {
                return this.stream.pos + this.header
            }
            ,
            n.prototype.posEnd = function() {
                return this.stream.pos + this.header + Math.abs(this.length)
            }
            ,
            n.prototype.fakeHover = function(e) {
                this.node.className += " hover",
                e && (this.head.className += " hover")
            }
            ,
            n.prototype.fakeOut = function(e) {
                var t = / ?hover/;
                this.node.className = this.node.className.replace(t, ""),
                e && (this.head.className = this.head.className.replace(t, ""))
            }
            ,
            n.prototype.toHexDOM_sub = function(e, t, n, i, s) {
                if (!(i >= s)) {
                    var r = o.tag("span", t);
                    r.appendChild(o.text(n.hexDump(i, s))),
                    e.appendChild(r)
                }
            }
            ,
            n.prototype.toHexDOM = function(t) {
                var n = o.tag("span", "hex");
                if (t === e && (t = n),
                this.head.hexNode = n,
                this.head.onmouseover = function() {
                    this.hexNode.className = "hexCurrent"
                }
                ,
                this.head.onmouseout = function() {
                    this.hexNode.className = "hex"
                }
                ,
                n.asn1 = this,
                n.onmouseover = function() {
                    var e = !t.selected;
                    e && (t.selected = this.asn1,
                    this.className = "hexCurrent"),
                    this.asn1.fakeHover(e)
                }
                ,
                n.onmouseout = function() {
                    var e = t.selected == this.asn1;
                    this.asn1.fakeOut(e),
                    e && (t.selected = null,
                    this.className = "hex")
                }
                ,
                this.toHexDOM_sub(n, "tag", this.stream, this.posStart(), this.posStart() + 1),
                this.toHexDOM_sub(n, this.length >= 0 ? "dlen" : "ulen", this.stream, this.posStart() + 1, this.posContent()),
                null === this.sub)
                    n.appendChild(o.text(this.stream.hexDump(this.posContent(), this.posEnd())));
                else if (this.sub.length > 0) {
                    var i = this.sub[0]
                      , s = this.sub[this.sub.length - 1];
                    this.toHexDOM_sub(n, "intro", this.stream, this.posContent(), i.posStart());
                    for (var r = 0, a = this.sub.length; a > r; ++r)
                        n.appendChild(this.sub[r].toHexDOM(t));
                    this.toHexDOM_sub(n, "outro", this.stream, s.posEnd(), this.posEnd())
                }
                return n
            }
            ,
            n.prototype.toHexString = function() {
                return this.stream.hexDump(this.posStart(), this.posEnd(), !0)
            }
            ,
            n.decodeLength = function(e) {
                var t = e.get()
                  , n = 127 & t;
                if (n == t)
                    return n;
                if (n > 3)
                    throw "Length over 24 bits not supported at position " + (e.pos - 1);
                if (0 === n)
                    return -1;
                t = 0;
                for (var i = 0; n > i; ++i)
                    t = t << 8 | e.get();
                return t
            }
            ,
            n.hasContent = function(e, i, s) {
                if (32 & e)
                    return !0;
                if (3 > e || e > 4)
                    return !1;
                var o = new t(s);
                3 == e && o.get();
                var r = o.get();
                if (r >> 6 & 1)
                    return !1;
                try {
                    var a = n.decodeLength(o);
                    return o.pos - s.pos + a == i
                } catch (c) {
                    return !1
                }
            }
            ,
            n.decode = function(e) {
                e instanceof t || (e = new t(e,0));
                var i = new t(e)
                  , s = e.get()
                  , o = n.decodeLength(e)
                  , r = e.pos - i.pos
                  , a = null;
                if (n.hasContent(s, o, e)) {
                    var c = e.pos;
                    if (3 == s && e.get(),
                    a = [],
                    o >= 0) {
                        for (var l = c + o; e.pos < l; )
                            a[a.length] = n.decode(e);
                        if (e.pos != l)
                            throw "Content size is not correct for container starting at offset " + c
                    } else
                        try {
                            for (; ; ) {
                                var d = n.decode(e);
                                if (0 === d.tag)
                                    break;
                                a[a.length] = d
                            }
                            o = c - e.pos
                        } catch (u) {
                            throw "Exception while decoding undefined length content: " + u
                        }
                } else
                    e.pos += o;
                return new n(i,r,o,s,a)
            }
            ,
            n.test = function() {
                for (var e = [{
                    value: [39],
                    expected: 39
                }, {
                    value: [129, 201],
                    expected: 201
                }, {
                    value: [131, 254, 220, 186],
                    expected: 16702650
                }], i = 0, s = e.length; s > i; ++i) {
                    var o = new t(e[i].value,0)
                      , r = n.decodeLength(o);
                    r != e[i].expected && document.write("In test[" + i + "] expected " + e[i].expected + " got " + r + "\n")
                }
            }
            ,
            window.ASN1 = n
        }(),
        ASN1.prototype.getHexStringValue = function() {
            var e = this.toHexString()
              , t = 2 * this.header
              , n = 2 * this.length;
            return e.substr(t, n)
        }
        ,
        pn.prototype.parseKey = function(e) {
            try {
                var t = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/
                  , n = t.test(e) ? Hex.decode(e) : Base64.unarmor(e)
                  , i = ASN1.decode(n);
                if (9 === i.sub.length) {
                    var s = i.sub[1].getHexStringValue();
                    this.n = dn(s, 16);
                    var o = i.sub[2].getHexStringValue();
                    this.e = parseInt(o, 16);
                    var r = i.sub[3].getHexStringValue();
                    this.d = dn(r, 16);
                    var a = i.sub[4].getHexStringValue();
                    this.p = dn(a, 16);
                    var c = i.sub[5].getHexStringValue();
                    this.q = dn(c, 16);
                    var l = i.sub[6].getHexStringValue();
                    this.dmp1 = dn(l, 16);
                    var d = i.sub[7].getHexStringValue();
                    this.dmq1 = dn(d, 16);
                    var u = i.sub[8].getHexStringValue();
                    this.coeff = dn(u, 16)
                } else {
                    if (2 !== i.sub.length)
                        return !1;
                    var p = i.sub[1]
                      , g = p.sub[0]
                      , s = g.sub[0].getHexStringValue();
                    this.n = dn(s, 16);
                    var o = g.sub[1].getHexStringValue();
                    this.e = parseInt(o, 16)
                }
                return !0
            } catch (h) {
                return !1
            }
        }
        ,
        pn.prototype.getPrivateBaseKey = function() {
            var e = {
                array: [new KJUR.asn1.DERInteger({
                    "int": 0
                }), new KJUR.asn1.DERInteger({
                    bigint: this.n
                }), new KJUR.asn1.DERInteger({
                    "int": this.e
                }), new KJUR.asn1.DERInteger({
                    bigint: this.d
                }), new KJUR.asn1.DERInteger({
                    bigint: this.p
                }), new KJUR.asn1.DERInteger({
                    bigint: this.q
                }), new KJUR.asn1.DERInteger({
                    bigint: this.dmp1
                }), new KJUR.asn1.DERInteger({
                    bigint: this.dmq1
                }), new KJUR.asn1.DERInteger({
                    bigint: this.coeff
                })]
            }
              , t = new KJUR.asn1.DERSequence(e);
            return t.getEncodedHex()
        }
        ,
        pn.prototype.getPrivateBaseKeyB64 = function() {
            return Cn(this.getPrivateBaseKey())
        }
        ,
        pn.prototype.getPublicBaseKey = function() {
            var e = {
                array: [new KJUR.asn1.DERObjectIdentifier({
                    oid: "1.2.840.113549.1.1.1"
                }), new KJUR.asn1.DERNull]
            }
              , t = new KJUR.asn1.DERSequence(e);
            e = {
                array: [new KJUR.asn1.DERInteger({
                    bigint: this.n
                }), new KJUR.asn1.DERInteger({
                    "int": this.e
                })]
            };
            var n = new KJUR.asn1.DERSequence(e);
            e = {
                hex: "00" + n.getEncodedHex()
            };
            var i = new KJUR.asn1.DERBitString(e);
            e = {
                array: [t, i]
            };
            var s = new KJUR.asn1.DERSequence(e);
            return s.getEncodedHex()
        }
        ,
        pn.prototype.getPublicBaseKeyB64 = function() {
            return Cn(this.getPublicBaseKey())
        }
        ,
        pn.prototype.wordwrap = function(e, t) {
            if (t = t || 64,
            !e)
                return e;
            var n = "(.{1," + t + "})( +|$\n?)|(.{1," + t + "})";
            return e.match(RegExp(n, "g")).join("\n")
        }
        ,
        pn.prototype.getPrivateKey = function() {
            var e = "-----BEGIN RSA PRIVATE KEY-----\n";
            return e += this.wordwrap(this.getPrivateBaseKeyB64()) + "\n",
            e += "-----END RSA PRIVATE KEY-----"
        }
        ,
        pn.prototype.getPublicKey = function() {
            var e = "-----BEGIN PUBLIC KEY-----\n";
            return e += this.wordwrap(this.getPublicBaseKeyB64()) + "\n",
            e += "-----END PUBLIC KEY-----"
        }
        ,
        pn.prototype.hasPublicKeyProperty = function(e) {
            return e = e || {},
            e.hasOwnProperty("n") && e.hasOwnProperty("e")
        }
        ,
        pn.prototype.hasPrivateKeyProperty = function(e) {
            return e = e || {},
            e.hasOwnProperty("n") && e.hasOwnProperty("e") && e.hasOwnProperty("d") && e.hasOwnProperty("p") && e.hasOwnProperty("q") && e.hasOwnProperty("dmp1") && e.hasOwnProperty("dmq1") && e.hasOwnProperty("coeff")
        }
        ,
        pn.prototype.parsePropertiesFrom = function(e) {
            this.n = e.n,
            this.e = e.e,
            e.hasOwnProperty("d") && (this.d = e.d,
            this.p = e.p,
            this.q = e.q,
            this.dmp1 = e.dmp1,
            this.dmq1 = e.dmq1,
            this.coeff = e.coeff)
        }
        ;
        var Jn = function(e) {
            pn.call(this),
            e && ("string" == typeof e ? this.parseKey(e) : (this.hasPrivateKeyProperty(e) || this.hasPublicKeyProperty(e)) && this.parsePropertiesFrom(e))
        };
        Jn.prototype = new pn,
        Jn.prototype.constructor = Jn;
        var Gn = function(e) {
            e = e || {},
            this.default_key_size = parseInt(e.default_key_size) || 1024,
            this.default_public_exponent = e.default_public_exponent || "010001",
            this.log = e.log || !1,
            this.key = null
        };
        Gn.prototype.setKey = function(e) {
            this.log && this.key && console.warn("A key was already set, overriding existing."),
            this.key = new Jn(e)
        }
        ,
        Gn.prototype.setPrivateKey = function(e) {
            this.setKey(e)
        }
        ,
        Gn.prototype.setPublicKey = function(e) {
            this.setKey(e)
        }
        ,
        Gn.prototype.decrypt = function(e) {
            try {
                return this.getKey().decrypt(wn(e))
            } catch (t) {
                return !1
            }
        }
        ,
        Gn.prototype.encrypt = function(e) {
            try {
                return Cn(this.getKey().encrypt(e))
            } catch (t) {
                return !1
            }
        }
        ,
        Gn.prototype.getKey = function(e) {
            if (!this.key) {
                if (this.key = new Jn,
                e && "[object Function]" === {}.toString.call(e))
                    return void this.key.generateAsync(this.default_key_size, this.default_public_exponent, e);
                this.key.generate(this.default_key_size, this.default_public_exponent)
            }
            return this.key
        }
        ,
        Gn.prototype.getPrivateKey = function() {
            return this.getKey().getPrivateKey()
        }
        ,
        Gn.prototype.getPrivateKeyB64 = function() {
            return this.getKey().getPrivateBaseKeyB64()
        }
        ,
        Gn.prototype.getPublicKey = function() {
            return this.getKey().getPublicKey()
        }
        ,
        Gn.prototype.getPublicKeyB64 = function() {
            return this.getKey().getPublicBaseKeyB64()
        }
        ,
        e.JSEncrypt = Gn
    }(passport.lib.RSAExport),
    passport.lib.RSA = passport.lib.RSAExport.JSEncrypt;
    var passport = passport || window.passport || {};
    passport.err = passport.err || {},
    function(e) {
        var t = null;
        t = "function" === (typeof e.getCurrent).toLowerCase() ? e.getCurrent() : {
            errMsg: {},
            labelText: {}
        },
        t.errMsg.login = {
            "-1": {
                msg: '系统错误,请您稍后再试,<a href="http://passport.baidu.com/v2/?ucenterfeedback#{urldata}#login"  target="_blank">帮助中心</a>',
                field: ""
            },
            1: {
                msg: "您输入的帐号格式不正确",
                field: "userName"
            },
            2: {
                msg: '用户名或密码有误，请重新输入或<a href="http://passport.baidu.com/?getpassindex#{urldata}"  target="_blank" >找回密码</a>',
                field: "userName"
            },
            3: {
                msg: "验证码不存在或已过期,请重新输入",
                field: ""
            },
            4: {
                msg: "帐号或密码错误，请重新输入或者<a href='http://passport.baidu.com/?getpassindex#{urldata}'  target='_blank' >找回密码</a>",
                field: "password"
            },
            5: {
                msg: "",
                field: ""
            },
            6: {
                msg: "您输入的验证码有误",
                field: "verifyCode"
            },
            7: {
                msg: "用户名或密码有误，请重新输入或<a href='http://passport.baidu.com/?getpassindex#{urldata}'  target='_blank' >找回密码</a>",
                field: "password"
            },
            16: {
                msg: '您的帐号因安全问题已被限制登录,<a href="http://passport.baidu.com/v2/?ucenterfeedback#{urldata}#login"  target="_blank" >帮助中心</a>',
                field: ""
            },
            257: {
                msg: "请输入验证码",
                field: "verifyCode"
            },
            100027: {
                msg: "百度正在进行系统升级，暂时不能提供服务，敬请谅解",
                field: ""
            },
            120016: {
                msg: "",
                field: ""
            },
            18: {
                msg: "",
                field: ""
            },
            19: {
                msg: "",
                field: ""
            },
            20: {
                msg: "",
                field: ""
            },
            21: {
                msg: "没有登录权限",
                field: ""
            },
            22: {
                msg: "",
                field: ""
            },
            23: {
                msg: "",
                field: ""
            },
            24: {
                msg: "百度正在进行系统升级，暂时不能提供服务，敬请谅解",
                field: ""
            },
            400031: {
                msg: "请在弹出的窗口操作,或重新登录",
                field: ""
            },
            400032: {
                msg: "",
                field: ""
            },
            400034: {
                msg: "",
                field: ""
            },
            401007: {
                msg: "您的手机号关联了其他帐号，请选择登录",
                field: ""
            },
            120021: {
                msg: "登录失败,请在弹出的窗口操作,或重新登录",
                field: ""
            },
            500010: {
                msg: "登录过于频繁,请24小时后再试",
                field: ""
            },
            200010: {
                msg: "验证码不存在或已过期",
                field: ""
            },
            100005: {
                msg: "系统错误,请您稍后再试",
                field: ""
            },
            120019: {
                msg: "请在弹出的窗口操作,或重新登录",
                field: "userName"
            },
            110024: {
                msg: "此帐号暂未激活,<a href='#{gotourl}' >重发验证邮件</a>",
                field: ""
            },
            100023: {
                msg: "开启Cookie之后才能登录,<a href='http://passport.baidu.com/v2/?ucenterfeedback#{urldata}#login'  target='_blank' >如何开启</a>?",
                field: ""
            },
            17: {
                msg: '您的帐号已锁定,请<a href="http://passport.baidu.com/v2/?ucenterfeedback#login_10" target="_blank">解锁</a>后登录',
                field: "userName"
            },
            400401: {
                msg: "",
                field: ""
            },
            400037: {
                msg: "",
                field: ""
            },
            50023: {
                msg: "1个手机号30日内最多换绑3个账号",
                field: ""
            },
            50024: {
                msg: "注册过于频繁，请稍候再试",
                field: ""
            },
            50025: {
                msg: "注册过于频繁，请稍候再试；也可以通过上行短信的方式进行注册",
                field: ""
            },
            50028: {
                msg: '帐号或密码多次输错，请3个小时之后再试或<a href="http://passport.baidu.com/?getpassindex&getpassType=financePwdError#{urldata}"  target="_blank">找回密码</a>',
                field: ""
            },
            50029: {
                msg: '帐号或密码多次输错，请3个小时之后再试或<a href="http://passport.baidu.com/?getpassindex&getpassType=pwdError#{urldata}"  target="_blank">找回密码</a>',
                field: ""
            },
            50030: {
                msg: "抱歉，该手机号的申请次数已达当日上限，请更换手机号",
                field: ""
            },
            50031: {
                msg: "抱歉，该手机号的申请次数已达当月上限，请更换手机号",
                field: ""
            },
            50032: {
                msg: "抱歉，该手机号的申请次数已达本季度上限，请更换手机号",
                field: ""
            },
            400413: {
                msg: "",
                field: ""
            },
            400414: {
                msg: "",
                field: ""
            },
            400415: {
                msg: "帐号存在风险，为了您的帐号安全，请到百度钱包/理财/地图任一APP登录并完成验证，谢谢",
                field: ""
            },
            400500: {
                msg: "您登录的帐号已注销，请登录其他帐号或重新注册",
                field: ""
            },
            72200: {
                msg: "您的帐号因冻结暂时无法登录，请前往冻结时的手机APP，在登录页点击遇到问题进行解冻",
                field: ""
            }
        },
        t.errMsg.checkVerifycode = {
            500002: {
                msg: "您输入的验证码有误",
                field: "verifyCode"
            },
            500018: {
                msg: "验证码已失效，请重试",
                field: "verifyCode"
            }
        },
        t.labelText.login = {
            agree: "阅读并接受",
            baiduUserProtocal: "《百度用户协议》",
            verifyCode: "验证码",
            verifyCodeStaErr: "您输入的验证码有误",
            verifyCodeLenErr: "您输入的验证码有误",
            captcha: "验证码",
            captchaErr: "您输入的动态密码有误,请重试",
            captchaAlt: "验证码图片",
            captchaChange: "换一张",
            memberPassLabel: "下次自动登录",
            login: "登录",
            fgtPwd: "忘记密码？",
            feedback: "帮助中心",
            register: "立即注册",
            phoneNum: "手机号",
            account: "邮箱",
            userName: "手机/邮箱/用户名",
            password: "密码",
            passwordResetWarnNo: '用户名或密码有误，请重新输入或<a href="http://passport.baidu.com/?getpassindex#{urldata}"  target="_blank" >找回密码</a>',
            passwordResetSms: "<a href='javascript:void(0)' onclick='var smDom=document.getElementsByClassName(\"pass-sms-btn\");if(smDom.length>0){smDom[0].click();}' >短信登录\r\n</a>,或者",
            passwordResetWarn: '用户名或密码有误，请重新输入或<a href="http://passport.baidu.com/?getpassindex#{urldata}"  target="_blank" >找回密码</a>',
            passwordResetIn: "个月以内",
            passwordResetOut: "个月以前",
            unameMailLengthError: "邮箱过长,请重新输入",
            unameInputError: "邮箱格式错误,若未绑定邮箱,请使用用户名登录",
            smsPhone: "手机号",
            smsPhoneMsg: "请输入手机号",
            smsVerifyPlaceholder: "验证码",
            smsVerifyCode: "验证码",
            toSmsBtn: "短信快捷登录",
            logining: "登录中...",
            loginsuccess: "登录成功",
            submitTimeup: "登录超时,请稍后再试",
            backToLogin: "用户名密码登录",
            footerBackToLogin: "用户名登录",
            qrcodeTitle: "请使用",
            qrcodeHref: '<a class="pass-link" href="https://mo.baidu.com/wuxian/?from=1019447z" target="new">百度App</a>扫码登录',
            qrcodeMsg: "百度技术加密，保障您的隐私安全",
            qrcodeListaq: "安全",
            qrcodeListgx: "高效",
            qrcodeListbj: "便捷",
            appName: "百度App",
            appHref: "http://xbox.m.baidu.com/mo/",
            sysError: "系统错误，休息一会儿，请稍后再试",
            sysUpdate: "服务正在升级中,请您稍后再试",
            cookieDisable: "开启Cookie之后才能登录,<a href='http://passport.baidu.com/v2/?ucenterfeedback#login'  target='_blank' >如何开启</a>?",
            captchaErr: "动态密码错误",
            confirmVerCodeEmpty: "验证码为空",
            foreignToLogin: "帐号密码登录",
            foreignMobileError: "手机号码格式不正确",
            foreignMobileMsg: "<span>请选择您的国家地区</span>",
            foreignMobileLink: "海外手机号",
            phoenixBtn: "第三方登录",
            qrcodeBtn: "扫码登录",
            QrcodeSuccessTip: "扫描成功",
            QrcodeSuccessMsg: "请在手机端确认登录",
            QrcodeErrorTip: "网络连接失败",
            QrcodeErrorMsg: "请稍候再试",
            QrcodeRefreshTip: "二维码已失效",
            QrcodeRefreshBtn: "点击刷新",
            QrcodeLoadTip: "二维码加载失败"
        },
        e.getCurrent = function() {
            return t
        }
    }(passport.err);
    var passport = passport || window.passport || {};
    passport.data = passport.data || {},
    function(e) {
        function t(e) {
            this._requests = [],
            this._value = null,
            this._exception = null,
            this._isComplete = !1;
            var t = this;
            e(function(e) {
                t._fulfillPromise(e)
            }, function(e) {
                t._breakPromise(e)
            })
        }
        function n(e, t, n) {
            return t ? n ? function(n) {
                return n = n || {},
                l.submit(d + t, i(n, e, g[e], h[e], !0), {
                    charset: "utf-8",
                    processData: function(t) {
                        if (t)
                            for (var n in t)
                                if (t.hasOwnProperty(n)) {
                                    var i = t[n];
                                    i && (t[n] = decodeURIComponent(i))
                                }
                        return s(e, t)
                    }
                })
            }
            : function(n) {
                return l.jsonp(d + t, i(n, e, g[e], h[e], !1), {
                    charset: "utf-8",
                    processData: function(t) {
                        return s(e, t)
                    }
                })
            }
            : a
        }
        function i(e, t, n, i, s) {
            var o = s ? {
                staticpage: _.staticPage,
                charset: _.charset || document.characterSet || document.charset || ""
            } : {}
              , r = f[t];
            if (r)
                for (var a in r) {
                    if (r.hasOwnProperty(a)) {
                        var l = r[a];
                        o[a] = "function" == typeof l ? l(e) : l
                    }
                    "verifypass" == a && (o[a] = decodeURIComponent(o[a]))
                }
            if (o.token = _.token,
            o.tpl = _.product || "",
            o.subpro = _.subpro,
            o.apiver = "v3",
            o.tt = (new Date).getTime(),
            e) {
                n = n || {},
                i = i || {};
                for (var a in e)
                    if (e.hasOwnProperty(a)) {
                        var d = i[a]
                          , u = d ? d(e[a], e) : e[a];
                        "string" == typeof u && (s && (u = decodeURIComponent(u)),
                        m[a] || (u = c.trim(u))),
                        o[n[a] || a.toLowerCase()] = u
                    }
            }
            return o
        }
        function s(t, n) {
            if (e && e.traceID && e.traceID.getTraceID && e.traceID.getTraceID(n),
            n) {
                var i = v[t];
                i && i(n);
                var s = n.errInfo
                  , r = n
                  , a = r;
                return s ? r.errInfo = o(t, s, r) : (s = {
                    no: n.err_no,
                    msg: n.err_msg || ""
                },
                delete r.err_no,
                delete r.err_msg,
                a = {
                    data: r,
                    errInfo: o(t, s, r)
                }),
                a
            }
            return n
        }
        function o(e, t) {
            var n = y[b[e] || e];
            if (n && t && 0 != t.no) {
                var i = n[t.no] || n[-1];
                if (i) {
                    var s = i.msg;
                    t.msg = s,
                    t.field = i.field
                }
            }
            return t
        }
        function r(t) {
            if (e && e.traceID && e.traceID.getTraceID && e.traceID.getTraceID(t),
            t) {
                var n = t.errInfo
                  , i = t;
                if (!n)
                    for (var s in t)
                        if (t.hasOwnProperty(s)) {
                            var o = t[s];
                            o && (t[s] = decodeURIComponent(o))
                        }
                n || (n = {
                    no: t.err_no,
                    msg: t.err_msg || ""
                },
                delete i.err_no,
                delete i.err_msg,
                t = {
                    data: i,
                    errInfo: n
                })
            }
            return t
        }
        var a = function() {};
        t.prototype = {
            get_isComplete: function() {
                return this._isComplete
            },
            get_value: function() {
                if (!this._isComplete)
                    return void 0;
                if (this._exception)
                    throw this._exception;
                return this._value
            },
            call: function(e) {
                for (var t = [], n = 0, i = arguments.length - 1; i > n; n++)
                    t[n] = arguments[n + 1];
                return this.when(function(n) {
                    return n[e].apply(n, t)
                })
            },
            getValue: function(e) {
                return this.when(function(t) {
                    return t[e]
                })
            },
            setValue: function(e, t) {
                this.whenOnly(function(n) {
                    n[e] = t
                })
            },
            when: function(e, n, i) {
                return t.when(this, e, n, i)
            },
            whenOnly: function(e, n, i) {
                t.whenOnly(this, e, n, i)
            },
            success: function(e, t) {
                return this.when(e, a, t)
            },
            fail: function(e, t) {
                return this.when(a, e, t)
            },
            _enqueueOne: function(e) {
                this._isComplete ? this._notify(e) : this._requests.push(e)
            },
            _notify: function(e) {
                this._exception ? e.breakPromise && e.breakPromise(this._exception) : e.fulfillPromise && e.fulfillPromise(this._value)
            },
            _notifyAll: function() {
                for (var e = 0, t = this._requests.length; t > e; e++)
                    this._notify(this._requests[e])
            },
            _fulfillPromise: function(e) {
                this._value = e,
                this._exception = null,
                this._isComplete = !0,
                this._notifyAll()
            },
            _breakPromise: function(e) {
                this._value = null,
                this._exception = e || new Error("An error occured"),
                this._isComplete = !0,
                this._notifyAll()
            }
        },
        t.when = function(e, n, i, s) {
            return new t(function(o, r) {
                t.make(e)._enqueueOne({
                    fulfillPromise: function(e) {
                        o(n ? n.call(s, e) : e)
                    },
                    breakPromise: function(e) {
                        if (i)
                            try {
                                o(i.call(s, e))
                            } catch (t) {
                                r(t)
                            }
                        else
                            r(e)
                    }
                })
            }
            )
        }
        ,
        t.whenOnly = function(e, n, i, s) {
            t.make(e)._enqueueOne({
                fulfillPromise: function(e) {
                    n && n.call(s, e)
                },
                breakPromise: function(e) {
                    i && i.call(s, e)
                }
            })
        }
        ,
        t.make = function(e) {
            return e instanceof t ? e : t.immediate(e)
        }
        ,
        t.immediate = function(e) {
            return new t(function(t) {
                t(e)
            }
            )
        }
        ;
        var c = {};
        !function(e) {
            var t = new RegExp("(^[\\s\\t\\xa0\\u3000]+)|([\\u3000\\xa0\\s\\t]+$)","g");
            e.trim = function(e) {
                return String(e).replace(t, "")
            }
            ,
            e.getUniqueId = function(e) {
                return e + Math.floor(2147483648 * Math.random()).toString(36)
            }
            ,
            e.g = function(e) {
                return e ? "string" == typeof e || e instanceof String ? document.getElementById(e) : !e.nodeName || 1 != e.nodeType && 9 != e.nodeType ? null : e : null
            }
            ,
            e.getParent = function(t) {
                return t = e.g(t),
                t.parentElement || t.parentNode || null
            }
            ,
            e.encodeHTML = function(e) {
                return String(e).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;")
            }
            ,
            e.array = e.array || {},
            e.array.indexOf = function(e, t, n) {
                var i = e.length;
                for (n = 0 | n,
                0 > n && (n = Math.max(0, i + n)); i > n; n++)
                    if (n in e && e[n] === t)
                        return n;
                return -1
            }
            ,
            e.browser = e.browser || {},
            e.browser.opera = /opera(\/| )(\d+(\.\d+)?)(.+?(version\/(\d+(\.\d+)?)))?/i.test(navigator.userAgent) ? +(RegExp.$6 || RegExp.$2) : void 0,
            e.insertHTML = function(t, n, i) {
                t = e.g(t);
                var s, o;
                return t.insertAdjacentHTML && !e.browser.opera ? t.insertAdjacentHTML(n, i) : (s = t.ownerDocument.createRange(),
                n = n.toUpperCase(),
                "AFTERBEGIN" == n || "BEFOREEND" == n ? (s.selectNodeContents(t),
                s.collapse("AFTERBEGIN" == n)) : (o = "BEFOREBEGIN" == n,
                s[o ? "setStartBefore" : "setEndAfter"](t),
                s.collapse(o)),
                s.insertNode(s.createContextualFragment(i))),
                t
            }
        }(c),
        e.base = c;
        var l = {};
        !function(n) {
            var i = "__bdpp_pstc__" + (new Date).getTime()
              , s = i + "_form"
              , o = i + "_ifr"
              , r = function(e) {
                if ("object" == typeof e) {
                    var t = [];
                    for (var n in e) {
                        var i = e[n];
                        if (void 0 !== i && null !== i) {
                            t.length && t.push("&");
                            var s = encodeURIComponent("boolean" == typeof i ? i ? "1" : "0" : i.toString());
                            t.push(encodeURIComponent(n), "=", s)
                        }
                    }
                    return t.join("")
                }
                return "string" == typeof e ? e : null
            }
              , a = function(e, t) {
                if (t = r(t),
                "string" == typeof t) {
                    var n = /\?/g.test(e);
                    e += (n ? "&" : "?") + r(t)
                }
                return e
            }
              , l = function(e, t, n) {
                e.setAttribute("type", "text/javascript"),
                n && e.setAttribute("charset", n),
                e.setAttribute("src", t),
                document.getElementsByTagName("head")[0].appendChild(e)
            }
              , d = function(e) {
                if (e.clearAttributes)
                    e.clearAttributes();
                else
                    for (var t in e)
                        e.hasOwnProperty(t) && delete e[t];
                e && e.parentNode && e.parentNode.removeChild(e),
                e = null
            }
              , u = function(e, t, n) {
                function i(e) {
                    return function() {
                        try {
                            e ? u.onfailure && u.onfailure() : (t.apply(window, arguments),
                            clearTimeout(o)),
                            window[s] = null,
                            delete window[s]
                        } catch (n) {} finally {
                            d(r)
                        }
                    }
                }
                var s, o, r = document.createElement("SCRIPT"), a = "bd__cbs__", u = n || {}, p = u.charset, g = u.queryField || "callback", h = u.timeOut || 0, f = new RegExp("(\\?|&)" + g + "=([^&]*)");
                s = c.getUniqueId(a),
                window[s] = i(0),
                h && (o = setTimeout(i(1), h)),
                e = e.replace(f, "$1" + g + "=" + s),
                e.search(f) < 0 && (e += (e.indexOf("?") < 0 ? "?" : "&") + g + "=" + s),
                l(r, e, p)
            }
              , p = function(e, t) {
                var n = [];
                n.push("<form id='", s, "' target='", o, "' "),
                n.push("action='", c.encodeHTML(e), "' method='post'>");
                for (var i in t)
                    if (t.hasOwnProperty(i)) {
                        var r = t[i];
                        if (void 0 !== r && null !== r) {
                            var a = c.encodeHTML("boolean" == typeof r ? r ? "1" : "0" : r);
                            n.push("<input type='hidden' name='", c.encodeHTML(i), "' value='", a, "' />")
                        }
                    }
                return n.push("</form>"),
                n.join("")
            }
              , g = function(e, t, n, r) {
                function a(e) {
                    return function() {
                        try {
                            e ? r.onfailure && r.onfailure() : (n.apply(window, arguments),
                            d && clearTimeout(d)),
                            window[u] = null,
                            delete window[u]
                        } catch (t) {}
                    }
                }
                r = r || {};
                var l = r.timeOut || 0
                  , d = !1
                  , u = c.getUniqueId("bd__pcbs__");
                t[r.queryField || "callback"] = "parent." + u;
                var g = p(e, t);
                if (c.g(s))
                    c.getParent(s).innerHTML = g;
                else {
                    var h = [];
                    h.push("<div id='", i, "' style='display:none;'>"),
                    h.push("<div>", g, "</div>"),
                    h.push("<iframe name='", o, "' src='" + ("https:" == (window.location ? window.location.protocol.toLowerCase() : document.location.protocol.toLowerCase()) ? "https://passport.baidu.com/passApi/html/_blank.html" : "about:blank") + "' style='display:none;'></iframe>"),
                    h.push("</div>"),
                    c.insertHTML(document.body, "beforeEnd", h.join(""))
                }
                window[u] = a(),
                l && (d = setTimeout(a(1), l)),
                c.g(s).submit()
            };
            n.jsonp = function(n, i, s) {
                return s = s || {},
                e && e.traceID && e.traceID.createTraceID && (i.traceid = e.traceID.createTraceID()),
                new t(function(e, t) {
                    n = a(n, i),
                    u(n, function(t) {
                        s.processData && (t = s.processData(t)),
                        e && e(t)
                    }, {
                        charset: s.charset,
                        queryField: s.queryField,
                        timeOut: s.timeOut,
                        onfailure: function() {
                            t && t()
                        }
                    })
                }
                )
            }
            ,
            n.submit = function(n, i, s) {
                return e && e.traceID && e.traceID.createTraceID && (i.traceid = e.traceID.createTraceID()),
                n && i ? new t(function(e) {
                    g(n, i, function(t) {
                        s.processData && (t = s.processData(t)),
                        e && e(t)
                    }, s)
                }
                ) : void 0
            }
            ;
            var h = [];
            n.load = function(e) {
                return new t(function(t) {
                    var n = h.push(new Image) - 1
                      , i = !1
                      , s = setTimeout(function() {
                        i = !0,
                        t && t()
                    }, 1e3);
                    h[n].onload = function() {
                        clearTimeout(s),
                        i || t && t(),
                        i = !0,
                        h[n] = h[n].onload = null
                    }
                    ,
                    h[n].src = e
                }
                )
            }
        }(l);
        var d = "https://passport.baidu.com"
          , u = {
            getApiInfo: "/v2/api/?getapi",
            getLoginHistory: "/v2/api/?loginhistory",
            loginCheck: "/v2/api/?logincheck",
            getVerifyCodeStr: "/v2/?reggetcodestr",
            getRegSmsVerifyCodeStr: "/v2/?regsmscodestr",
            checkUserName: "/v2/?regnamesugg",
            checkPassword: "/v2/?regpwdcheck",
            checkMail: "/v2/?regmailcheck",
            isUserNoName: "/v2/api/?ucenteradduname",
            checkPhone: "/v2/?regphonecheck",
            getphonestatus: "/v2/?getphonestatus",
            sendPhoneCode: "/v2/?regphonesend",
            multiBind: "/v2/?multiaccountassociate",
            multiUnbind: "/v2/?multiaccountdisassociate",
            multiCheckUserName: "/v2/?multiaccountusername",
            multiGetaccounts: "/v2/?multiaccountget",
            multiSwitchuser: "/v2/?loginswitch",
            checkVerifycode: "/v2/?checkvcode",
            getRsaKey: "/v2/getpublickey",
            authwidGetverify: "/v2/sapi/authwidgetverify",
            checkIDcard: "/v3/finance/main/idnumcert",
            checkIDcardSecondStep: "/v3/finance/main/upcert",
            checkIDcardAllStep: "/v3/finance/main/idnumcert",
            checkIDcardState: "/v3/finance/main/checkupcert"
        }
          , p = {
            login: "/v2/api/?login",
            reg: "/v2/api/?reg",
            fillUserName: "/v2/api/?ucenteradduname",
            regPhone: "/v2/api/?regphone",
            checkIDcard: "/v3/finance/main/idnumcert",
            checkIDcardSecondStep: "/v3/finance/main/upcert",
            checkIDcardAllStep: "/v3/finance/main/idnumcert"
        }
          , g = {
            getApiInfo: {
                apiType: "class"
            },
            login: {
                memberPass: "mem_pass",
                safeFlag: "safeflg",
                isPhone: "isPhone",
                timeSpan: "ppui_logintime",
                logLoginType: "logLoginType"
            },
            fillUserName: {
                selectedSuggestName: "pass_fillinusername_suggestuserradio",
                timeSpan: "ppui_fillusernametime"
            },
            reg: {
                password: "loginpass",
                timeSpan: "ppui_regtime",
                suggestIndex: "suggestIndex",
                suggestType: "suggestType",
                selectedSuggestName: "pass_reg_suggestuserradio_0",
                logRegType: "logRegType"
            },
            regPhone: {
                password: "loginpass",
                timeSpan: "ppui_regtime",
                suggestIndex: "suggestIndex",
                suggestType: "suggestType",
                selectedSuggestName: "pass_reg_suggestuserradio_0",
                logRegType: "logRegType"
            }
        }
          , h = {
            loginCheck: {
                isPhone: function(e) {
                    return e ? "true" : "false"
                }
            },
            login: {
                memberPass: function(e) {
                    return e ? "on" : ""
                }
            }
        }
          , f = {
            checkPassword: {
                fromreg: 1
            },
            reg: {
                registerType: 1,
                verifypass: function(e) {
                    return e.password
                }
            }
        }
          , m = {
            password: !0
        }
          , v = {
            login: function() {}
        }
          , b = {
            checkUserName: "reg",
            checkMail: "reg",
            checkPhone: "regPhone",
            sendPhoneCode: "regPhone",
            multiCheckUserName: "multiBind",
            multiSwitchuser: "changeUser",
            checkVerifycode: "checkVerifycode"
        }
          , y = passport.err.getCurrent().errMsg || passport.err.getCurrent()
          , _ = {};
        e.setContext = function(e) {
            _.product = e.product || _.product,
            _.charset = e.charset || _.charset,
            _.staticPage = e.staticPage || _.staticPage,
            _.token = e.token || _.token,
            _.subpro = e.subpro || _.subpro
        }
        ,
        e.traceID = {
            headID: e.traceID && e.traceID.headID || "",
            flowID: e.traceID && e.traceID.flowID || "",
            cases: e.traceID && e.traceID.cases || "",
            initTraceID: function(e) {
                var t = this;
                e && e.length > 0 ? (t.headID = e.slice(0, 6),
                t.flowID = e.slice(6, 8)) : t.destory()
            },
            createTraceID: function() {
                var e = this;
                return e.headID + e.flowID + e.cases
            },
            startFlow: function(e) {
                var t = this
                  , n = t.getFlowID(e);
                0 === t.flowID.length || t.flowID === n ? (t.createHeadID(),
                t.flowID = n) : t.finishFlow(n)
            },
            finishFlow: function() {
                var e = this;
                e.destory()
            },
            getRandom: function() {
                return parseInt(90 * Math.random() + 10, 10)
            },
            createHeadID: function() {
                var e = this
                  , t = (new Date).getTime() + e.getRandom().toString()
                  , n = Number(t).toString(16)
                  , i = n.length
                  , s = n.slice(i - 6, i).toUpperCase();
                e.headID = s
            },
            getTraceID: function(e) {
                var t = this
                  , n = e && e.traceid || "";
                t.initTraceID(n)
            },
            getFlowID: function(e) {
                var t = {
                    login: "01",
                    reg: "02"
                };
                return t[e]
            },
            setData: function(e) {
                var t = this;
                return e.data ? e.data.traceid = t.createTraceID() : e.url = e.url + (e.url.indexOf("?") > -1 ? "&" : "?") + "traceid=" + t.createTraceID(),
                e
            },
            destory: function() {
                var e = this;
                e.headID = "",
                e.flowID = ""
            }
        };
        for (var E in u)
            u.hasOwnProperty(E) && (e[E] = n(E, u[E]));
        for (var E in p)
            p.hasOwnProperty(E) && (e[E] = n(E, p[E], !0));
        e.jsonp = function(e, t) {
            return 0 != e.indexOf("http") && (e = d + e),
            t = t || {},
            t.flag_code && 1 == t.flag_code || (t.apiver = "v3"),
            t.tt = (new Date).getTime(),
            l.jsonp(e, t, {
                charset: "utf-8",
                processData: function(e) {
                    return r(e)
                }
            })
        }
        ,
        e.post = function(e, t) {
            return t = t || {},
            e = "wap" == t.apitype ? e : d + e,
            t.staticpage = t.staticpage || _.staticPage,
            t.charset = t.charset || _.charset || document.characterSet || document.charset || "",
            t.token = t.token || _.token,
            t.tpl = t.tpl || _.product,
            l.submit(e, t, {
                charset: "utf-8",
                processData: function(e) {
                    return r(e)
                }
            })
        }
        ,
        e.request = l
    }(passport.data);
    var passport = passport || window.passport || {};
    passport.analysis = passport.analysis || {},
    function(e) {
        var t = function(e, t) {
            var n = e.config.diaPassLogin ? "dialogLogin" : "basicLogin"
              , i = e.config.loginMerge ? 1 : 0
              , s = e.config.product || "isnull"
              , o = window.location ? window.location.protocol.toLowerCase() : document.location.protocol.toLowerCase()
              , r = ""
              , a = "&tt=" + (new Date).getTime()
              , c = e.guideRandom ? e.guideRandom : "";
            for (var l in t)
                r = r + "&" + l + "=" + t[l];
            if ("http:" == o)
                var d = "http://nsclick.baidu.com/v.gif?pid=111&url=&logintype=" + n + "&gid=" + c + "&merge=" + i + "&tpl=" + s + r + a;
            else if ("https:" == o)
                var d = "https://passport.baidu.com/img/v.gif?logintype=" + n + "&gid=" + c + "&merge=" + i + "&tpl=" + s + r + a;
            if (d) {
                var u = new Image;
                u.onload = u.onerror = function() {
                    u.onload = u.onerror = null,
                    u = null
                }
                ,
                u.src = d
            }
        };
        e.login = {
            render: function(e) {
                t(e, {
                    type: "firstrender",
                    loginurl: encodeURIComponent(document.location.href)
                }),
                baidu(e.getPhoenixElement("pass_phoenix_list_login")).on("click", function(n) {
                    var i, s = baidu(n.target);
                    if (s && s.attr("title")) {
                        switch (s.attr("title")) {
                        case "普通登录":
                            i = "normal";
                            break;
                        case "二维码登录":
                            i = "qrcode";
                            break;
                        case "短信登录":
                            i = "sms";
                            break;
                        case "QQ帐号":
                            i = "qq";
                            break;
                        case "新浪微博":
                            i = "weibo";
                            break;
                        case "人人网":
                            i = "renren";
                            break;
                        case "腾讯微博":
                            i = "tqq";
                            break;
                        case "飞信":
                            i = "fetion";
                            break;
                        case "微信":
                            i = "weixin";
                            break;
                        case "天翼":
                            i = "tianyi"
                        }
                        t(e, {
                            phoenix: i
                        })
                    }
                });
                var n = (e.getElement(),
                e.getElement("form"));
                baidu(n).on("submit", function() {
                    e.loginfirstsubmit || (e.loginfirstsubmit = !0,
                    t(e, {
                        type: "loginfirstsubmit"
                    }))
                })
            },
            changeLoginType: function(e, n) {
                t(e, {
                    type: "changelogintype",
                    logintype: n && n.loginType || ""
                })
            },
            fieldFocus: function(e, n) {
                n.ele.get(0).id != e.$getId("smsPhone") && n.ele.get(0).id != e.$getId("smsVerifyCode") || e.smsloginfirstlog ? e.loginfirstlog || (e.loginfirstlog = !0,
                t(e, {
                    type: "loginfirst"
                })) : (e.smsloginfirstlog = !0,
                t(e, {
                    type: "smsloginfirst"
                }))
            },
            loginSuccess: function(e) {
                t(e, {
                    type: "loginsuccess"
                })
            },
            loginError: function() {},
            validateError: function(e, n) {
                return n.validate && t(e, {
                    errno: encodeURIComponent(n.validate.msg),
                    type: "loginerrno"
                }),
                {
                    preventEvent: !1,
                    preventDefault: !1
                }
            },
            fieldKeyup: function(e) {
                e.KEYUPFLAG || (t(e, {
                    type: "typein"
                }),
                e.KEYUPFLAG = !0)
            }
        }
    }(passport.analysis);
    var passport = passport || window.passport || {};
    return passport.hook = passport.hook || {},
    function(e) {
        function t(e) {
            var t, n, i = this, s = {
                120016: {
                    isLogin: !1,
                    msg: "您的帐号存在安全风险，我们已经为您采取保护策略，建议您先绑定手机。"
                },
                400032: {
                    isLogin: !0,
                    msg: "快来绑定密保工具吧，提升帐号安全性的同时可以快速找回密码。"
                },
                400034: {
                    isLogin: !1,
                    msg: {
                        phone: "请绑定您的手机号码作为您的密保手机，提升帐号安全性的同时还可以快速找回密码。",
                        email: "请绑定一个您的常用邮箱作为您的密保邮箱，提升帐号安全性的同时还可以快速找回密码。"
                    }
                }
            }[e.errno], o = e.args, r = e.title, a = s.msg, c = (e.auth_title,
            e.auth_msg,
            s.isLogin), l = e.cfg, d = function(e, t, n) {
                var i = t.args
                  , s = {
                    action: t.type || "init",
                    u: e.config.u,
                    tpl: e.config.product,
                    ltoken: i.rsp.data.ltoken,
                    lstr: i.rsp.data.lstr
                };
                e.REQUESTBINDTOKENURL = "/v2/?loginspmbindsecureinfo",
                passport.data.jsonp("https://passport.baidu.com" + e.REQUESTBINDTOKENURL, s).success(function(t) {
                    0 == t.errInfo.no ? n && n({
                        bindEmailToken: t.data.bindEmailToken,
                        bindMobileToken: t.data.bindMobileToken,
                        authsid: t.data.authsid,
                        loginproxy: t.data.loginproxy,
                        otherValue: s
                    }) : alert(e.lang.sysError)
                })
            }, u = function(e) {
                var t = "string" == (typeof a).toLowerCase() ? a : a.email;
                return t += c ? "您可以<a class='bindLink bindJumpEmail'>跳过此步骤</a>或<a class='bindLink bindPhoneBtn'>绑定手机</a>。" : "您也可以<a class='bindLink bindPhoneBtn'>绑定手机</a>。",
                passport.pop.ArmorWidget("bindemail", {
                    token: e.bindEmailToken,
                    authsid: e.authsid,
                    title: r || "绑定密保邮箱",
                    otherValue: e.otherValue,
                    msg: t,
                    subpro: i.config.subpro,
                    traceid: e.traceid,
                    onSubmitSuccess: function(e) {
                        var e = e;
                        d(i, {
                            args: o,
                            type: "check"
                        }, function(t) {
                            e && e.hide && e.hide(),
                            o.isCompleted = !0,
                            t.loginproxy ? passport.data.jsonp(t.loginproxy).success(function(e) {
                                l.onCompleted && l.onCompleted(e, function() {
                                    l.onCancel && l.onCancel(o)
                                })
                            }) : l.onCancel && l.onCancel(o)
                        })
                    },
                    onRender: function() {
                        var e = this;
                        baidu(".bindPhoneBtn").on("click", function() {
                            e.close(),
                            n.show()
                        }),
                        baidu(".bindJumpEmail").on("click", function(t) {
                            t.preventDefault(),
                            e.close(),
                            o.isCompleted = !0,
                            l.onCancel && l.onCancel(o)
                        }),
                        baidu("#" + e.getId("header_a")).on("click", function() {
                            c && (o.isCompleted = !0,
                            l.onCancel && l.onCancel(o))
                        })
                    }
                })
            }, p = function(e) {
                var n = "string" == (typeof a).toLowerCase() ? a : a.phone;
                return c && e.bindEmailToken ? n += "您可以<a class='bindLink bindJumpPhone'>跳过此步骤</a>或<a class='bindLink bindEmailBtn'>绑定密保邮箱</a>。" : e.bindEmailToken && (n += "您也可以<a class='bindLink bindEmailBtn'>绑定密保邮箱</a>。"),
                passport.pop.ArmorWidget("bindmobile", {
                    token: e.bindMobileToken,
                    authsid: e.authsid,
                    title: r || "绑定手机",
                    otherValue: e.otherValue,
                    msg: n,
                    bindToLogin: 1,
                    apiMargicInstance: i,
                    subpro: i.config.subpro,
                    traceid: e.traceid,
                    onSubmitSuccess: function(e) {
                        var e = e;
                        d(i, {
                            args: o,
                            type: "check"
                        }, function(t) {
                            e && e.hide && e.hide(),
                            o.isCompleted = !0,
                            t.loginproxy ? passport.data.jsonp(t.loginproxy).success(function(e) {
                                l.onCompleted && l.onCompleted(e, function() {
                                    l.onCancel && l.onCancel(o)
                                })
                            }) : l.onCancel && l.onCancel(o)
                        })
                    },
                    onRender: function(n) {
                        var n = this;
                        baidu(".bindEmailBtn").on("click", function(i) {
                            i.preventDefault(),
                            n.close(),
                            t = t || u(e),
                            t.show()
                        }),
                        baidu(".bindJumpPhone").on("click", function(e) {
                            e.preventDefault(),
                            n.close(),
                            o.isCompleted = !0,
                            l.onCancel && l.onCancel(o)
                        }),
                        baidu("#" + n.getId("header_a")).on("click", function() {
                            c && (o.isCompleted = !0,
                            l.onCancel && l.onCancel(o))
                        })
                    },
                    onBindToLoginFn: function(e, t) {
                        t && t.mobile && (i.config.sms ? (i.getElement("smsPhone_placeholder") && i.$hide("smsPhone_placeholder"),
                        i.getElement("smsPhone") && (i.getElement("smsPhone").value = t.mobile),
                        i.getElement("smsVerifyCode") && (i.getElement("smsVerifyCode").value = "",
                        i.getElement("smsVerifyCode").focus())) : (i.getElement("userName_placeholder") && i.$hide("userName_placeholder"),
                        i.getElement("userName") && (i.getElement("userName").value = t.mobile),
                        i.getElement("password") && (i.getElement("password").value = "",
                        i.getElement("password").focus())))
                    }
                })
            };
            d(i, {
                args: o,
                type: "init"
            }, function(e) {
                passport._use(C, y[C], function() {
                    e.bindMobileToken ? (n = p(e),
                    n.show()) : e.bindEmailToken ? (t = u(e),
                    t.show()) : alert(i.lang.sysError)
                })
            })
        }
        function n(e) {
            var t, n, i = this, s = e.rspData, o = e.cfg, r = e.args, a = function(e) {
                var e = e || "系统检测到您的帐号疑似被盗，存在安全风险。请尽快修改密码。";
                return '<div class="passport-forceverify-risk"><p class="passport-forceverify-risk-msg">' + e + '</p><div  class="passport-forceverify-risk-con clearfix"><a class="passport-forceverify-risk-next" id="passport_forceverify_risk_next" href="###">下次提醒</a><a class="passport-forceverify-risk-btn" href="http://passport.baidu.com/v2/account/password" target="_blank" >立即修改</a></div></div>'
            };
            if (s && s.secstate)
                switch (s.secstate) {
                case "PA001":
                    n = "您的帐号密码输入错误次数达到上限，为保障帐号安全，登录前需验证身份。";
                    break;
                case "PA002":
                    n = "您的网络环境存在安全风险，为保障帐号安全，登录前需验证身份。";
                    break;
                case "PA003":
                    n = "您的帐号长时间未登录，为保障帐号安全，登录前需验证身份。";
                    break;
                case "risk":
                    t = a(),
                    n = "您的帐号可能存在安全隐患，为保障您的帐号安全，登录前需验证身份。";
                    break;
                case "cheat":
                    n = "您的帐号因批量或者使用非法软件注册被冻结，登录前需验证身份。";
                    break;
                case "PC001":
                    n = "您操作频度过于频繁，为保障帐号安全，登录前需验证身份。";
                    break;
                case "PX008":
                    n = "您本次的登录地存在异常，为保障本次操作安全，登录前需验证身份。";
                    break;
                default:
                    n = "您的帐号存在安全风险，为保障帐号安全，登录前需验证身份。"
                }
            var c = {
                400031: {
                    title: "登录保护",
                    msg: "您已开启登录保护功能，为保障帐号安全，登录前需验证身份。"
                },
                5: {
                    title: "登录安全验证",
                    msg: "您的网络环境存在安全风险，为保障帐号安全，登录前需验证身份。",
                    onSuccess: function(e, t) {
                        var n = s.gotourl + "&authsid=" + t.authsid;
                        passport.data.jsonp(n).success(function(t) {
                            i._ownerDialog && i._ownerDialog.show(),
                            e.hide(),
                            i.getElement("error").innerHTML = 0 == t.errInfo.no || 0 == t.data.errno ? '请重新登录，或<a href="https://passport.baidu.com/?getpass_index" target="_blank">找回密码</a>' : i.lang.sysError
                        })
                    },
                    onGetapiError: function() {
                        i.getElement("error").innerHTML = "您所处的网络存在安全风险，请切换网络重试"
                    }
                },
                400023: {
                    title: "登录安全验证",
                    msg: "您的网络环境存在安全风险，为保障帐号安全，登录前需验证身份。",
                    onSuccess: function(e, t) {
                        var n = "https://passport.baidu.com/v3/login/main/qrbdusslogin?tt=" + (new Date).getTime()
                          , a = {
                            authsid: t.authsid,
                            bduss: s.bdusssign,
                            u: encodeURIComponent(s.u),
                            loginVersion: "v4",
                            tpl: i.config.product
                        };
                        passport.data.jsonp(n, a).success(function(t) {
                            e.hide(),
                            0 == t.errInfo.no || 0 == t.data.errno ? (r.isCompleted = !0,
                            o.onCompleted && o.onCompleted(t, function() {
                                o.onCancel && o.onCancel(r)
                            })) : i.getElement("error").innerHTML = i.lang.sysError
                        })
                    },
                    onGetapiError: function() {
                        i.getElement("error").innerHTML = "您所处的网络存在安全风险，请切换网络重试"
                    }
                },
                120019: {
                    title: "登录解冻验证",
                    msg: "您的帐号因密码输入错误次数过多，为保障帐号安全，登陆前需验证身份。",
                    onSuccess: function(e, t) {
                        var n = s.gotourl + "&authsid=" + t.authsid;
                        passport.data.jsonp(n).success(function(t) {
                            i._ownerDialog && i._ownerDialog.show(),
                            e.hide(),
                            i.getElement("error").innerHTML = 0 == t.errInfo.no || 0 == t.data.errno ? '请重新登录，或<a href="https://passport.baidu.com/?getpass_index" target="_blank">找回密码</a>' : i.lang.sysError
                        })
                    },
                    onGetapiError: function() {
                        i.getElement("error").innerHTML = '登录密码错误已达上限，您可以<a href="https://passport.baidu.com/?getpass_index" target="_blank">找回密码</a>或3小时后再试'
                    }
                },
                120021: {
                    title: "安全验证",
                    msg: n,
                    defaultHTML: t,
                    onSuccess: function(e) {
                        return passport.data.jsonp(s.loginproxy).success(function(n) {
                            e.show(),
                            0 == n.errInfo.no ? (r.isCompleted = !0,
                            t ? (e.getElement("article").innerHTML = t,
                            baidu(e.getElement("header_a")).on("click", function() {
                                e.hide(),
                                o.onCompleted && o.onCompleted(n, function() {
                                    o.onCancel && o.onCancel(r)
                                })
                            }),
                            baidu(document.getElementById("passport_forceverify_risk_next")).on("click", function() {
                                e.hide(),
                                o.onCompleted && o.onCompleted(n, function() {
                                    o.onCancel && o.onCancel(r)
                                })
                            })) : (e.hide(),
                            o.onCompleted && o.onCompleted(n, function() {
                                o.onCancel && o.onCancel(r)
                            }))) : alert(i.lang.sysError)
                        }),
                        !1
                    },
                    onRender: function(e) {
                        document.getElementById("passport_forceverify_risk_appeal") && (document.getElementById("passport_forceverify_risk_appeal").href = e.url_forgot)
                    }
                },
                riskCheat: {
                    token: "risk",
                    title: "安全验证",
                    msg: n,
                    defaultHTML: t,
                    onRender: function(e) {
                        baidu(document.getElementById("passport_forceverify_risk_next")).on("click", function() {
                            e.hide(),
                            o.onCancel && o.onCancel()
                        }),
                        document.getElementById("passport_forceverify_risk_appeal") && (document.getElementById("passport_forceverify_risk_appeal").href = e.url_forgot)
                    }
                }
            }[e.errno];
            passport._use(E, y[E], function() {
                forceverifyLoginverify = passport.pop.Forceverify({
                    token: s.authtoken,
                    title: c.title,
                    msg: c.msg,
                    subpro: i.config.subpro,
                    u: s.u || "",
                    lstr: s.lstr || "",
                    ltoken: s.ltoken || "",
                    tpl: s.tpl || "",
                    traceid: s.traceid,
                    onRender: function(e) {
                        c.onRender && c.onRender(e)
                    },
                    onSubmitSuccess: function(e, t) {
                        if ("1" === s.realnameverifyemail)
                            return s.realnameauthsid = t.authsid,
                            void d.apply(i, [{
                                args: r,
                                rspData: s,
                                cfg: o
                            }]);
                        if (c.onSuccess)
                            return void c.onSuccess(e, t);
                        var n = s.loginproxy;
                        passport.data.jsonp(n).success(function(t) {
                            0 == t.errInfo.no || 0 == t.data.errno ? (e.hide(),
                            r.isCompleted = !0,
                            o.onCompleted && o.onCompleted(t, function() {
                                o.onCancel && o.onCancel(r)
                            })) : (e.hide(),
                            i._ownerDialog && i._ownerDialog.show(),
                            i.getElement("error").innerHTML = i.lang.sysError)
                        })
                    },
                    onGetapiError: function(e) {
                        return i._ownerDialog && i._ownerDialog.show(),
                        c.onGetapiError ? void c.onGetapiError(e) : void (i.getElement("error").innerHTML = i.lang.sysError)
                    },
                    onHide: function() {
                        o.onCancel && o.onCancel(),
                        i.config.loginMerge && i.getElement("isPhone") && (i.getElement("isPhone").value = "")
                    }
                }, !0)
            })
        }
        function i(e) {
            for (var t = this, n = e.rspData, i = [], s = n.accounts.split(";"), o = 0; o < s.length; o++) {
                var r = s[o].split(",");
                i.push({
                    username: r[0],
                    portrait: r[1]
                })
            }
            passport._load(b + y[_], !0, function() {
                var e = passport.pop.init({
                    type: "loginMultichoice",
                    tangram: !0,
                    apiOpt: {
                        phone: n.userName,
                        userList: i
                    },
                    onChoicedUser: function(n, i) {
                        e.hide(),
                        t._ownerDialog && t._ownerDialog.show(),
                        t.getElement("userName").value = i.username,
                        t.getElement("isPhone").value = "false",
                        t.config.loginMerge && t.getElement("loginMerge") && (t.getElement("loginMerge").value = ""),
                        "sms" == t.currentLoginType ? (t.getElement("smsHiddenFields_switchuname").value = i.username,
                        t._submitSmsForm()) : (t.config.loginMerge || (t._collectData(),
                        t.switchTo("normal"),
                        t._restoreData("phone")),
                        t.submit())
                    },
                    onHide: function() {
                        t.getElement("userName").value = n.userName,
                        t.getElement("isPhone").value = ""
                    }
                });
                e.show()
            })
        }
        function s(e) {
            var t = this
              , n = t.$getId("pass_b2c_swf")
              , i = e.args.rsp.data
              , s = T()
              , o = 0;
            i && i.bckv && (o = parseInt(i.bckv, 10) > 0);
            var r = null;
            if (passport.CONSTANT = passport.CONSTANT || {},
            passport.CONSTANT.b2c_getlogin = function() {}
            ,
            passport.CONSTANT.b2c_setlogin = function() {
                var e = {
                    kv: i.bckv,
                    sync: i.bcsync,
                    checksum: i.bcchecksum,
                    time: i.bctime
                };
                try {
                    if (r) {
                        var t = r.get_movie(n, "b2c_setlogin").b2c_setlogin(e);
                        try {
                            var s = document.createElement("script");
                            s.type = "text/javascript",
                            s.src = [b, "/v2/b2c-stable?", "from=setlogin.done", "&checksum=", e.checksum, "&time=", e.time, "&status=", encodeURIComponent(t)].join(""),
                            document.getElementsByTagName("head")[0].appendChild(s)
                        } catch (o) {}
                    }
                } catch (o) {
                    try {
                        var s = document.createElement("script");
                        s.type = "text/javascript",
                        s.src = [b, "/v2/b2c-stable?", "from=setlogin.fail", "&msg=", encodeURI(o.message)].join(""),
                        document.getElementsByTagName("head")[0].appendChild(s)
                    } catch (o) {}
                }
            }
            ,
            t.getElement("pass_b2c") && s.isexists && o) {
                var a = function(e) {
                    var t = function(e) {
                        e = e || {};
                        var t, n, i, s, o = {}, r = function(e) {
                            return e.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;")
                        };
                        for (n in e)
                            o[n] = e[n];
                        e = o;
                        var a = e.vars
                          , c = ["classid", "codebase", "id", "width", "height", "align"];
                        if (e.align = e.align || "middle",
                        e.classid = "clsid:d27cdb6e-ae6d-11cf-96b8-444553540000",
                        e.codebase = "https://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0",
                        e.movie = e.url || "",
                        delete e.vars,
                        delete e.url,
                        "string" == typeof a)
                            e.flashvars = a;
                        else {
                            var l = [];
                            for (n in a)
                                s = a[n],
                                l.push(n + "=" + encodeURIComponent(s));
                            e.flashvars = l.join("&")
                        }
                        var d = ["<object "];
                        for (t = 0,
                        i = c.length; i > t; t++)
                            s = c[t],
                            d.push(" ", s, '="', r(e[s]), '"');
                        d.push(">");
                        var u = {
                            wmode: 1,
                            scale: 1,
                            quality: 1,
                            play: 1,
                            loop: 1,
                            menu: 1,
                            salign: 1,
                            bgcolor: 1,
                            base: 1,
                            allowscriptaccess: 1,
                            allownetworking: 1,
                            allowfullscreen: 1,
                            seamlesstabbing: 1,
                            devicefont: 1,
                            swliveconnect: 1,
                            flashvars: 1,
                            movie: 1
                        };
                        for (n in e)
                            s = e[n],
                            n = n.toLowerCase(),
                            u[n] && (s || s === !1 || 0 === s) && d.push('<param name="' + n + '" value="' + r(s) + '" />');
                        e.src = e.movie,
                        e.name = e.id,
                        delete e.id,
                        delete e.movie,
                        delete e.classid,
                        delete e.codebase,
                        e.type = "application/x-shockwave-flash",
                        e.pluginspage = "https://www.macromedia.com/go/getflashplayer",
                        d.push("<embed");
                        var p;
                        for (n in e)
                            if (s = e[n],
                            s || s === !1 || 0 === s) {
                                if (new RegExp("^salign$","i").test(n)) {
                                    p = s;
                                    continue
                                }
                                d.push(" ", n, '="', r(s), '"')
                            }
                        return p && d.push(' salign="', r(p), '"'),
                        d.push("></embed></object>"),
                        d.join("")
                    }
                      , n = function(e) {
                        e = e || {};
                        var n = document.createElement("div");
                        n.innerHTML = t(e),
                        n.style.display = "none",
                        document.getElementsByTagName("body")[0].appendChild(n)
                    }
                      , i = /msie (\d+\.\d+)/i.test(navigator.userAgent) ? document.documentMode || +RegExp.$1 : void 0;
                    return (i > 7 || !i) && n(e),
                    {
                        get_movie: function(e, t) {
                            var n = document[e];
                            if (9 === document.documentMode && n && n.length)
                                for (var i = n.length, s = 0; i > s; s++) {
                                    var o = n[s];
                                    if ("embed" === o.tagName.toLowerCase()) {
                                        n = o;
                                        break
                                    }
                                }
                            return t && "function" != typeof n[t] && (n = document.getElementById(e)),
                            n
                        }
                    }
                };
                try {
                    var c = window.location.protocol.toLowerCase();
                    r = a({
                        id: n,
                        width: "1",
                        height: "1",
                        url: c + "//passport.baidu.com/passApi/swf/b2c.swf?_t=" + Math.random(),
                        allowscriptaccess: "always"
                    })
                } catch (l) {}
            }
            passport.data.request.load(b + "/v2/b2c-flash?isexists=" + encodeURIComponent(s.isexists) + "&ver=" + encodeURIComponent(s.ver) + "&filename=" + encodeURIComponent(s.filename))
        }
        function o(e) {
            var t = this
              , n = e.rspData
              , i = e.args.rsp.data;
            return t.rebindGuideWidget ? void t.rebindGuideWidget.show() : void passport.use("uni_rebindGuide", {
                tangram: !0
            }, function() {
                t.rebindGuideWidget = new passport.pop.rebindGuideWidget({
                    color: t.config.color || "blue",
                    apiOpt: i,
                    rebindType: "rebindPhone",
                    onrebindGuideCompleted: function() {
                        S(t, n)
                    }
                }),
                t.rebindGuideWidget.show()
            })
        }
        function r(e) {
            var t = this
              , n = e.cfg
              , i = e.args
              , s = e.rspData.rsp.data || {};
            passport._load(b + y[_], !0, function() {
                h ? (h.setMakeOption && h.setMakeOption(s.authsid, s.bdstoken),
                h.show()) : (h = passport.pop.init({
                    type: "accSetPwd",
                    tangram: !0,
                    color: t.config.color || "blue",
                    apiOpt: {
                        u: t.config.u,
                        product: t.config.product,
                        authsid: s.authsid || "",
                        bdstoken: s.bdstoken || "",
                        staticPage: t.config.staticPage
                    },
                    onHide: function() {
                        "1" != s.setpwdswitch && (i.isCompleted = !0,
                        n.onCancel && n.onCancel(i))
                    },
                    onSubmitSuccess: function() {
                        i.isCompleted = !0,
                        i && i.rsp && i.rsp.errInfo && (i.rsp.errInfo.no = "0"),
                        s.hao123Param && D(s.hao123Param, t),
                        h.hide(),
                        n.onCancel && n.onCancel(i)
                    }
                }),
                h.show())
            })
        }
        function a(e) {
            var t = this
              , n = e.cfg
              , i = e.args
              , s = e.rspData.rsp.data || {};
            passport._load(b + y[_], !0, function() {
                f ? (f.setMakeOption && f.setMakeOption(s.authsid, s.bdstoken),
                f.show()) : (f = passport.pop.init({
                    type: "accSetPwd",
                    tangram: !0,
                    color: t.config.color || "blue",
                    jumpset: "1" == s.jumpset ? 1 : 0,
                    apiOpt: {
                        u: t.config.u,
                        product: t.config.product,
                        authsid: s.authsid || "",
                        bdstoken: s.bdstoken || "",
                        username: 1,
                        staticPage: t.config.staticPage
                    },
                    onHide: function() {
                        "1" == s.jumpset && (i.isCompleted = !0,
                        n.onCancel && n.onCancel(i))
                    },
                    onSubmitSuccess: function() {
                        i.isCompleted = !0,
                        i && i.rsp && i.rsp.errInfo && (i.rsp.errInfo.no = "0"),
                        s.hao123Param && D(s.hao123Param, t),
                        f.hide(),
                        n.onCancel && n.onCancel(i)
                    }
                }),
                f.show())
            })
        }
        function c(e) {
            var t = this
              , n = e.cfg
              , i = e.args
              , s = e.rspData.rsp.data || {}
              , o = "400413" === i.rsp.errInfo.no && "sms" === e.rspData.rsp.loginType ? "1" : "0";
            passport._load(b + y[_], !0, function() {
                v ? (v.reRender && v.reRender({
                    lstr: s.lstr || "",
                    ltoken: s.ltoken || "",
                    token: s.authtoken || "",
                    loginproxy: s.loginproxy || "",
                    select: o,
                    loginType: e.rspData.rsp.loginType
                }),
                v.show()) : (v = passport.pop.init({
                    type: "secondCardVerify",
                    tangram: !0,
                    color: t.config.color || "blue",
                    apiOpt: {
                        u: t.config.u,
                        product: t.config.product,
                        lstr: s.lstr || "",
                        ltoken: s.ltoken || "",
                        token: s.authtoken || "",
                        staticPage: t.config.staticPage,
                        select: o,
                        loginType: e.rspData.rsp.loginType,
                        loginproxy: s.loginproxy || ""
                    },
                    onloginSuccess: function() {
                        i.isCompleted = !0,
                        i && i.rsp && i.rsp.errInfo && (i.rsp.errInfo.no = "0"),
                        s.hao123Param && D(s.hao123Param, t),
                        v.hide(),
                        n.onCancel && n.onCancel(i)
                    },
                    onSubmitSuccess: function(e, n) {
                        n.rsp.data.loginproxy && passport.data.jsonp(n.rsp.data.loginproxy).success(function(e) {
                            "0" === e.errInfo.no ? document.location.href = "https://passport.baidu.com/v3/security/main/secondcardmodifyaccinfo?tpl=" + t.config.product + "&bdstoken=" + n.rsp.data.bdstoken + "&authsid=" + n.rsp.data.mod_authsid + "&u=" + encodeURIComponent(e.data.u) + "&loginType=" + n.rsp.data.loginType + "&hasUsername=" + n.rsp.data.hasUsername : alert(t.lang.sysError)
                        })
                    }
                }),
                v.show())
            })
        }
        function l(e) {
            var t = this;
            e.rspData = e.rspData || {},
            passport._load(b + y[w], !0, function() {
                m ? m.setToken(e.rspData.token, function() {
                    m.show()
                }) : (m = passport.pop.init({
                    type: "accConnect",
                    tangram: !0,
                    color: t.config.color || "",
                    apiOpt: {
                        u: t.config.u,
                        adtext: e.rspData.adtext,
                        product: t.config.product,
                        token: e.rspData.token,
                        staticPage: t.config.staticPage
                    },
                    onConnectSuccess: function(e) {
                        var n = e.rsp;
                        n.connect = m,
                        S(t, {
                            rsp: n
                        }),
                        e.returnValue = !1
                    }
                }),
                m.show())
            })
        }
        function d(e) {
            var t = this
              , n = e.cfg
              , i = e.args;
            e.rspData = e.rspData || {},
            passport._load(b + y[_], !0, function() {
                g ? g.show() : (g = passport.pop.init({
                    type: "accRealName",
                    tangram: !0,
                    color: t.config.color || "",
                    apiOpt: {
                        u: t.config.u,
                        product: t.config.product,
                        staticPage: t.config.staticPage,
                        action: "login",
                        realnameswitch: e.rspData.realnameswitch,
                        authsid: e.rspData.realnameauthsid,
                        ltoken: e.rspData.ltoken,
                        lstr: e.rspData.lstr,
                        cu: e.rspData.u,
                        overseas: t.config.overseas
                    },
                    onHide: function() {
                        t.fire("RealHide", i),
                        "1" != e.rspData.realnameswitch && (i.isCompleted = !0,
                        n.onCancel && n.onCancel(i))
                    },
                    onverifyHide: function(s) {
                        t.realLoginHide || (e.rspData.loginproxy && s ? passport.data.jsonp(e.rspData.loginproxy + "&authsid=" + s).success(function(e) {
                            0 == e.errInfo.no ? (i.isCompleted = !0,
                            n.onCompleted && n.onCompleted(e, function() {
                                n.onCancel && n.onCancel(i)
                            })) : alert(t.lang.sysError)
                        }) : (i.isCompleted = !0,
                        e.rspData.hao123Param && "1" == e.rspData.realnameswitch && D(e.rspData.hao123Param, t),
                        n.onCancel && n.onCancel(i)))
                    },
                    onSubmitSuccess: function(s, o) {
                        e.rspData.loginproxy && o.rsp.data.authsid ? passport.data.jsonp(e.rspData.loginproxy + "&authsid=" + o.rsp.data.authsid).success(function(e) {
                            0 == e.errInfo.no ? (i.isCompleted = !0,
                            t.realLoginHide = !0,
                            g.hide(),
                            n.onCompleted && n.onCompleted(e, function() {
                                n.onCancel && n.onCancel(i)
                            })) : alert(t.lang.sysError)
                        }) : (i.isCompleted = !0,
                        i && i.rsp && i.rsp.errInfo && (i.rsp.errInfo.no = "0"),
                        e.rspData.hao123Param && "1" == e.rspData.realnameswitch && D(e.rspData.hao123Param, t),
                        t.realLoginHide = !0,
                        g.hide(),
                        n.onCancel && n.onCancel(i))
                    }
                }),
                g.show())
            })
        }
        function u(e, s, u) {
            function g(t) {
                var n = new Image;
                n.onload = n.onerror = function() {
                    n.onload = n.onerror = null,
                    n = null
                }
                ,
                n.src = b + "/img/v.gif?type=" + t + "&tt=" + (new Date).getTime(),
                s.isCompleted = !0,
                f.hao123Param && D(f.hao123Param, e),
                y.confirmWidgetMobileSure.hide(),
                u.onCancel && u.onCancel(s)
            }
            var h = s.rsp.errInfo.no
              , f = s.rsp.data
              , u = u || {}
              , m = f && ("risk" == f.secstate || "cheat" == f.secstate);
            if (f && f.connectType && e.config.connect) {
                var v = e.fire("beforeWarning", {
                    args: s
                });
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                p(b + "/passApi/css/uni_accConnect_ab6dda9.css"),
                l.apply(e, [{
                    args: s,
                    rspData: f,
                    cfg: u,
                    errno: h
                }]),
                !1
            }
            if (18 == h)
                return e.getElement("error").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                d.apply(e, [{
                    args: s,
                    rspData: f,
                    cfg: u,
                    errno: h
                }]),
                f.hao123Param && "1" != f.realnameswitch && D(f.hao123Param, e),
                !1;
            if (20 == h) {
                var v = e.fire("beforeWarning", s);
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e.getElement("smsError").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                r.apply(e, [{
                    args: s,
                    rspData: s,
                    cfg: u
                }]),
                f.hao123Param && "1" != f.setpwdswitch && D(f.hao123Param, e),
                !1
            }
            if (22 == h) {
                var v = e.fire("beforeWarning", s);
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e.getElement("smsError").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                a.apply(e, [{
                    args: s,
                    rspData: s,
                    cfg: u
                }]),
                f.hao123Param && D(f.hao123Param, e),
                !1
            }
            if ("400413" === h || "400414" === h) {
                var v = e.fire("beforeWarning", s);
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e.getElement("smsError").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                c.apply(e, [{
                    args: s,
                    rspData: s,
                    cfg: u
                }]),
                f.hao123Param && D(f.hao123Param, e),
                !1
            }
            if (19 == h) {
                var y = this
                  , f = s.rsp.data
                  , v = e.fire("beforeWarning", s);
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                null == y.confirmWidgetLabel ? passport._load(b + "/passApi/js/uni_wrapper.js", !0, function() {
                    y.confirmWidgetLabel = passport.pop.init({
                        type: "confirmWidget",
                        tangram: !0,
                        width: 430,
                        height: 150,
                        apiOpt: {
                            contentHTML: "                                        <div class='pass-confirmContent-wrapper-Label'>                                            <div class='pass-confirmContent-msg-Label'><span class='img-class' ></span></div>                                            <ul  class='pass-confirmContent-descmsg-Label' style='margin-left:20px;'>                                                <p>近日，某邮箱帐户存在被破解的可能性，建议您使用其他</p>                                                <p>邮箱绑定百度帐号，或及时修改您的百度帐号登陆密码并</p>                                                <p>绑定手机，以确保帐户安全。</p>                                            </ul>                                        </div>"
                        },
                        onConfirmClose: function() {
                            y.confirmWidgetLabel.hide(),
                            S(e, s)
                        },
                        onRender: function() {
                            y.confirmWidgetLabel.getElement("confirm_cancel").style.display = "none",
                            y.confirmWidgetLabel.getElement("confirm_continue").style.display = "none",
                            y.confirmWidgetLabel.getElement("confirmWidget_footer").style.display = "none"
                        }
                    }),
                    y.confirmWidgetLabel.show()
                }) : y.confirmWidgetLabel.show(),
                f.hao123Param && D(f.hao123Param, e),
                !1
            }
            if (23 == h) {
                var y = this
                  , f = s.rsp.data
                  , v = e.fire("beforeWarning", s);
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                null == y.confirmWidgetMobileSure ? passport._load(b + "/passApi/js/uni_wrapper.js", !0, function() {
                    y.confirmWidgetMobileSure = passport.pop.init({
                        type: "confirmWidget",
                        tangram: !0,
                        titleText: "非常重要",
                        width: 430,
                        apiOpt: {
                            Cancel: "不需要解绑",
                            Continue: "申诉去解绑",
                            contentHTML: '<div class="pass-confirmContent-wrapper-sureConfirm"><div class="pass-confirmContent-wrapper-msg"><p><span class="pass-confirmContent-redcolor" id="pass-mobile-sure-num">' + f.phoneNumber + '</span>是您绑定的手机号,请确认该手机号是否还在使用,为了帐号安全请及时解绑不使用的手机。</p></div><div class="pass-confirmwidget-bottom"><span id="pass-mobile-sure-btn" class="pass-button pass-button-grey cancel">不需要解绑</span><a href="' + f.appealurl + '" id="pass-appeal-btn" class="pass-button pass-button-grey continue" target="new">申诉去解绑</a></div></div>'
                        },
                        onRender: function() {
                            y.confirmWidgetMobileSure.getElement("confirm_cancel").style.display = "none",
                            y.confirmWidgetMobileSure.getElement("confirm_continue").style.display = "none",
                            y.confirmWidgetMobileSure.getElement("confirmWidget_footer").style.display = "none",
                            baidu(document.getElementById("pass-mobile-sure-btn")).on("click", function() {
                                g("mobileSurePC")
                            }),
                            baidu(document.getElementById("pass-appeal-btn")).on("click", function() {
                                g("appealMobilePC")
                            })
                        },
                        onConfirmClose: function() {
                            g("mobileSureClosePC")
                        },
                        onConfirmContinue: function() {},
                        onConfirmCancel: function() {}
                    }),
                    y.confirmWidgetMobileSure.show()
                }) : (document.getElementById("pass-mobile-sure-num") && (document.getElementById("pass-mobile-sure-num").html = f.phoneNumber || ""),
                y.confirmWidgetMobileSure.show()),
                f.hao123Param && D(f.hao123Param, e),
                !1
            }
            if (401007 == h) {
                var v = e.fire("beforeWarning", s);
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                i.apply(e, [{
                    rspData: f
                }]),
                !1
            }
            if (120016 == h || 400032 == h || 400034 == h) {
                var v = e.fire("beforeWarning", s);
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                t.apply(e, [{
                    errno: h,
                    args: s,
                    cfg: u
                }]),
                f.hao123Param && D(f.hao123Param, e),
                !1
            }
            if (5 == h || 400031 == h || 120019 == h || 120021 == h || 400023 == h || m) {
                var v = e.fire("beforeWarning", {
                    args: s
                });
                if (!v)
                    return;
                return e.getElement("error") && (e.getElement("error").innerHTML = ""),
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                p(b + "/passApi/css/uni_forceverify_38dd002.css"),
                n.apply(e, [{
                    args: s,
                    rspData: f,
                    cfg: u,
                    errno: m && 120021 != h ? "riskCheat" : h
                }]),
                !1
            }
            if (400037 == h) {
                var v = e.fire("beforeWarning", s);
                if (!v)
                    return;
                return e.getElement("error").innerHTML = "",
                e._ownerDialog && e._ownerDialog.hide("unHide"),
                o.apply(e, [{
                    args: s,
                    rspData: s,
                    cfg: u
                }]),
                f.hao123Param && D(f.hao123Param, e),
                !1
            }
            return !0
        }
        function p(e) {
            if (!I[e]) {
                I[e] = !0;
                var t = document.createElement("link");
                t.rel = "stylesheet",
                t.type = "text/css",
                t.href = e,
                document.getElementsByTagName("head")[0].appendChild(t)
            }
            return !0
        }
        var g, h, f, m, v, b = window.location ? "http:" == window.location.protocol.toLowerCase() ? "http://passport.baidu.com" : "https://passport.baidu.com" : "http:" == document.location.protocol.toLowerCase() ? "http://passport.baidu.com" : "https://passport.baidu.com", y = {
            uni_armorwidget: "/passApi/js/uni_armorwidget_800b8d9.js",
            uni_forceverify: "/passApi/js/uni_forceverify_c9f5636.js",
            uni_accConnect: "/passApi/js/uni_accConnect_wrapper.js",
            uni_wrapper: "/passApi/js/uni_wrapper.js"
        }, _ = "uni_wrapper", E = "uni_forceverify", C = "uni_armorwidget", w = "uni_accConnect", I = {}, S = function(e, t) {
            var n = e.fire("loginSuccess", t);
            n && (window.location ? window.location.href = t.rsp.data.u : document.location.href = t.rsp.data.u)
        }, T = function() {
            var e = 0
              , t = 0
              , n = null
              , i = /msie (\d+\.\d+)/i.test(navigator.userAgent);
            if (i || console.log(navigator.plugins["Shockwave Flash"]),
            i) {
                var s = new ActiveXObject("ShockwaveFlash.ShockwaveFlash");
                s && (e = 1,
                t = s.GetVariable("$version"))
            } else if (navigator && navigator.plugins && navigator.plugins.length > 0 && navigator.plugins["Shockwave Flash"]) {
                var s = navigator.plugins["Shockwave Flash"];
                s && (n = s.filename,
                e = 1,
                t = s.version ? s.version : s.description)
            }
            return {
                isexists: e,
                ver: t,
                filename: n
            }
        }, D = function(e, t) {
            if (!(t && t.config && t.config.noSynBdu && 1 === t.config.noSynBdu)) {
                var n = document.location.protocol.toLowerCase();
                return "https:" != n && passport.data.request.load(n + "//v.tieba.com/platform/agency/setbdu?bdu=" + encodeURIComponent(e) + "&t=" + (new Date).getTime()),
                passport.data.request.load(n + "//user.nuomi.com/pclogin/main/crossdomain?bdu=" + encodeURIComponent(e) + "&t=" + (new Date).getTime()),
                passport.data.request.load(n + "//passport.zongheng.com/bdpass/crossdomain.do?bdu=" + encodeURIComponent(e) + "&t=" + (new Date).getTime()),
                passport.data.request.load("https://www.baifubao.com/api/0/sync_bduss/0?bdu=" + encodeURIComponent(e) + "&t=" + (new Date).getTime()),
                passport.data.request.load("https://passport.qianqian.com/bdpass?bdu=" + encodeURIComponent(e) + "&t=" + (new Date).getTime()),
                passport.data.request.load(n + "//passport.chuanke.com/api/sync?bdu=" + encodeURIComponent(e) + "&t=" + (new Date).getTime()),
                passport.data.request.load(n + "//user.hao123.com/static/crossdomain.php?bdu=" + encodeURIComponent(e) + "&t=" + (new Date).getTime())
            }
        };
        e.login = {
            loginSuccess: function(e, t) {
                var n = /msie (\d+\.\d+)/i.test(navigator.userAgent);
                if (e.config.setWebToClient && !n && s.apply(e, [{
                    args: t
                }]),
                e.config.noSynBdu && 1 === e.config.noSynBdu) {
                    var i = u(e, t, {
                        onCancel: function() {
                            S(e, t)
                        }
                    });
                    i && S(e, t)
                } else
                    D(t.rsp.data.hao123Param, e).success(function() {
                        var n = u(e, t, {
                            onCancel: function() {
                                S(e, t)
                            }
                        });
                        n && S(e, t)
                    });
                return {
                    preventEvent: !0,
                    preventDefault: !0
                }
            },
            loginError: function(e, t) {
                return u(e, t, {
                    onCompleted: function(t, n) {
                        e.config.noSynBdu && 1 === e.config.noSynBdu ? n() : D(t.data.hao123Param, e).success(n)
                    },
                    onCancel: function(t) {
                        t && t.isCompleted && S(e, {
                            rsp: t.rsp
                        })
                    }
                }),
                {
                    preventEvent: !1,
                    preventDefault: !1
                }
            },
            connectNeedBind: function(e, t) {
                return u(e, t, {
                    onCompleted: function() {},
                    onCancel: function() {}
                }),
                {
                    preventEvent: !1,
                    preventDefault: !1
                }
            },
            validateAllError: function(e, t) {
                var n = t.validates ? e.getElement(t.validates[t.validates.length - 1].field) : "";
                return n && n.focus && n.focus(),
                {
                    preventEvent: !1,
                    preventDefault: !1
                }
            }
        }
    }(passport.hook),
    magic.passport = baidu.lang.createClass(function() {
        this._validateInfo = {}
    }, {
        type: "magic.passport",
        superClass: magic.Base
    }).extend({
        _getRegularField: function(e) {
            var t = e.pwd ? "password" : "text"
              , n = this
              , i = 'autocomplete="new-password"'
              , s = e.maxLength ? 'maxlength="' + e.maxLength + '"' : ""
              , o = e.tip ? e.tip : ""
              , r = e.value ? e.value : ""
              , a = "verifycode" == e.field ? "none" : ""
              , c = "";
            c = "text" === t ? '<input type="text" style="display:none;">' : '<input type="password" style="display: none;">';
            var l = '<p id="' + n.$getId(e.field + "Wrapper") + '" class="pass-form-item pass-form-item-' + e.field + '" style="display:' + a + '">' + (e.label ? '<label for="' + n.$getId(e.field) + '" id="' + n.$getId(e.field + "Label") + '" class="pass-label pass-label-' + e.field + '">' + e.label + "</label>" : "") + c + '<input id="' + n.$getId(e.field) + '" type="' + t + '" name="' + e.field + '" class="pass-text-input pass-text-input-' + e.field + '" ' + s + (e.placeholder ? 'placeholder="' + e.placeholder + '" ' : "") + i + (e.disabled ? '" disabled' : "") + ' value="' + r + '"/>' + (e.noError ? "" : '<span id="' + n.$getId(e.field + "Error") + '" class="pass-item-error pass-item-error-' + e.field + '"></span>') + (e.hasSucc ? '<span id="' + n.$getId(e.field + "Succ") + '" class="pass-item-succ pass-item-succ-' + e.field + '" style="display:none;"></span>' : "") + '<span id="' + n.$getId(e.field + "Tip") + '" class="pass-item-tip pass-item-tip-' + e.field + '" style="display:none"><span id="' + n.$getId(e.field + "TipText") + '" class="pass-item-tiptext pass-item-tiptext-' + e.field + '">' + o + "</span></span></p>";
            return l
        },
        _getHiddenField: function(e, t) {
            var n, i = this, s = '<p id="' + i.$getId(t || "hiddenFields") + '" style="display:none">';
            for (var o in e)
                e.hasOwnProperty(o) && (n = "string" == typeof e[o] ? e[o].replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/\x22/g, "&quot;").replace(/\x27/g, "&#39;") : e[o],
                s += '<input type="hidden" id="' + i.$getId((t ? t + "_" : "") + o) + '" name="' + o + '" value="' + n + '" />');
            return s += "</p>"
        },
        _setEvent: function() {
            var e = this
              , t = this.getElement()
              , n = function(t) {
                e._eventHandler.entrance.apply(e, [t])
            };
            baidu(e.getElement()).on("resize", function() {
                var e = (navigator.userAgent,
                !navigator.userAgent.match(/OS [1-8]_\d[_\d]* like Mac OS X/i))
                  , t = !!navigator.userAgent.toString().match(/\(i[^;]+;( U;)? CPU.+Mac OS X/)
                  , n = navigator.userAgent.toString().indexOf("iPad");
                if (e && t && null != n) {
                    var i = document.getElementsByClassName("popBox");
                    null != i && i.length > 0 && (i[0].style.height = window.screen.height > document.body.clientHeight ? window.screen.height * (window.screen.height / document.body.clientHeight) + 120 + "px" : window.screen.height * (window.screen.height / document.body.clientHeight))
                }
            }),
            baidu(e.getElement("form")).on("submit", n),
            baidu(e.getElement("license")).on("click", n),
            baidu(e.getElement("verifyCodeChange")).on("click", n),
            baidu(e.getElement("verifyCodeSend")).on("click", n),
            baidu(e.getElement("smsVcodeSend")).on("click", n),
            baidu(t).delegate(".pass-suggest-item label", "click", n),
            baidu(".pass-text-input", e.getElement()).on({
                focus: n,
                blur: n,
                change: n,
                keyup: n,
                mouseover: n,
                mouseout: n
            })
        },
        _validator: {
            confStorage: {},
            builtInMsg: {
                required: "请您输入%s",
                phone: "手机号码格式不正确",
                email: "邮箱格式不正确",
                idcard: "身份证格式不正确"
            },
            builtInRules: {
                required: /\S+/,
                phone: /^1[3456789]\d{9}$/,
                email: /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/,
                idcard: /(^\d{15}$)|(^\d{17}(\d|X|x)$)/
            },
            init: function(e, t) {
                this.confStorage[e.$getId()] = t
            },
            validate: function(e, t, n, i) {
                var s = e.getElement(t)
                  , o = {
                    field: t
                }
                  , r = /^\s*(.+?)\s*$/;
                if (!s || 0 == s.offsetHeight)
                    return !1;
                for (var a = s.value.replace(r, "$1"), c = this.confStorage[e.$getId()][t], l = c.rules, d = 0, u = l.length; u > d; d++) {
                    var p, g = l[d], h = this.builtInRules[g];
                    if (p = "[object function]" == Object.prototype.toString.call(h).toLowerCase() ? h.call(e, s, i) : new RegExp(h).test(a),
                    !p)
                        return o.error = !0,
                        e._validateInfo[t] = 0,
                        o.msg = this.builtInMsg[g].replace(/\%s/, c.desc),
                        e._validateError(o),
                        void n.error(o)
                }
                c.asyncRule ? c.asyncRule.call(e, {
                    success: function(i) {
                        o.error = !1,
                        o.data = i.data,
                        e._validateInfo[t] = 1,
                        e._validateSuccess(o),
                        n.success(o)
                    },
                    error: function(i) {
                        o.error = !0,
                        e._validateInfo[t] = 0,
                        o.msg = i.msg,
                        e._validateError(o),
                        n.error(o)
                    }
                }, i) : (o.error = !1,
                e._validateInfo[t] = 1,
                e._validateSuccess(o),
                n.success(o))
            },
            validateAll: function(e, t, n) {
                function i() {
                    a = !0,
                    r ? t && t.error(c) : t && t.success(c)
                }
                var s = this.confStorage[e.$getId()]
                  , o = 0
                  , r = !1
                  , a = !1
                  , c = []
                  , l = this._getActiveValidate(e, !0);
                for (var d in s) {
                    if (a)
                        break;
                    this.validate(e, d, {
                        success: function(e) {
                            o++,
                            c.push(e),
                            o == l && i()
                        },
                        error: function(e) {
                            return r = !0,
                            o++,
                            c.push(e),
                            n ? void i() : void (o == l && i())
                        }
                    }, "all")
                }
            },
            _getActiveValidate: function(e, t) {
                var n = this.confStorage[e.$getId()]
                  , i = [];
                for (var s in n) {
                    var o = e.getElement(s);
                    o && 0 != o.offsetHeight && i.push(o)
                }
                return t ? i.length : i
            },
            addRule: function(e, t) {
                var n = {};
                n[e] = t,
                baidu.extend(this.builtInRules, n)
            },
            addMsg: function(e, t) {
                var n = {};
                n[e] = t,
                baidu.extend(this.builtInMsg, n)
            }
        },
        validate: function(e, t) {
            var n = this
              , i = n.fireEvent("beforeValidate", {
                validate: {
                    field: e,
                    ele: baidu(n.getElement(e))
                }
            });
            i && n._validator.validate(n, e, {
                success: function(e) {
                    var i = n.fireEvent("validateSuccess", {
                        validate: e
                    });
                    i && t && t.success && t.success(e)
                },
                error: function(e) {
                    var i = n.fireEvent("validateError", {
                        validate: e
                    });
                    i && t && t.error && t.error(e)
                }
            })
        },
        validateAll: function(e, t) {
            var n = this;
            t = "boolean" == typeof e ? e : t ? t : !1;
            var i = n.fireEvent("beforeValidateAll");
            i && n._validator.validateAll(n, {
                success: function(t) {
                    var i = n.fireEvent("validateAllSuccess", {
                        validates: t
                    });
                    i && e && e.success && e.success(t)
                },
                error: function(t) {
                    var i = n.fireEvent("validateAllError", {
                        validates: t
                    });
                    i && e && e.error && e.error(t)
                }
            }, t)
        },
        getValidateStatus: function(e) {
            return this._validateInfo.hasOwnProperty(e) ? this._validateInfo[e] : -1
        },
        setValidateSuccess: function(e) {
            var t = this;
            t._validateInfo[e] = 1,
            t._validateSuccess({
                field: e
            })
        },
        setValidateError: function(e, t, n) {
            var i = this;
            i._validateInfo[e] = 0,
            i._validateError({
                field: e,
                msg: t
            }, n)
        },
        setGeneralError: function(e) {
            this.getElement("error").innerHTML = e
        },
        clearGeneralError: function() {
            this.getElement("error").innerHTML = ""
        },
        _isSupportPlaceholder: function() {
            return "placeholder"in document.createElement("input")
        },
        _getPlaceholder: function(e) {
            for (var t = this, n = {}, i = "", s = {}, o = 0; o < e.length; o++)
                i = t.lang[e[o].placeholder],
                0 != e[o].clearbtn && (s[o] = baidu('<span id="' + t.$getId(e[o].label + "_clearbtn") + '" class="pass-clearbtn pass-clearbtn-' + e[o].label + '" style="display:none;"></span>'),
                baidu(t.getElement(e[o].label)).after(s[o])),
                t._isSupportPlaceholder() && !baidu.browser.ie ? baidu(t.getElement(e[o].label)).attr({
                    placeholder: i
                }) : (n[o] = baidu('<span id="' + t.$getId(e[o].label + "_placeholder") + '" class="pass-placeholder pass-placeholder-' + e[o].label + '">' + i + "</span>"),
                baidu(t.getElement(e[o].label)).after(n[o])),
                t._rendEventPlaceholder(t.getElement(e[o].label), n[o], s[o])
        },
        _getCookie: function(e) {
            var t, n = new RegExp("(^| )" + e + "=([^;]*)(;|$)");
            return (t = document.cookie.match(n)) ? unescape(t[2]) : null
        },
        _logPass: function(e, t) {
            function n(e) {
                var t, n, i, s, o, r, a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
                for (i = e.length,
                n = 0,
                t = ""; i > n; ) {
                    if (s = 255 & e.charCodeAt(n++),
                    n == i) {
                        t += a.charAt(s >> 2),
                        t += a.charAt((3 & s) << 4),
                        t += "==";
                        break
                    }
                    if (o = e.charCodeAt(n++),
                    n == i) {
                        t += a.charAt(s >> 2),
                        t += a.charAt((3 & s) << 4 | (240 & o) >> 4),
                        t += a.charAt((15 & o) << 2),
                        t += "=";
                        break
                    }
                    r = e.charCodeAt(n++),
                    t += a.charAt(s >> 2),
                    t += a.charAt((3 & s) << 4 | (240 & o) >> 4),
                    t += a.charAt((15 & o) << 2 | (192 & r) >> 6),
                    t += a.charAt(63 & r)
                }
                return t
            }
            var i = document.location.protocol + "//nsclick.baidu.com/v.gif?v=" + (new Date).getTime()
              , s = "";
            for (var o in t)
                s = s + o + ":" + t[o] + ",";
            s = n("{" + s.substring(0, s.length - 1) + "}");
            var r = "&page=" + e.page + "&source=pc&tpl=" + e.tpl + "&auto_statistic=" + s;
            if (i += r) {
                var a = new Image;
                a.onload = a.onerror = function() {
                    a.onload = a.onerror = null,
                    a = null
                }
                ,
                a.src = i
            }
        },
        _rendEventPlaceholder: function(e, t, n) {
            if (e || n) {
                var i, s, o = this, r = function(e) {
                    1 == e ? (t && t[0] && o.$hide(t[0]),
                    n && n[0] && o.$show(n[0])) : (t && t[0] && o.$show(t[0]),
                    n && n[0] && o.$hide(n[0]))
                };
                setTimeout(function() {
                    void 0 != e && e.value && r(1)
                }, 200),
                baidu(t).on("mousedown", function() {
                    s = !0,
                    clearTimeout(i),
                    i = setTimeout(function() {
                        o.suggestionDom && "none" != o.suggestionDom.style.display || e.focus()
                    }, 0)
                }),
                baidu(n).on("click", function() {
                    e.value = "",
                    r(0),
                    e.focus(),
                    o.suggestionDom && (o.suggestionDom.data_delete = !0,
                    setTimeout(function() {
                        o.suggestionDom.data_delete = !1
                    }, 200))
                }),
                baidu(e).on("keyup", function() {
                    r(e.value ? 1 : 0)
                }),
                baidu(e).on("focus", function() {
                    inputCheckTimer = setInterval(function() {
                        e.value.length ? (r(1),
                        clearInterval(inputCheckTimer)) : r(0)
                    }, 30)
                })
            }
        },
        SBCtoDBC: function(e) {
            var t = "";
            if (e) {
                for (var n = e.length, i = 0; n > i; i++) {
                    var s = e.charCodeAt(i);
                    s = s >= 65281 && 65374 >= s ? s - 65248 : s,
                    s = 12288 == s ? 32 : s,
                    t += String.fromCharCode(s)
                }
                return t
            }
        },
        hide: function() {
            this.getElement().style.display = "none"
        },
        show: function() {
            this.getElement().style.display = "block"
        },
        _analysis: function(e, t) {
            return passport.analysis && passport.analysis[this.module] && passport.analysis[this.module][e] ? (passport.analysis[this.module][e](this, t),
            {
                preventDefault: !1,
                preventEvent: !1
            }) : void 0
        },
        _hook: function(e, t) {
            return passport.hook && passport.hook[this.module] && passport.hook[this.module][e] ? passport.hook[this.module][e](this, t) : {
                preventDefault: !1,
                preventEvent: !1
            }
        },
        fireEvent: function(e, t) {
            var n = this._hook(e, t)
              , i = (this._analysis(e, t),
            !0);
            return n.preventEvent || (i = this.fire(e, t)),
            !n.preventDefault && i
        }
    }),
    magic.passport.login = baidu.lang.createClass(function(e) {
        var t = this;
        if (passport && "https" === passport._protocol)
            var n = "https:";
        else
            var n = window.location ? window.location.protocol.toLowerCase() : document.location.protocol.toLowerCase();
        t._domain = {
            https: "https://passport.baidu.com",
            http: "http://passport.baidu.com",
            staticFile: "https:" === n ? "https://ss0.bdstatic.com/5LMZfyabBhJ3otebn9fN2DJv" : "http://passport.bdimg.com",
            auto: "https:" === n ? "https://passport.baidu.com" : "http://passport.baidu.com"
        },
        t.config = {
            memberPass: !0,
            isQuickUser: 0,
            safeFlag: 0,
            product: "",
            idc: "",
            charset: "",
            loginMerge: !0,
            staticPage: "",
            hasRegUrl: !1,
            u: "",
            lang: "zh-CN",
            autosuggest: !1,
            hasPlaceholder: !1,
            registerLink: "",
            authsiteLogin: "",
            authsiteCfgLogin: "",
            qrcode: !0,
            sms: 0,
            uniqueId: !1,
            autoFocus: !0,
            subpro: "",
            setWebToClient: !1,
            is_voice_sms: 0,
            voice_sms_flag: 0,
            userPwdLogin: 0,
            qrcode_animation: 1,
            qrcode_style: !0
        },
        baidu.extend(t.config, e),
        t.config.product = t.config.product || "isnull",
        t.config.qrcode = 3,
        this.module = "login",
        this.guideRandom = function() {
            return "xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                var t = 16 * Math.random() | 0
                  , n = "x" == e ? t : 3 & t | 8;
                return n.toString(16)
            }).toUpperCase()
        }(),
        t.constant = {
            CHECKVERIFYCODE: !0,
            CONTAINER_CLASS: "tang-pass-login",
            LABEL_FOCUS_CLASS: "pass-text-label-focus",
            FOCUS_CLASS: "pass-text-input-focus",
            HOVER_CLASS: "pass-text-input-hover",
            ERROR_CLASS: "pass-text-input-error",
            VERIFYCODE_URL_PREFIX: t._domain.https + "/cgi-bin/genimage?",
            BLANK_IMG_URL: passport.apiDomain.staticDomain + "/passApi/img/small_blank.gif",
            MODIFY_PWD_URL_PREFIX: t._domain.https + "/forcsdnpasschange",
            GET_PASSWORD_URL: t._domain.https + "/?getpassindex&tt=" + (new Date).getTime() + "&gid=" + t.guideRandom + "&tpl=" + encodeURIComponent(t.config.product) + "&u=" + encodeURIComponent(t.config.u),
            REG_URL: t.config.registerLink || t._domain.https + "/v2/?reg&tt=" + (new Date).getTime() + "&overseas=" + t.config.overseas + "&gid=" + t.guideRandom + "&tpl=" + encodeURIComponent(t.config.product) + "&u=" + encodeURIComponent(t.config.u),
            PROTOCAL_URL: t._domain.http + "/static/passpc-account/html/protocal.html",
            NOCAPTCHA_URL: t._domain.auto + "/static/passpc-base/js/ld.min.js?cdnversion=" + (new Date).getTime(),
            SUBMITFLAG: !1
        },
        t.lang = passport.err.getCurrent().labelText.login,
        passport.data.setContext(baidu.extend({}, t.config)),
        this.initialized = !1,
        this.validatorInited = !1,
        this.bdPsWtoken = "",
        this.innerData = {
            normal: {},
            phone: {}
        },
        this.dataFiels = ["userName", "password"],
        this.initTime = (new Date).getTime(),
        confirmSmsVerifyWidget = null,
        checkPhoneWidget = null,
        checkPhoneExist = !1;
        var i = /msie (\d+\.\d+)/i.test(navigator.userAgent) ? document.documentMode || +RegExp.$1 : void 0;
        6 >= i && (t.config.qrcode_animation = !1),
        t.passLowerIE = i,
        t.config.overseas && 1 == t.config.overseas && (this.foreignMobile = !0),
        this.internation = !1,
        t._insertNoCaptchaScript(),
        t.config.defaultCss && t._loadCssFileW("/passApi/css/loginv4_e3d7fd1.css", function() {}),
        (t.config.memberPass || t.config.getapi) && t._initApi(),
        this.smsConfig = t.config.sms + "" == "5" ? !0 : !1
    }, {
        type: "magic.passport.login",
        superClass: magic.passport
    }).extend({
        _getIrregularField: function(e) {
            var t = this
              , n = {
                makeText: '<p id="' + t.$getId("MakeTextWrapper") + '" class="pass-make-text" style="display:none;"></p>',
                logoText: '<p class="pass-form-logo">' + t.lang.backToLogin + "</p>",
                verifyCode: '<p id="' + t.$getId("verifyCodeImgWrapper") + '" class="pass-form-item pass-form-item-verifyCode" style="display:none"><input id="' + t.$getId("verifyCode") + '" type="text" name="verifyCode" class="pass-text-input pass-text-input-verifyCode" maxlength="6" /><span  id="' + t.$getId("verifyCodeImgParent") + '" class="pass-verifyCodeImgParent" ><img id="' + t.$getId("verifyCodeImg") + '" class="pass-verifyCode" src="' + t.constant.BLANK_IMG_URL + '" /></span><a id="' + t.$getId("verifyCodeChange") + '" href="#" class="pass-change-verifyCode">' + t.lang.captchaChange + '</a><span id="' + t.$getId("verifyCodeError") + '" class="pass-error pass-error-verifyCode"></span><span id="' + t.$getId("verifyCodeTip") + '" class="pass-tip pass-tip-verifyCode"></span><span id="' + t.$getId("verifyCodeSuccess") + '" class="pass-success pass-success-verifyCode"></span></p>',
                generalError: '<p id="' + t.$getId("errorWrapper") + '" class="pass-generalErrorWrapper"><span id="' + t.$getId("error") + '" class="pass-generalError pass-generalError-error"></span></p>',
                rem: '<p id="' + t.$getId("memberPassWrapper") + '" class="pass-form-item pass-form-item-memberPass"><input id="' + t.$getId("memberPass") + '" type="checkbox" name="memberPass" class="pass-checkbox-input pass-checkbox-memberPass"' + (t.config.memberPass ? ' checked="checked"' : "") + ' /><label for="' + t.$getId("memberPass") + '" id="' + t.$getId("memberPassLabel") + '" class="">' + t.lang.memberPassLabel + "</label></p>",
                submit: '<p id="' + t.$getId("submitWrapper") + '" class="pass-form-item pass-form-item-submit"><input id="' + t.$getId("submit") + '" type="submit" value="' + t.lang.login + '" class="pass-button pass-button-submit" /><a class="pass-fgtpwd pass-link" href="' + t.constant.GET_PASSWORD_URL + '" target="_blank">' + t.lang.fgtPwd + "</a>" + (t.smsConfig ? '<a class="pass-sms-btn pass-link" title="' + t.lang.toSmsBtn + '" data-type="sms" id="' + t.$getId("smsSwitchWrapper") + '">' + t.lang.toSmsBtn + "</a>" : "") + "</p>",
                foreignMobileMsg: '<p class="pass-foreignMobile-msg" id="' + t.$getId("foreignMobileMsg") + '">' + t.lang.foreignMobileMsg + "</p>",
                foreignMobileWrapper: '<div class="pass-form-item pass-form-item-PhoneCountry pass-foreignMobile-wrapper" id="' + t.$getId("foreignMobileWrapper") + '" style="display:none"><label for="' + t.$getId("foreignMobile") + '" id="' + t.$getId("foreignMobileLabel") + '" class="pass-label" data-countryCode="">+86</label><input id="' + t.$getId("foreignMobile") + '" type="text" name="foreignusername" class="pass-text-input"/><ul id="' + t.$getId("foreignCountryList") + '" class="pass-country-list"></ul></div>',
                foreignMobileLink: '<p class="pass-foreignMobile-link-wrapper" id="' + t.$getId("foreignMobileLinkWrapper") + '"><a id="' + t.$getId("foreignMobileLink") + '" class="pass-foreignMobile-link">' + t.lang.foreignMobileLink + "</a></p>",
                foreignMobileBack: '<p class="pass-foreignMobile-back-wrapper" id="' + t.$getId("foreignMobileBackWrapper") + '"><a id="' + t.$getId("foreignMobileBack") + '" class="pass-foreignMobile-link">' + t.lang.foreignToLogin + "</a></p>",
                choiceuser: '<div id="' + t.$getId("choiceuser_article") + '" class="tang-pass-login-choice choiceuser-article"><div class="choiceuser-msg"><p class="choiceuser-msg-title">亲爱的用户，</p><p class="choiceuser-msg-text">为了确保您的帐号安全，请先确认您输入的帐号是用户名还是手机号：</p></div><div class="choiceuser-buttons"><div class="choiceuser-btn"><input class="pass-button pass-button-choiceuser-username" type="button" value="用户名" id="' + t.$getId("choiceuser_btn_username") + '"/><input class="pass-button pass-button-choiceuser-phone" type="button" value="手机号" id="' + t.$getId("choiceuser_btn_mobile") + '"/></div><div class="choiceuser-back"><a href="#" id="' + t.$getId("choiceuser_btn_back") + '">' + t.lang.backToLogin + "</a></div></div></div>",
                webtoclint: '<div id="' + t.$getId("pass_b2c") + '" style="display:none;"></div>',
                is_voice_sms: '<div class="pass-smsSwitchWrapper"><a class="pass-is_voice_sms-btn" title="语音验证码" data-type="is_voice_sms" >语音验证码</a></div>'
            };
            return n[e]
        },
        _getTemplate: function() {
            var e = this
              , t = '<form id="' + e.$getId("form") + '" class="pass-form pass-form-normal" method="POST" autocomplete="off">'
              , n = {
                codeString: "",
                safeFlag: e.config.safeFlag,
                u: e.config.u,
                isPhone: !1,
                detect: "1",
                gid: e.guideRandom || "",
                staticPage: e.config.staticPage,
                quick_user: e.config.isQuickUser,
                logintype: e.config.diaPassLogin ? "dialogLogin" : "basicLogin",
                logLoginType: e.config.diaPassLogin ? "pc_loginDialog" : "pc_loginBasic",
                subpro: e.config.subpro,
                idc: e.config.idc,
                loginMerge: !0
            }
              , i = [{
                field: "userName",
                noError: !0
            }, {
                field: "password",
                pwd: !0,
                noError: !0
            }];
            t += e._getIrregularField("logoText"),
            t += e._getIrregularField("generalError"),
            t += e._getIrregularField("makeText"),
            t += e._getHiddenField(n),
            e.foreignMobile && (t += e._getIrregularField("foreignMobileMsg"),
            t += e._getIrregularField("foreignMobileWrapper"));
            for (var s = 0; s < i.length; s++)
                t += e._getRegularField(i[s]);
            return t += e._getIrregularField("verifyCode"),
            t += e._getIrregularField("rem"),
            e.foreignMobile && (t += e._getIrregularField("foreignMobileLink"),
            t += e._getIrregularField("foreignMobileBack")),
            t += e._getIrregularField("submit"),
            t += "</form>"
        },
        _collectData: function() {
            for (var e = this, t = e.innerData.normal, n = e.dataFiels, i = 0, s = n.length; s > i; i++)
                t[n[i]] = e.getElement(n[i]).value;
            return t
        },
        _restoreData: function(e) {
            for (var t = this, n = t.innerData[e ? e : "normal"], i = t.dataFiels, s = 0, o = i.length; o > s; s++)
                t.getElement(i[s]).value = n[i[s]] || "";
            return n
        },
        _loadCssFileW: function(e, t) {
            var n = this;
            if (window._loadedFilesW = window._loadedFilesW || {},
            !window._loadedFilesW[e]) {
                window._loadedFilesW[e] = !0;
                var i = document.createElement("link");
                i.rel = "stylesheet",
                i.type = "text/css",
                i.href = n._domain.staticFile + e,
                document.getElementsByTagName("head")[0].appendChild(i),
                i.readyState ? i.onreadystatechange = function() {
                    ("loaded" == i.readyState || "complete" == i.readyState) && (i.onreadystatechange = null,
                    t && t())
                }
                : i.onload = function() {
                    t && t()
                }
            }
        },
        _insertScriptW: function(e, t) {
            if (window._loadedFilesW = window._loadedFilesW || {},
            !window._loadedFilesW[e]) {
                window._loadedFilesW[e] = !0;
                var n = document
                  , i = n.createElement("SCRIPT");
                i.type = "text/javascript",
                i.charset = "UTF-8",
                i.readyState ? i.onreadystatechange = function() {
                    ("loaded" == i.readyState || "complete" == i.readyState) && (i.onreadystatechange = null,
                    t && t())
                }
                : i.onload = function() {
                    t && t()
                }
                ,
                i.src = e,
                n.getElementsByTagName("head")[0].appendChild(i)
            }
        },
        _authSiteW: function() {
            var e = this
              , t = e.config
              , n = e.getPhoenixId("pass_phoenix_btn");
            t.authsitecssLoad && e._loadCssFileW("/passApi/css/authsite_c01e2ff.css"),
            e._insertScriptW(e._domain.auto + "/phoenix/account/jsapi", function() {
                window.baidu.phoenix && window.baidu.phoenix.require(t.authsiteLogin, baidu.extend(t.authsiteCfgLogin || {}, {
                    tpl: t.product ? t.product : "",
                    idc: t.idc ? t.idc : "",
                    u: t.u,
                    subpro: t && t.subpro || "",
                    target: n,
                    html: {
                        qzone: '<a class="phoenix-btn-item" href="#" data-title="qzone">QQ帐号</a>',
                        tsina: '<a class="phoenix-btn-item" href="#" data-title="tsina">新浪微博</a>',
                        tqq: '<a class="phoenix-btn-item" href="#" data-title="tqq">腾讯微博</a>',
                        qunar: '<a class="phoenix-btn-item" href="#" data-title="qunar">去哪儿</a>',
                        weixin: '<a class="phoenix-btn-item" href="#" data-title="weixin">微信</a>',
                        tianyi: '<a class="phoenix-btn-item" href="#" data-title="tianyi">天翼</a>',
                        feifan: '<a class="phoenix-btn-item" href="#" data-title="feifan">飞凡</a>'
                    },
                    onAfterRender: function() {
                        for (var t = baidu("#" + n + " li"), i = function(t) {
                            t.on("click", function(n) {
                                var i = {
                                    page: "loginv4",
                                    tpl: e.config.product || ""
                                }
                                  , s = {
                                    eventType: t.attr("data-title") + "Click"
                                };
                                e._logPass(i, s),
                                n.preventDefault()
                            })
                        }, s = 0; s < t.length; s++) {
                            var o = baidu(".phoenix-btn-item", t[s]);
                            o.attr({
                                title: o[0] && o[0].innerHTML || ""
                            }),
                            i(o)
                        }
                    }
                }))
            })
        },
        getVerifyCode: function(e) {
            var t = this
              , n = {
                fr: "login",
                loginVersion: "v4",
                vcodetype: t.vcodetype || ""
            };
            if (t.getElement("verifyCode").value = "",
            t.$hide("verifyCodeSuccess"),
            t.getElement("verifyCode_clearbtn") && t.$hide("verifyCode_clearbtn"),
            t.getElement("verifyCodeImg").src = "",
            e && e.length) {
                t.$show("verifyCodeImgWrapper"),
                t.getElement("verifyCodeImg").src = t.constant.VERIFYCODE_URL_PREFIX + e,
                t.getElement("codeString").value = e;
                var i = t.fireEvent("renderVerifycode", {
                    verifyStr: e,
                    verifyCodeImg: t.constant.VERIFYCODE_URL_PREFIX + e
                });
                if (!i)
                    return
            } else
                passport.data.getVerifyCodeStr(n).success(function(e) {
                    if (0 == e.errInfo.no) {
                        t.$show("verifyCodeImgWrapper"),
                        t.getElement("verifyCodeImg").src = t.constant.VERIFYCODE_URL_PREFIX + e.data.verifyStr,
                        t.getElement("codeString").value = e.data.verifyStr;
                        var n = t.fireEvent("renderVerifycode", {
                            verifyStr: e.data.verifyStr,
                            verifyCodeImg: t.constant.VERIFYCODE_URL_PREFIX + e.data.verifyStr
                        });
                        if (!n)
                            return
                    }
                });
            t.getElement("verifyCode_placeholder") && setTimeout(function() {
                t.$show("verifyCode_placeholder")
            }, 200)
        },
        _getWDom: {
            parent: function(e) {
                return e.parentNode || e.parentElement
            },
            next: function(e) {
                do
                    e = e.nextSibling;
                while (e && 1 != e.nodeType);return e
            },
            prev: function(e) {
                do
                    e = e.previousSibling;
                while (e && 1 != e.nodeType);return e
            }
        },
        clearVerifyCode: function() {
            var e = this;
            e.$hide("verifyCodeImgWrapper"),
            e.getElement("codeString").value = ""
        },
        getPhoenixId: function(e) {
            if (this.config.uniqueId)
                return this.$getId(e);
            var t = {
                pass_phoenix_login: "pass-phoenix-login",
                pass_phoenix_list_login: "pass-phoenix-list-login",
                pass_phoenix_btn: "pass_phoenix_btn"
            };
            return t[e]
        },
        getPhoenixElement: function(e) {
            return this.getElement(e) ? this.getElement(e) : document.getElementById(this.getPhoenixId(e))
        },
        _getTemplateOther: function() {
            var e = []
              , t = this
              , n = 0;
            return t.config.authsiteLogin && (n = t.config.authsiteLogin.length),
            e.push('<div id="' + t.getPhoenixId("pass_phoenix_login") + '" class="tang-pass-login-phoenix"><div id="' + t.getPhoenixId("pass_phoenix_list_login") + '" class="pass-phoenix-list clearfix">' + (t.config.authsiteLogin ? '<div class="pass-phoenix-btn clearfix" id="' + t.getPhoenixId("pass_phoenix_btn") + '"></div>' : "") + '</div><div class="clear"></div></div>'),
            e.join("")
        },
        getTemplateFooterBar: function() {
            var e = this
              , t = [];
            return t.push('<div class="tang-pass-footerBar">' + (3 === e.config.qrcode ? '<p class="tang-pass-footerBarQrcode pass-link" title="' + e.lang.qrcodeBtn + '" data-type="qrcode" id="' + e.$getId("footerQrcodeBtn") + '"' + (1 != e.config.userPwdLogin ? ' style="display:none;"' : "") + ">" + e.lang.qrcodeBtn + "</p>" : "") + '<p class="tang-pass-footerBarULogin pass-link" title="' + e.lang.footerBackToLogin + '" data-type="normal" id="' + e.$getId("footerULoginBtn") + '"' + (1 == e.config.userPwdLogin ? ' style="display:none;"' : "") + ">" + e.lang.footerBackToLogin + "</p>" + (e.config.authsiteLogin.length > 0 ? '<div class="tang-pass-footerBarPhoenix"><span class="tang-pass-footerBarPhoenixSplit"></span><div class="tang-pass-footerBarPhoenixItem" id="' + e.$getId("PhoenixItem") + '"></div></div>' : "") + '<a class="pass-reglink pass-link" href="' + e.constant.REG_URL + '" target="_blank" ' + (e.config.hasRegUrl ? "" : 'style="display:none"') + ">" + e.lang.register + "</a></div>"),
            t.join("")
        },
        setEventFooterBar: function() {
            var e = this
              , t = e.$getId("footerQrcodeBtn")
              , n = e.$getId("footerULoginBtn");
            baidu("#" + t).on("click", function(i) {
                i && i.preventDefault && i.preventDefault(),
                e._changeLoginType("qrcode"),
                baidu("#" + t).hide(),
                baidu("#" + n).show()
            }),
            baidu("#" + n).on("click", function(i) {
                i && i.preventDefault && i.preventDefault();
                var s = {
                    page: "loginv4",
                    tpl: e.config.product || ""
                }
                  , o = {
                    eventType: "userPwdLoginClick"
                };
                e._logPass(s, o),
                e._changeLoginType("normal"),
                baidu("#" + n).hide(),
                baidu("#" + t).show()
            })
        },
        _getTemplateQrcode: function() {
            var e = this
              , t = []
              , n = e.config.qrcodeCfg && e.config.qrcodeCfg.appHref || ""
              , i = e.config.qrcodeCfg && e.config.qrcodeCfg.appName || "";
            return t.push('<div id="' + e.$getId("qrcode") + '" class="clearfix tang-pass-qrcode tang-pass-login" style="display:none;">'),
            t.push('<p class="pass-form-logo">' + e.lang.qrcodeBtn + "</p>"),
            t.push('<div class="tang-pass-qrcode-content" id="' + e.$getId("qrcodeContent") + '">'),
            t.push('<div class="tang-pass-qrcode-init">'),
            t.push('<div class="Qrcode-status-con tang-pass-qrcode-imgWrapper" id="' + e.$getId("QrcodeMain") + '"><img class="tang-pass-qrcode-img" src="' + e._domain.staticFile + '/passApi/img/loading.gif"/>' + (e.config.qrcode_animation ? '<p class="Qrcode-status-animation' + (8 == e.passLowerIE ? " Qrcode-status-animation-hackIE8" : "") + '" id="' + e.$getId("QrcodeAnimation") + '"></p>' : "") + "</div>"),
            t.push('<div class="Qrcode-status-con Qrcode-status-success" id="' + e.$getId("QrcodeSuccess") + '"><p class="Qrcode-status-icon"></p><p>' + e.lang.QrcodeSuccessTip + '</p><p class="Qrcode-status-msg">' + e.lang.QrcodeSuccessMsg + "</p></div>"),
            t.push('<div class="Qrcode-status-con Qrcode-status-error" id="' + e.$getId("QrcodeError") + '"><p class="Qrcode-status-icon"></p><p>' + e.lang.QrcodeErrorTip + '</p><p class="Qrcode-refresh-btn" id="' + e.$getId("QrcodeErrorfreshBtn") + '">' + e.lang.QrcodeRefreshBtn + "</p></div>"),
            t.push('<div class="Qrcode-status-con Qrcode-status-refresh" id="' + e.$getId("QrcodeRefresh") + '"><p class="Qrcode-status-icon"></p><p class="refresh-title refresh-timeout">' + e.lang.QrcodeRefreshTip + '</p><p class="refresh-title refresh-loadout">' + e.lang.QrcodeLoadTip + '</p><p class="Qrcode-refresh-btn" id="' + e.$getId("QrcodeRefreshBtn") + '">' + e.lang.QrcodeRefreshBtn + "</p></div>"),
            t.push("</div>"),
            t.push("</div>"),
            t.push('<p class="tang-pass-qrcode-title">' + e.lang.qrcodeTitle + (e.config.qrcodeCfg ? '<a class="pass-link" href="' + n + '">' + i + "</a>或" : "") + e.lang.qrcodeHref + "</p>"),
            t.push('<ul class="tang-pass-qrcode-ullist"><li class="tang-pass-qrcode-list"><span class="tang-pass-qrcode-list-aq"></span><span>' + e.lang.qrcodeListaq + '</span></li><li class="tang-pass-qrcode-list"><span class="tang-pass-qrcode-list-gx"></span><span>' + e.lang.qrcodeListgx + '</span></li><li class="tang-pass-qrcode-list"><span class="tang-pass-qrcode-list-bj"></span><span>' + e.lang.qrcodeListbj + "</span></li></ul>"),
            t.push("</div>"),
            t.join("")
        },
        _setEventQrcode: function() {
            var e = this;
            1 != e.config.userPwdLogin && (/msie 6/i.test(navigator.userAgent) ? setTimeout(function() {
                e._changeLoginType("qrcode")
            }, 0) : e._changeLoginType("qrcode"))
        },
        _setChannel: function() {
            var e = this
              , t = {
                apiver: "v3",
                tt: (new Date).getTime()
            }
              , n = e.getElement("qrcodeContent");
            passport[e.$getId("spareWData")] = passport[e.$getId("spareWData")] || {},
            baidu(".Qrcode-status-con", n).hide(),
            e.$show(e.getElement("QrcodeMain")),
            passport[e.$getId("spareWData")].loadQrcode = setTimeout(function() {
                e.config.qrcode_style && (baidu(".Qrcode-status-con", n).hide(),
                baidu(".refresh-title", n).hide(),
                baidu(".refresh-loadout", n).show(),
                e.$show(e.getElement("QrcodeRefresh")))
            }, 5e3),
            baidu.ajax({
                url: e._domain.https + "/v2/api/getqrcode?lp=pc&gid=" + (e.guideRandom || ""),
                dataType: "jsonp",
                data: t,
                success: function(t) {
                    clearTimeout(passport[e.$getId("spareWData")].loadQrcode),
                    clearTimeout(passport[e.$getId("spareWData")].unicast),
                    passport[e.$getId("spareWData")].channelimg = (window.location ? window.location.protocol : document.location.protocol) + "//" + t.imgurl,
                    passport[e.$getId("spareWData")].sign = t.sign,
                    e._createChannel(passport[e.$getId("spareWData")].sign);
                    for (var i = baidu(".tang-pass-qrcode-img", n), s = 0, o = i.length; o > s; s++)
                        i.get(s).src = passport[e.$getId("spareWData")].channelimg
                },
                error: function() {
                    clearTimeout(passport[e.$getId("spareWData")].loadQrcode),
                    clearTimeout(passport[e.$getId("spareWData")].unicast),
                    e.config.qrcode_style && (baidu(".Qrcode-status-con", n).hide(),
                    e.$show(e.getElement("QrcodeError")))
                }
            })
        },
        _stopChannel: function() {
            var e = this;
            passport[e.$getId("spareWData")] = passport[e.$getId("spareWData")] || {},
            passport[e.$getId("spareWData")].sign = "",
            clearInterval(passport[e.$getId("spareWData")].timer)
        },
        _createChannel: function(sign) {
            var me = this
              , qrcodeSign = sign
              , container = me.getElement("qrcodeContent")
              , qrcodeInit = baidu(".tang-pass-qrcode-init", container).get(0)
              , qrcodeImg = baidu(".tang-pass-qrcode-img", qrcodeInit).get(0)
              , data = {
                apiver: "v3",
                tt: (new Date).getTime()
            };
            passport[me.$getId("spareWData")] = passport[me.$getId("spareWData")] || {},
            passport[me.$getId("spareWData")].unicast = setTimeout(function() {
                baidu(".Qrcode-status-con", container).hide(),
                me.$show(me.getElement("QrcodeError"))
            }, 35e3),
            baidu.ajax({
                url: me._domain.https + "/channel/unicast?channel_id=" + passport[me.$getId("spareWData")].sign + "&tpl=" + me.config.product + "&gid=" + (me.guideRandom || ""),
                dataType: "jsonp",
                data: data,
                success: function(d) {
                    if (clearTimeout(passport[me.$getId("spareWData")].unicast),
                    d.channel_v)
                        try {
                            d.channel_v = eval("(" + d.channel_v + ")")
                        } catch (e) {
                            d.channel_v = {}
                        }
                    else
                        d.channel_v = {};
                    if (d.channel_v.u && (d.channel_v.u = decodeURIComponent(d.channel_v.u)),
                    0 == d.errno && 0 == d.channel_v.status) {
                        clearInterval(passport[me.$getId("spareWData")].timer);
                        var data = {
                            bduss: d.channel_v.v,
                            u: encodeURIComponent(d.channel_v.u || me.config.u),
                            loginVersion: "v4",
                            qrcode: 1,
                            tpl: me.config.product ? me.config.product : ""
                        };
                        passport.data.jsonp("/v3/login/main/qrbdusslogin?v=" + (new Date).getTime(), data).success(function(e) {
                            if (0 == e.errInfo.no) {
                                var t = me.fireEvent("loginSuccess", {
                                    rsp: e
                                })
                                  , n = {
                                    page: "loginv4",
                                    tpl: me.config.product || ""
                                }
                                  , i = {
                                    eventType: "qrcodeLoginSuccess_" + (me.config.product || "")
                                };
                                if (me._logPass(n, i),
                                !t)
                                    return;
                                window.location.href = e.data.u
                            } else {
                                var t = me.fireEvent("loginError", {
                                    rsp: e
                                })
                                  , n = {
                                    page: "loginv4",
                                    tpl: me.config.product || ""
                                }
                                  , i = {
                                    eventType: "qrcodeLoginError_" + (me.config.product || "")
                                };
                                if (me._logPass(n, i),
                                !t)
                                    return
                            }
                        })
                    } else {
                        if (0 == d.errno && "1" == d.channel_v.status) {
                            me.config.qrcode_style && (baidu(".Qrcode-status-con", container).hide(),
                            me.$show(me.getElement("QrcodeSuccess")));
                            var urlData = {
                                page: "loginv4",
                                tpl: me.config.product || ""
                            }
                              , autoStatisticObj = {
                                eventType: "qrcodeLoginSuccess_" + (me.config.product || "")
                            };
                            me._logPass(urlData, autoStatisticObj)
                        } else
                            0 == d.errno && "2" == d.channel_v.status && (clearInterval(passport[me.$getId("spareWData")].timer),
                            me.config.qrcode_style ? (baidu(".Qrcode-status-con", container).hide(),
                            baidu(".refresh-title", container).hide(),
                            baidu(".refresh-timeout", container).show(),
                            me.$show(me.getElement("QrcodeRefresh"))) : (qrcodeImg && (qrcodeImg.src = me._domain.staticFile + "/passApi/img/loading.gif"),
                            me._setChannel(),
                            passport[me.$getId("spareWData")].timer = setInterval(function() {
                                me._setChannel()
                            }, 3e5)));
                        qrcodeSign == passport[me.$getId("spareWData")].sign && me._createChannel(qrcodeSign)
                    }
                },
                error: function() {
                    clearTimeout(passport[me.$getId("spareWData")].unicast),
                    me.config.qrcode_style && (baidu(".Qrcode-status-con", container).hide(),
                    me.$show(me.getElement("QrcodeError")))
                }
            })
        },
        refreshQrcode: function() {
            var e = this;
            clearTimeout(passport[e.$getId("spareWData")].unicast);
            var t = e.getElement("qrcodeContent")
              , n = baidu(".tang-pass-qrcode-init", t).get(0)
              , i = baidu(".tang-pass-qrcode-img", n).get(0);
            i && (i.src = e._domain.staticFile + "/passApi/img/loading.gif"),
            e._setChannel(),
            passport[e.$getId("spareWData")].timer = setInterval(function() {
                e._setChannel()
            }, 3e5)
        },
        _actionQrcode: function() {
            var e = this
              , t = e.qrcodeDialogDom ? e.qrcodeDialogDom : this.getElement()
              , n = e._getWDom.parent(t);
            e._getWDom.parent(n),
            passport[e.$getId("spareWData")] = passport[e.$getId("spareWData")] || {},
            passport[e.$getId("spareWData")].channelimg || (e._setChannel(),
            passport[e.$getId("spareWData")].timer = setInterval(function() {
                e._setChannel()
            }, 3e5))
        },
        _showQrcode: function() {
            var e = this
              , t = this.getElement()
              , n = e._getWDom.parent(t)
              , i = e._getWDom.parent(n)
              , s = baidu(".pass-qrcode-btn", i).get(0);
            e._getWDom.prev(t) && e.$hide(e._getWDom.prev(t)),
            e.$hide("choiceuser_article").$hide(t).$show(baidu(".tang-pass-qrcode", n).get(0)),
            e.$hide(e._getWDom.next(s) ? s : e._getWDom.parent(e._getWDom.parent(s)))
        },
        qrcodeAnimationShow: function() {
            var e = this;
            e.supportCss3Anim() ? baidu(e.getElement("QrcodeMain")).removeClass("Qrcode-animationRight").addClass("Qrcode-animation") : baidu(e.getElement("QrcodeMain")).css("margin-left", "39px"),
            baidu(e.getElement("QrcodeAnimation")).addClass("Qrcode-status-guideAnim")
        },
        qrcodeAnimationHide: function() {
            var e = this;
            baidu(e.getElement("QrcodeAnimation")).removeClass("Qrcode-status-guideAnim"),
            e.supportCss3Anim() ? baidu(e.getElement("QrcodeMain")).removeClass("Qrcode-animation").addClass("Qrcode-animationRight") : baidu(e.getElement("QrcodeMain")).css("margin-left", "99px")
        },
        supportCss3Anim: function() {
            var e = document.getElementsByTagName("body")[0].style;
            return "undefined" != typeof e.animation || "undefined" != typeof e.WebkitAnimation ? !0 : !1
        },
        setqrcodeEvent: function() {
            var e = this;
            e.config.qrcode_animation && (baidu(e.getElement("QrcodeMain")).on("mouseenter", function(t) {
                t && t.preventDefault && t.preventDefault(),
                e.qrcodeAnimationShow()
            }),
            baidu(e.getElement("QrcodeMain")).on("mouseleave", function(t) {
                t && t.preventDefault && t.preventDefault(),
                e.qrcodeAnimationHide()
            })),
            baidu(e.getElement("QrcodeErrorfreshBtn")).on("click", function() {
                e.refreshQrcode()
            }),
            baidu(e.getElement("QrcodeRefreshBtn")).on("click", function() {
                e.refreshQrcode()
            })
        },
        _getTemplateSms: function() {
            var e = this
              , t = "none"
              , n = '<div id="' + e.$getId("sms") + '" class="tang-pass-login tang-pass-sms" style="display:' + t + '">'
              , i = {
                u: e.config.u,
                staticPage: e.config.staticPage,
                tpl: e.config.product ? e.config.product : "",
                idc: e.config.idc ? e.config.idc : "",
                isdpass: "1",
                gid: e.guideRandom || "",
                switchuname: "",
                smsCodeString: "",
                smsVcodesign: "",
                smsVcodestr: "",
                subpro: e.config.subpro,
                is_voice_sms: e.config.is_voice_sms,
                voice_sms_flag: 0
            };
            return n += '<p class="pass-form-logo">' + e.lang.toSmsBtn + "</p>",
            n += '<p class="tang-pass-sms-tip">' + (e.config.smsText || "验证即登录，未注册将自动创建百度帐号") + "</p>",
            n += '<form id="' + e.$getId("smsForm") + '" method="POST">',
            n += e._getHiddenField(i, "smsHiddenFields"),
            n += '<p id="' + e.$getId("smsErrorWrapper") + '" class="pass-generalErrorWrapper"><span id="' + e.$getId("smsError") + '" class="pass-generalError"></span></p>',
            n += '<div id="' + e.$getId("smsPhoneWrapper") + '" class="pass-form-item pass-form-item-smsPhone' + (e.foreignMobile ? " pass-form-item-PhoneCountry" : "") + '">' + (e.foreignMobile ? '<label for="' + e.$getId("smsPhone") + '" id="' + e.$getId("smsPhoneCountryLabel") + '" class="pass-label pass-label-smsPhone" data-countryCode="">+86</label>' : "") + '<input id="' + e.$getId("smsPhone") + '" type="text" name="username" class="pass-text-input pass-text-input-smsPhone" /><span id="' + e.$getId("smsPhoneTip") + '" class="pass-item-tip pass-item-tip-smsPhone" style="display:none"><span id="' + e.$getId("smsPhoneTipText") + '"></span></span>' + (e.foreignMobile ? '<ul id="' + e.$getId("smsCountryList") + '" class="pass-country-list"></ul>' : "") + "</div>",
            n += '<p id="' + e.$getId("smsVerifyCodeWrapper") + '" class="pass-form-item pass-form-item-smsVerifyCode"><input id="' + e.$getId("smsVerifyCode") + '" type="text" name="password" class="pass-text-input pass-text-input-smsVerifyCode" /><button id="' + e.$getId("smsTimer") + '" class="pass-item-timer">发送' + e.lang.smsVerifyCode + '</button><span id="' + e.$getId("smsVerifyCodeTip") + '" class="pass-item-tip pass-item-tip-smsVerifyCode" style="display:none"><span id="' + e.$getId("smsVerifyCodeTipText") + '"></span></span></p>',
            n += 1 != e.config.is_voice_sms ? '<p id="' + e.$getId("smsSubmitWrapper") + '" class="pass-form-item pass-form-item-submit"><input id="' + e.$getId("smsSubmit") + '" type="submit" value="登录" class="pass-button pass-button-submit" /><span class="tang-pass-sms-agreement pass-link">' + e.lang.agree + '<a target="_blank" href="' + e.constant.PROTOCAL_URL + '">' + e.lang.baiduUserProtocal + "</a></span>" + ('<a id="' + e.$getId("sms_btn_back") + '" class="pass-sms-link pass-sms-link-back pass-link">' + e.lang.backToLogin + "</a>") + "</p>" : '<p id="' + e.$getId("smsSubmitWrapper") + '" class="pass-form-item pass-form-item-submit"><input id="' + e.$getId("smsSubmit") + '" type="submit" value="登录" class="pass-button pass-button-submit" /><input  type="button" style="border:none;background:none;margin-top:12px;cursor:pointer;color:#2e7fdb;font-size:12px" class="pass-is_voice"  id="getVoiceSms" value="获取语音验证码" />' + ('<a id="' + e.$getId("sms_btn_back") + '" class="pass-sms-link pass-sms-link-back pass-link">' + e.lang.backToLogin + "</a>") + '</br><span class="tang-pass-sms-agreement pass-link">' + e.lang.agree + '<a target="_blank" href="' + e.constant.PROTOCAL_URL + '">' + e.lang.baiduUserProtocal + "</a></span></p>",
            n += "</form>",
            n += "</div>"
        },
        _setEventSms: function() {
            var e = this
              , t = this.getElement()
              , n = e._getWDom.parent(t)
              , i = e._getWDom.parent(n)
              , s = baidu("#" + e.$getId("sms"), i).get(0);
            baidu(".pass-text-input", s),
            e.foreignMobile && baidu(e.getElement("smsPhoneCountryLabel")).on("click", function(t) {
                var n = e.getElement("smsCountryList");
                n && "block" != n.style.display ? (e.$show(n),
                baidu(e.getElement("smsPhoneCountryLabel")).addClass("pass-label-code-up")) : n && (e.$hide(n),
                baidu(e.getElement("smsPhoneCountryLabel")).removeClass("pass-label-code-up")),
                e._selectCountryList(e.getElement("smsPhoneWrapper")),
                t.preventDefault()
            }),
            baidu(".pass-text-input", s).on("mouseover", function() {
                var t = e.fireEvent("fieldMouseover", {
                    ele: baidu(this)
                });
                t && baidu(this).addClass(e.constant.HOVER_CLASS)
            }),
            baidu(".pass-text-input", s).on("mouseout", function() {
                var t = e.fireEvent("fieldMouseout", {
                    ele: baidu(this)
                });
                t && baidu(this).removeClass(e.constant.HOVER_CLASS)
            }),
            baidu(".pass-text-input", s).on("keydown", function(t) {
                13 == t.keyCode && (t && t.preventDefault && t.preventDefault(),
                e._submitSmsForm(t))
            }),
            baidu(e.getElement("smsPhone")).on("focus", function() {
                e.initialized || e._initApi();
                var t = e.fireEvent("fieldFocus", {
                    ele: baidu(this)
                });
                if (t) {
                    baidu(this).addClass(e.constant.FOCUS_CLASS),
                    baidu(this).removeClass(e.constant.ERROR_CLASS);
                    var n = document.getElementById(e.$getId("smsRegPromptWrapper"));
                    n && e.$hide(n)
                }
            }),
            baidu(e.getElement("smsVerifyCode")).on("focus", function() {
                e.initialized || e._initApi();
                var t = e.fireEvent("fieldFocus", {
                    ele: baidu(this)
                });
                t && (baidu(this).addClass(e.constant.FOCUS_CLASS),
                baidu(this).removeClass(e.constant.ERROR_CLASS))
            }),
            baidu(".pass-text-input", s).on("blur", function() {
                if (this.value) {
                    var t = e.fireEvent("fieldBlur", {
                        ele: baidu(this)
                    });
                    if (!t)
                        return;
                    "username" === this.name ? e._validatorPhoneFn(this) : e._validatorSmsFn(this)
                }
                baidu(this).removeClass(e.constant.FOCUS_CLASS)
            }),
            baidu("#" + e.$getId("smsTimer"), s).on("click", function(t) {
                e.config.voice_sms_flag = 0,
                t.preventDefault(),
                e._checkRegPhone()
            }),
            baidu("#" + e.$getId("smsSubmit"), s).on("click", function(t) {
                t && t.preventDefault && t.preventDefault(),
                e._submitSmsForm(t)
            }),
            baidu(e.getElement("smsSwitchWrapper")).on("click", function() {
                /msie 6/i.test(navigator.userAgent) || /msie 7/i.test(navigator.userAgent) ? setTimeout(function() {
                    e._changeLoginType("sms")
                }, 0) : e._changeLoginType("sms")
            }),
            baidu(e.getElement("sms_btn_back")).on("click", function() {
                e._changeLoginType("normal"),
                e.getElement("password") && e._doFocus("password")
            }),
            baidu(document.getElementById("getVoiceSms")).on("click", function(t) {
                e.config.voice_sms_flag = 1,
                t.preventDefault(),
                e._checkRegPhone()
            })
        },
        _setSmsGeneralError: function(e) {
            this.getElement("smsError").innerHTML = e
        },
        _sendVcode: function(e) {
            var t, n = e || this, i = (n.config.voice_sms_flag,
            document.getElementById(n.$getId("smsPhone"))), s = n.getElement("smsPhoneCountryLabel") ? baidu(n.getElement("smsPhoneCountryLabel")).attr("data-countrycode") || "" : "", o = 60, r = baidu("#" + n.$getId("sms")).get(0);
            if (n._validatorPhoneFn(i)) {
                baidu("#" + n.$getId("smsRegPromptBtn"), r).off("click"),
                baidu("#" + n.$getId("smsRegPromptBtn"), r).on("click", function(e) {
                    e.preventDefault()
                }),
                baidu("#" + n.$getId("smsTimer"), r).off("click"),
                baidu("#" + n.$getId("smsTimer"), r).on("click", function(e) {
                    e.preventDefault()
                }),
                baidu("#" + n.$getId("smsTimer"), r).removeClass("pass-item-timer"),
                baidu("#" + n.$getId("smsTimer"), r).addClass("pass-item-time-timing");
                var a = {
                    gid: n.guideRandom || "",
                    username: n._SBCtoDBC(i.value),
                    countrycode: s,
                    bdstoken: n.bdPsWtoken,
                    tpl: n.config.product ? n.config.product : "",
                    loginVersion: "v4",
                    flag_code: n.config.voice_sms_flag
                };
                a.dv = document.getElementById("dv_Input") ? document.getElementById("dv_Input").value : window.LG_DV_ARG && window.LG_DV_ARG.dvjsInput || "";
                var c = "";
                c = 1 == n.config.voice_sms_flag ? window.location.protocol.toLowerCase() + "//wappass.baidu.com/wp/api/login/sms?is_voice_sms=" + n.config.voice_sms_flag : n._domain.auto + "/v2/api/senddpass",
                passport.data.jsonp(c, a).success(function(e) {
                    if (0 == n.config.voice_sms_flag && 0 != e.data.errno || 1 == n.config.voice_sms_flag && 0 != e.errInfo.no) {
                        if (18 == e.data.errno || 19 == e.data.errno || 50020 == e.errInfo.no || 50021 == e.errInfo.no) {
                            var a = n.constant.VERIFYCODE_URL_PREFIX + e.data.vcodestr;
                            n.getElement("smsHiddenFields_smsVcodesign").value = e.data.vcodesign,
                            n.getElement("smsHiddenFields_smsVcodestr").value = e.data.vcodestr,
                            confirmSmsVerifyWidget ? (n.getElement("confirmVerifyCodeImg").src = a,
                            n.getElement("confirmVerifyCode").value = "",
                            n._ownerDialog && n._ownerDialog.hide("unHide"),
                            confirmSmsVerifyWidget.show()) : passport._load(n._domain.auto + "/passApi/js/uni_wrapper.js", !0, function() {
                                confirmSmsVerifyWidget = passport.pop.init({
                                    type: "confirmWidget",
                                    tangram: !0,
                                    titleText: "安全验证",
                                    width: 490,
                                    apiOpt: {
                                        Continue: "确定",
                                        contentHTML: '<p class="pass-confirm-verifyWidget-msg">请填写图中的验证码</p><p class="pass-confirm-verifyWidget-imgWrapper"><input type="text" class="pass-text-input pass-confirm-verifyWidget-verifyCode" id="' + n.$getId("confirmVerifyCode") + '" name="confirmVerifyCode" value="" /><img src="' + a + '" title="" class="pass-confirm-verifyWidget-verifyCode-img" id="' + n.$getId("confirmVerifyCodeImg") + '" /><a href="#" class="pass-confirm-verifyWidget-imgChange" id="' + n.$getId("confirmVerifyCodeChange") + '">换一张</a><span class="pass-confirm-verifyWidget-error" id="' + n.$getId("confirmVerifyCodeError") + '"></span></p>'
                                    },
                                    onRender: function() {
                                        baidu(confirmSmsVerifyWidget.getElement("confirmWidget_footer")).addClass("pass-confirm-verifyWidget-bottom"),
                                        n.config.hasPlaceholder && n._getPlaceholder([{
                                            label: "confirmVerifyCode",
                                            placeholder: "verifyCode"
                                        }]),
                                        baidu(n.getElement("confirmVerifyCodeChange")).on("click", function() {
                                            baidu(n.getElement("confirmVerifyCodeImg")).attr("src", n.constant.VERIFYCODE_URL_PREFIX + n.getElement("smsHiddenFields_smsVcodestr").value + "&v=" + (new Date).getTime())
                                        }),
                                        baidu(n.getElement("confirmVerifyCode")).on("keyup", function() {
                                            baidu(n.getElement("confirmVerifyCode")).removeClass("pass-text-input-error"),
                                            baidu(n.getElement("confirmVerifyCodeError")).hide(),
                                            baidu(n.getElement("confirmVerifyCodeError")).get(0).innerHTML = ""
                                        })
                                    },
                                    onConfirmClose: function() {
                                        baidu(n.getElement("confirmVerifyCodeError")).hide(),
                                        baidu(n.getElement("confirmVerifyCodeError")).get(0).innerHTML = "",
                                        confirmSmsVerifyWidget.hide(),
                                        n._ownerDialog && n._ownerDialog.show()
                                    },
                                    onConfirmCancel: function() {},
                                    onConfirmContinue: function() {
                                        if ("" == n.getElement("confirmVerifyCode").value)
                                            return baidu(n.getElement("confirmVerifyCode")).addClass("pass-text-input-error"),
                                            baidu(n.getElement("confirmVerifyCodeError")).show(),
                                            void (baidu(n.getElement("confirmVerifyCodeError")).get(0).innerHTML = n.lang.confirmVerCodeEmpty);
                                        var a = document.getElementById("dv_Input")
                                          , c = {
                                            gid: n.guideRandom || "",
                                            username: n._SBCtoDBC(i.value),
                                            countrycode: s,
                                            bdstoken: n.bdPsWtoken,
                                            tpl: n.config.product ? n.config.product : "",
                                            vcodestr: n.getElement("smsHiddenFields_smsVcodestr").value,
                                            vcodesign: n.getElement("smsHiddenFields_smsVcodesign").value,
                                            verifycode: n._SBCtoDBC(n.getElement("confirmVerifyCode").value),
                                            flag_code: n.config.voice_sms_flag,
                                            loginVersion: "v4",
                                            dv: a ? a.value : window.LG_DV_ARG && window.LG_DV_ARG.dvjsInput || ""
                                        }
                                          , l = "";
                                        l = 1 == n.config.voice_sms_flag ? window.location.protocol.toLowerCase() + "//wappass.baidu.com/wp/api/login/sms?is_voice_sms=" + n.config.voice_sms_flag : n._domain.auto + "/v2/api/senddpass",
                                        passport.data.jsonp(l, c).success(function(i) {
                                            if (0 == n.config.voice_sms_flag && 0 == i.data.errno || 1 == n.config.voice_sms_flag && 0 == i.errInfo.no) {
                                                if (1 == n.config.voice_sms_flag) {
                                                    var s = 15;
                                                    document.getElementById("getVoiceSms").disabled = !0,
                                                    t = setInterval(function() {
                                                        0 == --s ? (clearInterval(t),
                                                        baidu("#" + n.$getId("smsTimer"), r).removeClass("pass-item-time-timing"),
                                                        baidu("#" + n.$getId("smsTimer"), r).addClass("pass-item-timer"),
                                                        document.getElementById("getVoiceSms").disabled = !1,
                                                        document.getElementById("getVoiceSms").value = "重新发送语音验证码",
                                                        document.getElementById(n.$getId("smsTimer")).innerHTML = "重新发送",
                                                        s = 60) : document.getElementById("getVoiceSms").value = "已发送" + s + "s"
                                                    }, 1e3)
                                                } else
                                                    t = setInterval(function() {
                                                        0 == --o ? (clearInterval(t),
                                                        baidu("#" + n.$getId("smsTimer"), r).removeClass("pass-item-time-timing"),
                                                        baidu("#" + n.$getId("smsTimer"), r).addClass("pass-item-timer"),
                                                        document.getElementById(n.$getId("smsTimer")).innerHTML = "重新发送",
                                                        o = 60) : document.getElementById(n.$getId("smsTimer")).innerHTML = "重新发送(" + o + ")"
                                                    }, 1e3);
                                                baidu(n.getElement("confirmVerifyCodeError")).hide(),
                                                baidu(n.getElement("confirmVerifyCodeError")).get(0).innerHTML = "",
                                                confirmSmsVerifyWidget.hide(),
                                                n._ownerDialog && n._ownerDialog.show()
                                            } else
                                                20 == i.data.errno || 21 == i.data.errno ? (baidu(n.getElement("confirmVerifyCode")).addClass("pass-text-input-error"),
                                                baidu(n.getElement("confirmVerifyCodeError")).show(),
                                                baidu(n.getElement("confirmVerifyCodeError")).get(0).innerHTML = i.data.msg,
                                                n.getElement("confirmVerifyCodeImg").src = n.constant.VERIFYCODE_URL_PREFIX + i.data.vcodestr,
                                                n.getElement("confirmVerifyCode").value = "",
                                                n.getElement("smsHiddenFields_smsVcodesign").value = i.data.vcodesign,
                                                n.getElement("smsHiddenFields_smsVcodestr").value = i.data.vcodestr) : 27 == e.data.errno ? document.location.href = "https://passport.baidu.com/v2/?reg&overseas=" + n.config.overseas + "&tpl=" + n.config.product + "&u=" + encodeURIComponent(n.config.u) : (baidu(n.getElement("confirmVerifyCodeError")).hide(),
                                                confirmSmsVerifyWidget.hide(),
                                                n._ownerDialog && n._ownerDialog.show(),
                                                n._setSmsGeneralError(1 == n.config.voice_sms_flag ? i.errInfo.msg : i.data.msg))
                                        })
                                    }
                                }),
                                n._ownerDialog && n._ownerDialog.hide("unHide"),
                                confirmSmsVerifyWidget.show()
                            })
                        } else
                            27 == e.data.errno ? document.location.href = "https://passport.baidu.com/v2/?reg&overseas=" + n.config.overseas + "&tpl=" + n.config.product + "&u=" + encodeURIComponent(n.config.u) : n._setSmsGeneralError(1 != n.config.voice_sms_flag ? e.data.msg : e.errInfo.msg);
                        baidu("#" + n.$getId("smsTimer"), r).addClass("pass-item-timer"),
                        baidu("#" + n.$getId("smsTimer"), r).removeClass("pass-item-time-timing"),
                        document.getElementById(n.$getId("smsTimer")).innerHTML = "重新发送"
                    } else if (1 == n.config.voice_sms_flag) {
                        var c = 15;
                        document.getElementById("getVoiceSms").disabled = !0,
                        t = setInterval(function() {
                            0 == --c ? (clearInterval(t),
                            baidu("#" + n.$getId("smsTimer"), r).removeClass("pass-item-time-timing"),
                            baidu("#" + n.$getId("smsTimer"), r).addClass("pass-item-timer"),
                            document.getElementById("getVoiceSms").disabled = !1,
                            document.getElementById("getVoiceSms").value = "重新发送语音验证码",
                            document.getElementById(n.$getId("smsTimer")).innerHTML = "重新发送",
                            c = 15) : document.getElementById("getVoiceSms").value = "已发送" + c + "s"
                        }, 1e3)
                    } else
                        t = setInterval(function() {
                            0 == --o ? (clearInterval(t),
                            baidu("#" + n.$getId("smsTimer"), r).removeClass("pass-item-time-timing"),
                            baidu("#" + n.$getId("smsTimer"), r).addClass("pass-item-timer"),
                            document.getElementById(n.$getId("smsTimer")).innerHTML = "重新发送",
                            o = 60) : document.getElementById(n.$getId("smsTimer")).innerHTML = "重新发送(" + o + ")"
                        }, 1e3);
                    baidu("#" + n.$getId("smsTimer"), r).on("click", function(e) {
                        n.config.voice_sms_flag = 0,
                        e.preventDefault(),
                        n._checkRegPhone()
                    })
                })
            }
        },
        _validatorPhoneFn: function(e) {
            var t = this;
            if ("" == e.value)
                return t._setSmsGeneralError("请填写手机号"),
                baidu(e).addClass(t.constant.ERROR_CLASS),
                !1;
            if (t.getElement("smsPhoneCountryLabel") && "" != baidu(t.getElement("smsPhoneCountryLabel")).attr("data-countrycode")) {
                if (!new RegExp(/^(\d)*$/).test(t._SBCtoDBC(e.value)))
                    return t._setSmsGeneralError("手机号码格式不正确"),
                    baidu(e).addClass(t.constant.ERROR_CLASS),
                    !1
            } else if (!new RegExp(/^1[3456789]\d{9}$/).test(t._SBCtoDBC(e.value)))
                return t._setSmsGeneralError("手机号码格式不正确"),
                baidu(e).addClass(t.constant.ERROR_CLASS),
                !1;
            return t._setSmsGeneralError(""),
            baidu(e).removeClass(t.constant.ERROR_CLASS),
            !0
        },
        _validatorSmsFn: function(e) {
            var t = this;
            return "" == e.value ? (t._setSmsGeneralError("请填写验证码"),
            baidu(e).addClass(t.constant.ERROR_CLASS),
            !1) : (t._setSmsGeneralError(""),
            !0)
        },
        _postSmsData: function(e) {
            var t = this;
            e.countrycode = t.getElement("smsPhoneCountryLabel") ? baidu(t.getElement("smsPhoneCountryLabel")).attr("data-countrycode") || "" : "",
            e.token = t.bdPsWtoken,
            e.loginVersion = "v4",
            passport.data.traceID && passport.data.traceID.startFlow && passport.data.traceID.startFlow("login"),
            e.dv = document.getElementById("dv_Input") ? document.getElementById("dv_Input").value : window.LG_DV_ARG && window.LG_DV_ARG.dvjsInput || "",
            passport.data.login(e).success(function(e) {
                if (e.loginType = "sms",
                0 == e.errInfo.no) {
                    var n = t.fireEvent("loginSuccess", {
                        rsp: e
                    });
                    if (!n)
                        return;
                    window.location.href = e.data.u
                } else {
                    t.getElement("smsSubmit").style.color = "#fff";
                    var n = t.fireEvent("loginError", {
                        rsp: e
                    });
                    if (!n)
                        return;
                    t._setSmsGeneralError(4 == e.errInfo.no ? t.lang.captchaErr : e.errInfo.msg),
                    (3 == e.errInfo.no || 4 == e.errInfo.no) && t._clearInput("smsVerifyCode")
                }
            })
        },
        smsLoginSubmit: function(e) {
            var t = this
              , e = e || {}
              , n = baidu.form.json(t.getElement("smsForm"));
            e.errInfo && 3 == e.errInfo.no ? passport.data.post("/v2/unite-bind", {
                username: e.data.username || "",
                password: n.password,
                countrycode: t.getElement("smsPhoneCountryLabel") ? baidu(t.getElement("smsPhoneCountryLabel")).attr("data-countrycode") || "" : "",
                sms: 1,
                apiver: "v3",
                loginVersion: "v4",
                token: e.data.token || ""
            }).success(function() {
                t._postSmsData(n)
            }) : t._postSmsData(n)
        },
        _submitSmsForm: function() {
            function e() {
                t._postSmsData(o)
            }
            var t = this
              , n = document.getElementById(t.$getId("smsPhone"))
              , i = document.getElementById(t.$getId("smsVerifyCode"));
            if (!t._validatorPhoneFn(n))
                return void n.focus();
            if (t._validatorSmsFn(i)) {
                var s = t.fireEvent("beforeSubmit");
                if (s) {
                    t.getElement("smsSubmit").style.color = "#9ebef4";
                    var o = baidu.form.json(t.getElement("smsForm"));
                    o.password = t._SBCtoDBC(o.password),
                    o.username = t._SBCtoDBC(o.username),
                    o.FP_UID = t._getCookie("FP_UID") || "",
                    o.FP_INFO = window.PP_FP_INFO || "",
                    t.loginConnect({
                        username: o.username,
                        password: o.password,
                        countrycode: t.getElement("smsPhoneCountryLabel") ? baidu(t.getElement("smsPhoneCountryLabel")).attr("data-countrycode") || "" : "",
                        smsVcode: o.password,
                        isdpass: 1,
                        sms: 1
                    }, {
                        fail: function(e) {
                            t._setSmsGeneralError(e)
                        }
                    }, e)
                }
            }
        },
        _setEventChoiceUser: function() {
            var e = this
              , t = function() {
                baidu(e.getElement()).removeClass("tang-pass-login-hide"),
                e.$show(e.getElement()).$hide("choiceuser_article")
            }
              , n = function() {
                baidu(e.getElement()).removeClass("tang-pass-login-hide"),
                e.$show(e.getElement()).$hide("choiceuser_article"),
                e.submit()
            };
            baidu(e.getElement("choiceuser_btn_username")).on("click", function(t) {
                e.getElement("loginMerge").value = "false",
                n(t)
            }),
            baidu(e.getElement("choiceuser_btn_mobile")).on("click", function(t) {
                e.getElement("isPhone").value = "true",
                e.getElement("loginMerge").value = "false",
                n(t)
            }),
            baidu(e.getElement("choiceuser_btn_back")).on("click", function(e) {
                e.preventDefault(),
                t()
            })
        },
        _getToken: function(e) {
            var t = this;
            passport[t.$getId("spareWData")] = passport[t.$getId("spareWData")] || {},
            passport.data.getApiInfo({
                apiType: "login",
                loginVersion: "v4",
                gid: t.guideRandom || ""
            }).success(function(n) {
                t.bdPsWtoken = n.data.token,
                e && e(t)
            })
        },
        _getRSA: function(e) {
            var t = this;
            passport.data.getRsaKey({
                gid: t.guideRandom || "",
                loginVersion: "v4"
            }).success(function(t) {
                t.errInfo.no || 0 == t.errInfo.no || (t = t.data);
                var n = new passport.lib.RSA;
                n.setKey(t.pubkey),
                e && e({
                    RSA: n,
                    rsakey: t.key
                })
            })
        },
        _changeLoginType: function(e) {
            var t = this
              , n = this.getElement()
              , i = t._getWDom.parent(n)
              , s = t._getWDom.parent(i)
              , o = (t.getElement("qrcode"),
            t.getElement("sms"),
            baidu(".tang-pass-login-phoenix", s).get(0),
            {
                normal: {
                    $btn: baidu(".pass-normal-btn", t.getPhoenixElement("pass_phoenix_list_login")),
                    $ele: baidu(t.getElement("form")).parent()
                },
                sms: {
                    $btn: baidu(".pass-sms-btn", t.getPhoenixElement("pass_phoenix_list_login")),
                    $ele: baidu(t.getElement("sms"))
                },
                qrcode: {
                    $btn: baidu(".pass-qrcode-btn", t.getPhoenixElement("pass_phoenix_list_login")),
                    $ele: baidu(t.getElement("qrcode"))
                }
            })
              , r = t.getElement("choiceuser_article");
            e = e || "normal",
            r && t.$hide("choiceuser_article");
            var a = t.fireEvent("changeLoginType", {
                loginType: e,
                currentLoginType: t.currentLoginType || ""
            });
            if (a) {
                for (var c in o)
                    o[c].$ele && o[c].$ele.length > 0 && (c == e ? t.$show(o[c].$ele[0]) : t.$hide(o[c].$ele[0]));
                "qrcode" === e && t._actionQrcode(),
                t.currentLoginType = e
            }
        },
        _doFocus: function(e) {
            var t = this;
            t.config.autoFocus && ("string" == (typeof e).toLowerCase() && t.getElement(e) ? t.getElement(e).focus() : e.focus())
        },
        _clearInput: function(e) {
            var t = this
              , n = t.getElement(e)
              , i = t.getElement(e + "_placeholder")
              , s = t.getElement(e + "_clearbtn");
            n && (i && t.$show(i),
            s && t.$hide(i),
            n.value = "",
            t._doFocus(n))
        },
        _insertAfterW: function(e, t) {
            var n = this
              , i = n._getWDom.parent(t);
            i.lastChild == t ? i.appendChild(e) : i.insertBefore(e, n._getWDom.next(t))
        },
        _insertNoCaptchaScript: function() {
            var e = this;
            e._insertScriptW(e.constant.NOCAPTCHA_URL, function() {})
        },
        _checkCapsLock: function() {
            var e = this
              , t = baidu(e.getElement("password"));
            t.on("keypress", function(t) {
                var n = t || window.event
                  , i = n.keyCode || n.which
                  , s = n.shiftKey || 16 == i || !1
                  , o = document.getElementById(e.$getId("caps"));
                if (i >= 65 && 90 >= i && !s || i >= 97 && 122 >= i && s)
                    if (o)
                        e.$show(o);
                    else {
                        var r = document.createElement("span");
                        r.id = e.$getId("caps"),
                        r.innerHTML = "大小写锁定已打开";
                        var a = document.getElementById(e.$getId("passwordWrapper"));
                        "static" == a.style.position && (a.style.position = "relative"),
                        a.style.zIndex = a.style.zIndex ? a.style.zIndex + 1 : 20,
                        r.style.cssText = 'position:absolute;left:60px;clear:both;top:25px;width:103px;height:37px;font-size:12px;line-height:45px;z-index:20;text-align:center;background:url("' + e._domain.staticFile + '/passApi/img/caps.gif") no-repeat 0 0;',
                        a.appendChild(r)
                    }
                else
                    o && e.$hide(o)
            }),
            t.on("blur", function() {
                var t = document.getElementById(e.$getId("caps"));
                t && e.$hide(t)
            })
        },
        _checkRegPhone: function() {
            var e = this
              , t = e.getElement("smsPhoneCountryLabel") ? baidu(e.getElement("smsPhoneCountryLabel")).attr("data-countrycode") || "" : ""
              , n = document.getElementById(e.$getId("smsPhone"));
            e._validatorPhoneFn(n) && passport.data.getphonestatus({
                gid: e.guideRandom || "",
                phone: e._SBCtoDBC(n.value),
                loginVersion: "v4",
                countrycode: t
            }).success(function(i) {
                var s = e.fireEvent("_checkRegPhone", {
                    rsp: i
                });
                if (s)
                    if (0 == i.errInfo.no)
                        e.config.sendVcodeBefore && "function" == typeof e.config.sendVcodeBefore ? e.config.sendVcodeBefore(e, e._sendVcode, function() {
                            n.value = "",
                            n.focus()
                        }) : e.bdPsWtoken ? e._sendVcode() : e._getToken(e._sendVcode);
                    else if (3 == i.errInfo.no) {
                        var o = e.config.voice_sms_flag
                          , r = document.getElementById(e.$getId("smsRegPromptWrapper"))
                          , a = document.getElementById(e.$getId("smsPhoneWrapper"));
                        if (r)
                            e.$show(r),
                            e.getElement("smsRegPromptBtn").focus();
                        else {
                            var c = document.createElement("div");
                            c.id = e.$getId("smsRegPromptWrapper"),
                            c.setAttribute("class", "pass-form-sms-checkphone"),
                            c.style.cssText = 'position:absolute;clear:both;color:#826f33;z-index:999;font-size:12px;width:211px;height:75px;padding:16px 16px 11px 13px;background:url("' + e._domain.staticFile + '/passApi/img/smsRegphone.png") 0px 0px no-repeat;right:0px;',
                            c.innerHTML = '<p style="margin:0px;padding:0px;line-height:2em;">您的手机号码尚未注册，点击注册，帮您注册新的百度帐号</p><button id="' + e.$getId("smsRegPromptBtn") + '" style="background:#2e82ff;border:none;color:#fff;cursor:pointer;height:25px;line-height:25px;width:60px;text-align:center;position:absolute;right:16px;top:66px;" hidefocus=true>注册</button>',
                            a.appendChild(c),
                            e.getElement("smsRegPromptBtn").focus()
                        }
                        baidu(e.getElement("smsRegPromptBtn")).on("click", function(i) {
                            e.config.voice_sms_flag = o,
                            e.getElement("smsRegPromptWrapper") && baidu(e.getElement("smsRegPromptWrapper")).hide(),
                            i.preventDefault(),
                            "" != t ? window.location.href = e.constant.REG_URL : e.config.sendVcodeBefore && "function" == typeof e.config.sendVcodeBefore ? e.config.sendVcodeBefore(e, e._sendVcode, function() {
                                n.value = "",
                                n.focus()
                            }) : e.bdPsWtoken ? e._sendVcode() : e._getToken(e._sendVcode)
                        }),
                        e.config.voice_sms_flag = 0
                    } else
                        e.config.voice_sms_flag = 0,
                        e._setSmsGeneralError(i.errInfo.msg)
            })
        },
        changeSuggestView: function(e) {
            var t = this;
            t.suggestionDom && e.list && ("hide" == e.list ? t.$hide(t.suggestionDom) : "show" == e.list && t.$show(t.suggestionDom)),
            t.selectBtn && e.btn && ("close" == e.btn ? (baidu(t.selectBtn).removeClass("open"),
            baidu(t.getElement("userName")).addClass("open"),
            t.$show(t.selectBtn)) : "open" == e.btn ? (baidu(t.selectBtn).addClass("open"),
            baidu(t.getElement("userName")).addClass("open"),
            t.$show(t.selectBtn)) : "hide" == e.btn ? (t.$hide(t.selectBtn),
            baidu(t.getElement("userName")).removeClass("open")) : "show" == e.btn && (t.$show(t.selectBtn),
            baidu(t.getElement("userName")).addClass("open")),
            t.$hide(t.selectBtn))
        },
        _suggestion: function(e) {
            var t = this
              , n = []
              , i = baidu("#" + t.$getId("userName"), t.getElement())
              , s = ["qq.com", "163.com", "126.com", "sohu.com", "sina.com", "gmail.com", "21cn.com", "hotmail.com", "vip.qq.com", "yeah.net", "139.com"]
              , o = /^([a-zA-Z0-9_.\-+]+)([@]?[a-zA-Z0-9_\-*]*[.]?[a-zA-Z*]*[.]?[a-zA-Z*]*)$/
              , r = function(e, t) {
                var n = e;
                return e.substr(0, e.indexOf("@") - 1).length > t.maxlength && (n = e.substr(0, t.maxlength - 4) + "…" + e.substr(e.indexOf("@"))),
                baidu('<li class="pass-item-suggsetion" data-select="' + e + '" data-type="' + (t.ifdelete ? "history" : "normal") + '">' + n + (t.ifdelete ? '<a data-delete="' + e + '" title="删除该记录"></a>' : "") + "</li>").get(0)
            }
              , a = function(e, i) {
                t.suggestionDom || (t.suggestionDom = document.createElement("ul"),
                t.suggestionDom.id = t.$getId("suggestionWrapper"),
                baidu(t.getElement("userNameWrapper")).append(t.suggestionDom),
                baidu(t.suggestionDom).addClass("pass-suggestion-list"),
                baidu(t.suggestionDom).on("click", function(e) {
                    var s = baidu(e.target)
                      , o = s.attr("data-delete")
                      , r = s.attr("data-select");
                    if (o)
                        e.preventDefault(),
                        passport.data.getLoginHistory({
                            token: t.bdPsWtoken,
                            loginVersion: "v4",
                            item: o
                        }),
                        t.suggestionDom.data_delete = !0,
                        baidu(s.parent()).hide(),
                        baidu.array(n).remove(o),
                        n.length < 1 && t.changeSuggestView({
                            list: " hide",
                            btn: "hide"
                        }),
                        t._doFocus("userName"),
                        setTimeout(function() {
                            t.suggestionDom.data_delete = !1
                        }, 200);
                    else {
                        "history" == s.attr("data-type") ? i.value = r : (t.suggestionDom.data_delete = !1,
                        i.value = r || i.value),
                        t.getElement("userName_placeholder") && t.$hide("userName_placeholder"),
                        t.changeSuggestView({
                            list: "hide",
                            btn: "close"
                        }),
                        t._doFocus(i),
                        setTimeout(function() {
                            t.setGeneralError(""),
                            baidu(i).removeClass("pass-text-input-error"),
                            t._doFocus("password")
                        }, 100);
                        var a = t.getElement("userName").value;
                        t._loginCheck(a)
                    }
                })),
                t.suggestionDom.innerHTML = "",
                t.$show(t.suggestionDom),
                t.suggestionDom.appendChild(e),
                baidu(".pass-item-suggsetion", t.suggestionDom).on("mouseover", function() {
                    baidu(".pass-item-suggsetion_hover", t.suggestionDom).removeClass("pass-item-suggsetion_hover"),
                    baidu(this).addClass("pass-item-suggsetion_hover")
                }),
                baidu(".pass-item-suggsetion", t.suggestionDom).on("mouseout", function() {
                    baidu(this).removeClass("pass-item-suggsetion_hover")
                })
            };
            !function() {
                if (n = t.loginrecord.displayname || [],
                n.length > 0) {
                    for (var i = document.createDocumentFragment(), s = 0, o = n.length; o > s; s++)
                        i.appendChild(r(n[s], {
                            maxlength: e,
                            ifdelete: !0
                        }));
                    a(i, t.getElement("userName")),
                    t.selectBtn = baidu('<span class="pass-item-selectbtn pass-item-selectbtn-userName" ></span>').get(0),
                    t.getElement("userNameWrapper").appendChild(t.selectBtn),
                    baidu(t.selectBtn).on("click", function() {
                        setTimeout(function() {
                            t.changeSuggestView("none" != t.suggestionDom.style.display ? {
                                list: "hide",
                                btn: "close"
                            } : {
                                list: "show",
                                btn: "open"
                            })
                        }, 200)
                    }),
                    t.changeSuggestView({
                        list: "hide",
                        btn: "show"
                    })
                }
            }(),
            i.on("keyup", function(i) {
                if (1 == t.disUnameLogin)
                    ;
                else {
                    var c, l = document.createDocumentFragment(), d = this, u = 0;
                    if (n.length > 0)
                        for (var p = 0, g = n.length; g > p; p++)
                            0 == n[p].indexOf(this.value) && (l.appendChild(r(n[p], {
                                maxlength: e,
                                ifdelete: !0
                            })),
                            ++u);
                    if ((n.length < 1 || 1 > u) && (c = o.exec(this.value),
                    c && c[2]))
                        for (var p = 0, g = s.length; g > p; p++)
                            if (0 == ("@" + s[p]).indexOf(c[2])) {
                                var h = c[1];
                                l.appendChild(r(h + "@" + s[p], {
                                    maxlength: e
                                })),
                                ++u
                            }
                    if (t.suggestionDom && 38 !== i.keyCode && 40 !== i.keyCode && t.$hide(t.suggestionDom),
                    n.length > 1 && u > 0 && (38 !== i.keyCode && 40 !== i.keyCode && a(l, d),
                    (38 == i.keyCode || 40 == i.keyCode) && "none" != t.suggestionDom.style.display)) {
                        for (var f = t.suggestionDom.childNodes, m = f.length, v = -1, b = 0; m > b; b++)
                            f[b].className.indexOf("pass-item-suggsetion_hover") > -1 && (v = b);
                        38 == i.keyCode && (q = -1 === v ? m - 1 : 0 === v ? m - 1 : v - 1),
                        40 == i.keyCode && (q = -1 === v ? 0 : v === m - 1 ? 0 : v + 1),
                        baidu(".pass-item-suggsetion_hover", t.suggestionDom).removeClass("pass-item-suggsetion_hover"),
                        baidu(f[q], t.suggestionDom).addClass("pass-item-suggsetion_hover");
                        var y = baidu(f[q]).attr("data-select");
                        d.value = "history" == baidu(f[q]).attr("data-type") ? y : d.value.substr(0, d.value.indexOf("@")) + y.substr(y.indexOf("@")),
                        t.getElement("userName_placeholder") && t.$hide("userName_placeholder")
                    }
                }
            }),
            i.on("keydown", function(e) {
                13 != e.keyCode && 9 != e.keyCode || !t.suggestionDom || "none" == t.suggestionDom.style.display || (t.changeSuggestView({
                    list: "hide",
                    btn: "close"
                }),
                t._doFocus("password"),
                e.preventDefault(),
                e.stopPropagation())
            }),
            i.on("blur", function() {
                setTimeout(function() {
                    t.suggestionDom && !t.suggestionDom.data_delete && t.changeSuggestView({
                        list: "hide",
                        btn: "close"
                    })
                }, 150)
            }),
            i.on("focus", function() {
                t.changeSuggestView({
                    list: "show",
                    btn: "open"
                })
            })
        },
        _initCountryCode: function(e) {
            var t = this
              , n = '<li class="pass-item-country"><span class="pass-country-code" data-countryCode="">+86</span>中国</li>'
              , i = t.countryCodeList || {}
              , s = i.length;
            if (!(0 >= s)) {
                for (var o = 0; s > o; o++)
                    n += '<li class="pass-item-country"><span class="pass-country-code" data-countryCode=' + i[o].code + ">+" + i[o].code.substring(2) + "</span>" + i[o].name + "</li>";
                baidu(e).html(n)
            }
        },
        _getCountryCode: function(e) {
            var t = this
              , n = {
                apiver: "v3",
                loginVersion: "v4",
                subpro: t.config.subpro
            };
            passport.data.jsonp("https://passport.baidu.com/v2/?securitygetcountrycode", n).success(function(n) {
                n.data.country.length > 0 && (t.countryCodeList = n.data.country,
                t.getElement("foreignCountryList") && t._initCountryCode(t.getElement("foreignCountryList")),
                t.getElement("smsCountryList") && t._initCountryCode(t.getElement("smsCountryList")),
                e && e())
            })
        },
        _selectCountryList: function(e) {
            var t = this
              , n = baidu(e)
              , i = n.find(".pass-country-list").eq(0)
              , s = n.find(".pass-label");
            0 != s.length && (i.on("click", function(n) {
                var o = n.target;
                "li" === o.tagName.toLowerCase() ? (s.eq(0).html(baidu(o).find("span.pass-country-code").eq(0).html()),
                s.eq(0).attr("data-countryCode", baidu(o).find("span.pass-country-code").eq(0).attr("data-countryCode"))) : "span" === o.tagName.toLowerCase() && (s.eq(0).html(baidu(o).html()),
                s.eq(0).attr("data-countryCode", baidu(o).attr("data-countryCode"))),
                t.$hide(i[0]),
                s.eq(0).removeClass("pass-label-code-up"),
                e == t.getElement("foreignMobileWrapper") && t.getElement("foreignMobile") && t.getElement("foreignMobile").value ? t._validatorforeignmobileFn(t.getElement("foreignMobile")) : e == t.getElement("smsPhoneWrapper") && t.getElement("smsPhone") && t.getElement("smsPhone").value && t._validatorPhoneFn(t.getElement("smsPhone")),
                n.preventDefault()
            }),
            i.on("mouseover", function(e) {
                var t = e.target;
                "li" === t.tagName.toLowerCase() ? (n.find(".pass-item-country-hover").removeClass("pass-item-country-hover"),
                baidu(t).addClass("pass-item-country-hover")) : "span" === t.tagName.toLowerCase() && (n.find(".pass-item-country-hover").removeClass("pass-item-country-hover"),
                baidu(t).parent("li.pass-item-country").addClass("pass-item-country-hover"))
            }),
            i.on("mouseout", function(e) {
                var t = e.target;
                "li" === t.tagName.toLowerCase() ? baidu(t).removeClass("pass-item-country-hover") : "span" === t.tagName.toLowerCase() && baidu(t).parent("li.pass-item-country").removeClass("pass-item-country-hover")
            }),
            baidu("html").on("click", function(e) {
                var n = e.target;
                return s ? void (baidu(n).attr("id") != baidu(t.getElement("foreignMobileLabel")).attr("id") && baidu(n).attr("id") != baidu(t.getElement("smsPhoneCountryLabel")).attr("id") && setTimeout(function() {
                    t.$hide(i[0]),
                    s.eq(0).removeClass("pass-label-code-up")
                }, 200)) : !1
            }))
        },
        _setForeignMobileEvent: function() {
            var e = this;
            e.getElement("foreignMobileLabel") && baidu(e.getElement("foreignMobileLabel")).on("click", function(t) {
                var n = e.getElement("foreignCountryList");
                n && "block" !== n.style.display ? (e.$show(n),
                baidu(e.getElement("foreignMobileLabel")).addClass("pass-label-code-up")) : n && (e.$hide(n),
                baidu(e.getElement("foreignMobileLabel")).removeClass("pass-label-code-up")),
                e._selectCountryList(e.getElement("foreignMobileWrapper")),
                t.preventDefault()
            }),
            e.getElement("foreignMobile") && (baidu(e.getElement("foreignMobile")).on("blur", function() {
                if (this.value) {
                    var t = e.fireEvent("fieldBlur", {
                        ele: baidu(this)
                    });
                    if (!t)
                        return;
                    e._validatorforeignmobileFn(this)
                }
                baidu(this).removeClass(e.constant.FOCUS_CLASS)
            }),
            baidu(e.getElement("foreignMobile")).on("focus", function() {
                e.initialized || e._initApi();
                var t = e.fireEvent("fieldFocus", {
                    ele: baidu(this)
                });
                t && (baidu(this).addClass(e.constant.FOCUS_CLASS),
                baidu(this).removeClass(e.constant.ERROR_CLASS))
            })),
            e.getElement("foreignMobileLink") && baidu(e.getElement("foreignMobileLink")).on("click", function(t) {
                e.$hide(e.getElement("userNameWrapper")),
                e.$hide(e.getElement("smsSwitchWrapper")),
                e.$hide(e.getElement("foreignMobileLink")),
                baidu(e.getElement("userName")).removeClass(e.constant.ERROR_CLASS),
                e.setGeneralError(""),
                e.getElement("password").value = "",
                e.$show(e.getElement("foreignMobileWrapper")),
                e.$show(e.getElement("foreignMobileMsg")),
                e.$show(e.getElement("foreignMobileBackWrapper")),
                e.internation = !0,
                t.preventDefault();
                var n = {
                    page: "loginv4",
                    tpl: e.config.product || ""
                }
                  , i = {
                    eventType: "foreignMobileLinkClick"
                };
                e._logPass(n, i)
            }),
            e.getElement("foreignMobileBackWrapper") && baidu(e.getElement("foreignMobileBackWrapper")).on("click", function(t) {
                e.$hide(e.getElement("foreignMobileWrapper")),
                e.$hide(e.getElement("foreignMobileMsg")),
                e.$hide(e.getElement("foreignMobileBackWrapper")),
                baidu(e.getElement("foreignMobile")).removeClass(e.constant.ERROR_CLASS),
                e.setGeneralError(""),
                e.getElement("password").value = "",
                e.$show(e.getElement("userNameWrapper")),
                e.$show(e.getElement("smsSwitchWrapper")),
                e.$show(e.getElement("foreignMobileLink")),
                e.internation = !1,
                t.preventDefault()
            })
        },
        _validatorforeignmobileFn: function(e) {
            var t = this;
            if ("" == e.value)
                return t.setGeneralError("请填写手机号"),
                baidu(e).addClass(t.constant.ERROR_CLASS),
                !1;
            if (t.getElement("foreignMobileLabel") && "" != baidu(t.getElement("foreignMobileLabel")).attr("data-countrycode")) {
                if (!new RegExp(/^(\d)*$/).test(t._SBCtoDBC(e.value)))
                    return t.setGeneralError("手机号码格式不正确"),
                    baidu(e).addClass(t.constant.ERROR_CLASS),
                    !1
            } else if (!new RegExp(/^1[3456789]\d{9}$/).test(t._SBCtoDBC(e.value)))
                return t.setGeneralError("手机号码格式不正确"),
                baidu(e).addClass(t.constant.ERROR_CLASS),
                !1;
            return t.setGeneralError(""),
            baidu(e).removeClass(t.constant.ERROR_CLASS),
            !0
        },
        _rendPhoenixbtn: function() {
            var e = this
              , t = baidu(e.getPhoenixElement("pass_phoenix_list_login"));
            t.on("click", function(t) {
                var n = baidu(t.target)
                  , i = n.attr("data-type");
                i && e._changeLoginType(i)
            })
        },
        setMakeText: function(e) {
            var t = this
              , n = t.getElement("MakeTextWrapper")
              , e = e.replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/\x22/g, "&quot;").replace(/\x27/g, "&#39;");
            n && (e ? (n.style.display = "",
            n.innerHTML = e) : (n.style.display = "none",
            n.innerHTML = ""))
        },
        render: function(e) {
            var t = this;
            t.getElement() || t.$mappingDom("", e || document.body);
            var n = baidu(t.getElement());
            n.addClass(t.constant.CONTAINER_CLASS);
            var i = t._getTemplate();
            if (n.get(0).appendChild(baidu(i).get(0)),
            t.config.makeText && t.setMakeText(t.config.makeText),
            t.config.setWebToClient) {
                var s = t._getIrregularField("webtoclint");
                t._insertAfterW(baidu(s).get(0), t.getElement())
            }
            var o = t.getTemplateFooterBar();
            if (t._insertAfterW(baidu(o).get(0), n.get(0)),
            t.setEventFooterBar(),
            t.config.authsiteLogin && t.config.authsiteLogin.length > 0) {
                var r = t._getTemplateOther();
                t.getElement("PhoenixItem").innerHTML = r,
                t._rendPhoenixbtn(),
                t._authSiteW()
            }
            if (3 === t.config.qrcode) {
                var a = t._getTemplateQrcode();
                "[object function]" == Object.prototype.toString.call(t.config.qrcodeDom).toLowerCase() && t.config.diaPassLogin && 3 == t.config.qrcode ? (t.qrcodeDialogDom = t.config.qrcodeDom(),
                t.qrcodeDialogDom.appendChild(baidu(a).get(0)),
                setTimeout(function() {
                    t._actionQrcode()
                }, 500),
                t.getElement("qrcode").style.display = "") : (t._insertAfterW(baidu(a).get(0), n.get(0)),
                t._setEventQrcode()),
                t.setqrcodeEvent()
            }
            if (t.smsConfig) {
                var a = t._getTemplateSms();
                t._insertAfterW(baidu(a).get(0), n.get(0)),
                t._setEventSms()
            }
            if (setTimeout(function() {
                t.getElement("loginMerge").value = "true"
            }, 200),
            t.config.hasPlaceholder) {
                var c = [{
                    label: "userName",
                    placeholder: "userName"
                }, {
                    label: "password",
                    placeholder: "password"
                }, {
                    label: "verifyCode",
                    placeholder: "verifyCode"
                }];
                t.smsConfig && (c.push({
                    label: "smsPhone",
                    placeholder: t.config && t.config.diaPassLogin ? "smsPhoneMsg" : "smsPhone"
                }),
                c.push({
                    label: "smsVerifyCode",
                    placeholder: "smsVerifyPlaceholder"
                })),
                t.foreignMobile && c.push({
                    label: "foreignMobile",
                    placeholder: t.config && t.config.diaPassLogin ? "smsPhoneMsg" : "smsPhone"
                }),
                t._getPlaceholder(c)
            }
            t.foreignMobile && (t._getCountryCode(),
            t._setForeignMobileEvent());
            var l = {
                page: "loginv4",
                tpl: t.config.product || ""
            }
              , d = {
                eventType: "loginShow"
            };
            t._logPass(l, d);
            var u = t.fireEvent("render");
            u && (t._setValidator(),
            t._setEvent(),
            t._checkCapsLock())
        },
        _initApi: function(e) {
            var t = this;
            t.initialized = !0,
            t.initTime = (new Date).getTime(),
            passport.data.getApiInfo({
                apiType: "login",
                gid: t.guideRandom || "",
                loginVersion: "v4",
                loginType: t.config && t.config.diaPassLogin ? "dialogLogin" : "basicLogin"
            }).success(function(n) {
                var i = t.fireEvent("getApiInfo", {
                    rsp: n
                });
                if (i && (1 == n.data.disable && t.setGeneralError(t.lang.sysUpdate),
                0 == n.errInfo.no)) {
                    var s = n.data.token;
                    t.bdPsWtoken = n.data.token,
                    t.loginrecord = {},
                    t.config.autosuggest ? passport.data.getLoginHistory({
                        token: t.bdPsWtoken,
                        tt: (new Date).getTime(),
                        loginVersion: "v4",
                        gid: t.guideRandom
                    }).success(function(e) {
                        t.loginrecord = e.data,
                        t._suggestion(t.config.diaPassLogin ? 20 : 12),
                        t.config.memberPass && t.loginrecord.displayname.length > 0 && (t._doFocus("password"),
                        t.getElement("userName_placeholder") && t.$hide("userName_placeholder"),
                        t.getElement("userName").value && "" != t.getElement("userName").value || (t.getElement("userName").value = t.loginrecord.displayname[0],
                        t._loginCheck(t.loginrecord.displayname[0])),
                        t.$show("userName_clearbtn").$hide("userName_placeholder"))
                    }) : t.config.memberPass && !t.constant.SUBMITFLAG && (t.getElement("userName").value = n.data.rememberedUserName);
                    var o = (navigator.userAgent,
                    !navigator.userAgent.match(/OS [1-8]_\d[_\d]* like Mac OS X/i))
                      , r = !!navigator.userAgent.toString().match(/\(i[^;]+;( U;)? CPU.+Mac OS X/)
                      , a = navigator.userAgent.toString().indexOf("iPad");
                    if (o && r && null != a) {
                        var c = document.getElementsByClassName("popBox");
                        null != c && c.length > 0 && (c[0].style.height = window.screen.height > document.body.clientHeight ? window.screen.height * (window.screen.height / document.body.clientHeight) + 120 + "px" : window.screen.height * (window.screen.height / document.body.clientHeight))
                    }
                    t.disUnameLogin = 0,
                    t.ifShowWarning = n.data.ifShowWarning,
                    n.data.spLogin && t.config.diaPassLogin && (t.spLogin = n.data.spLogin),
                    passport.data.setContext({
                        token: s
                    }),
                    navigator.cookieEnabled || t.setGeneralError(t.lang.cookieDisable),
                    t.constant.SUBMITFLAG ? t.getElement("submit").click() : e && e.success(n)
                }
            })
        },
        submitForm: function() {
            var e = this;
            e.constant.SUBMITFLAG = !0
        },
        setSubpro: function(e) {
            var t = this;
            t.getElement("subpro") && e && (t.getElement("subpro").value = e.replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/\x22/g, "&quot;").replace(/\x27/g, "&#39;"))
        },
        _setValidator: function() {
            var e = this;
            e.validatorInited || (e._validator.addRule("unameMailLength", function(e) {
                var t = String(e.value);
                return /^[0-9a-zA-Z\.\_-]+@([0-9a-zA-Z-]+\.)+[a-z]{2,4}$/.test(t) ? t.length <= 60 : !0
            }),
            e._validator.addMsg("unameMailLength", e.lang.unameMailLengthError),
            e._validator.addRule("unameInputLogin", function(t) {
                var n = String(t.value);
                return 0 == e.disUnameLogin && e.config.diaPassLogin && !/^[0-9a-zA-Z\.\_-]+@([0-9a-zA-Z-]+\.)+[a-z]{2,4}$/.test(n) ? !1 : !0
            }),
            e._validator.addMsg("unameInputLogin", e.lang.unameInputError),
            e._validator.addRule("checkVcodeLength", function(t) {
                return t.value,
                e.constant.CHECKVERIFYCODE ? !0 : (e.$hide("verifyCodeSuccess"),
                !1)
            }),
            e._validator.addMsg("checkVcodeLength", e.lang.verifyCodeLenErr),
            e._validator.addRule("checkVcodeStatus", function(t, n) {
                return "all" != n || e.constant.CHECKVERIFYCODE ? !0 : !1
            }),
            e._validator.addMsg("checkVcodeStatus", e.lang.verifyCodeStaErr)),
            e.validatorInited = !0,
            e.validateRules = {
                userName: {
                    rules: ["required"],
                    desc: e.lang.userName
                },
                password: {
                    rules: ["required"],
                    desc: e.lang.password
                },
                verifyCode: {
                    rules: ["required", "checkVcodeLength", "checkVcodeStatus"],
                    desc: e.lang.captcha
                }
            },
            e._validator.init(e, e.validateRules)
        },
        _validateError: function(e, t) {
            var n = this
              , i = baidu(n.getElement(e.field));
            if (i.addClass(n.constant.ERROR_CLASS),
            n.setGeneralError(e.msg),
            0 == n.disUnameLogin && "userName" == e.field && e.msg == n.lang.unameInputError) {
                var s = new Image;
                s.onload = s.onerror = function() {
                    s.onload = s.onerror = null,
                    s = null
                }
                ,
                s.src = n._domain.https + "/img/v.gif?type=login&loginType=userName"
            }
            t && t.callback && callback()
        },
        _enableUnameLoginCallback: function(e, t) {
            var n = this
              , i = baidu('<input type="hidden" name="userNameLogin" value="1">')
              , s = n.getElement("pass-pop-login-placeholder-normal")
              , o = n.getElement().parentNode
              , r = (baidu(".tab li", o),
            baidu(".tab a", o).get(0))
              , a = baidu(e);
            if (e || t || (t = 1 == n.isLoginWeak ? "normal" : "other",
            a = n.eleLoginWeak),
            0 == n.disUnameLogin) {
                n.disUnameLogin = 1,
                n._validator.confStorage[n.$getId()].userName.desc = "用户名",
                i.get(0).value = "1",
                s && (s.innerHTML = "用户名"),
                r && (r.innerHTML = "用户名登录"),
                n.normalLogin && (n.normalLogin.innerHTML = "用户名登录",
                baidu(n.normalLogin).addClass("pass-normal-btn-s2"),
                "none" !== n.normalLogin.style.display && n._changeLoginType("normal")),
                n.getElement("userNameLabel").innerHTML = "用户名",
                n.getElement("error"),
                baidu(n.getElement("userName")).removeClass("pass-text-input-error"),
                baidu(".tang-pass-pop-login-placeholder").hide(),
                n.getElement("userName").value || n.$show("pass-pop-login-placeholder-normal"),
                n.changeSuggestView({
                    list: "hide",
                    btn: "hide"
                }),
                "normal" == t ? (a.removeClass("pass-unamelogin-btn"),
                a.addClass("pass-emaillogin-btn"),
                a.get(0).innerHTML = "邮箱登录") : "other" == t && (a.get(0).innerHTML = '忘记用户名?使用<a href="###" id="pass-user-login" tabIndex="-1" data-click="other">邮箱登录</a>');
                var c = new Image;
                c.onload = c.onerror = function() {
                    c.onload = c.onerror = null,
                    c = null
                }
                ,
                c.src = n._domain.https + "/img/v.gif?type=login&loginType=normalName"
            } else
                n.disUnameLogin = 0,
                n._validator.confStorage[n.$getId()].userName.desc = "邮箱",
                i.get(0).value = "0",
                s && (s.innerHTML = "邮箱"),
                r && (r.innerHTML = "邮箱登录"),
                n.normalLogin && (n.normalLogin.innerHTML = "邮箱登录",
                baidu(n.normalLogin).removeClass("pass-normal-btn-s2"),
                "none" != n.normalLogin.style.display && n._changeLoginType("normal")),
                n.getElement("userNameLabel").innerHTML = "邮箱",
                n.getElement("error"),
                baidu(n.getElement("userName")).removeClass("pass-text-input-error"),
                baidu(".tang-pass-pop-login-placeholder").hide(),
                n.getElement("userName").value || baidu(n.getElement("pass-pop-login-placeholder-normal")).show(),
                n.changeSuggestView({
                    list: "hide"
                }),
                n.selectBtn && n.loginrecord && n.loginrecord.email && n.loginrecord.email.length > 1 ? n.changeSuggestView({
                    btn: "show"
                }) : n.selectBtn && n.changeSuggestView({
                    btn: "hide"
                }),
                "normal" == t ? (a.addClass("pass-unamelogin-btn"),
                a.removeClass("pass-emaillogin-btn"),
                a.get(0).innerHTML = "用户名登录") : "other" == t && (a.get(0).innerHTML = '忘记邮箱?使用<a href="###" id="pass-user-login" tabIndex="-1" data-click="other">用户名登录</a>')
        },
        _validateSuccess: function(e, t) {
            var n = this
              , i = baidu(n.getElement(e.field));
            n.clearGeneralError(),
            i.removeClass(n.constant.ERROR_CLASS),
            t && t.callback && callback()
        },
        _defaultLoginErr: function(e) {
            var t = this;
            if (t.vcodetype = e.data.vcodetype,
            e.data.codeString ? (t.getVerifyCode(e.data.codeString),
            t._clearInput("verifyCode")) : t.clearVerifyCode(),
            400401 == e.errInfo.no) {
                if (t.getElement("choiceuser_article"))
                    t.$show("choiceuser_article");
                else {
                    var n = t._getIrregularField("choiceuser");
                    t._insertAfterW(baidu(n).get(0), t.getElement()),
                    t._setEventChoiceUser()
                }
                baidu(t.getElement()).hide()
            }
            if (257 == e.errInfo.no && (baidu(t.getElement()).removeClass("tang-pass-login-hide"),
            t.$show(t.getElement()).$hide("choiceuser_article")),
            (6 == e.errInfo.no || 257 == e.errInfo.no) && t._clearInput("verifyCode"),
            4 == e.errInfo.no && (t._clearInput("password"),
            e.data.resetpwd)) {
                var i = "";
                switch (e.data.resetpwd) {
                case "1":
                    i = "1" + t.lang.passwordResetIn;
                    break;
                case "2":
                    i = "2" + t.lang.passwordResetIn;
                    break;
                case "3":
                    i = "3" + t.lang.passwordResetIn;
                    break;
                case "4":
                    i = "3" + t.lang.passwordResetOut
                }
                i.length > 0 && (e.errInfo.msg = t._format(t.lang.passwordResetWarn, {
                    resetpwd: i
                }))
            }
            if (7 == e.errInfo.no) {
                var i = "";
                i.length > 0 && (e.errInfo.msg = t._format(t.lang.passwordResetWarnNo, {
                    resetpwd: i
                }))
            }
            if (e.errInfo.msg && e.errInfo.msg.indexOf("#{") >= 0)
                if (110024 == e.errInfo.no) {
                    var s = t._domain.https + "/v2/?regnotify&action=resend&tpl=" + t.config.product + "&email=" + encodeURIComponent(e.data.mail) + "&u=" + encodeURIComponent(e.data.u);
                    e.errInfo.msg = t._format(e.errInfo.msg, {
                        gotourl: s
                    })
                } else {
                    var o = t.getElement("userName").value;
                    e.errInfo.msg = t._format(e.errInfo.msg, {
                        urldata: "&account=" + o + "&tpl=" + t.config.product + "&u=" + t.config.u
                    })
                }
            e.errInfo.field ? t.setValidateError(e.errInfo.field, e.errInfo.msg, e) : t.setGeneralError(e.errInfo.msg, e)
        },
        _asyncValidate: {
            checkVerifycode: function(e) {
                var t = this
                  , n = t.getElement("verifyCode")
                  , i = t.getElement("codeString");
                passport.data.checkVerifycode({
                    verifycode: t._SBCtoDBC(n.value),
                    loginVersion: "v4",
                    codestring: i.value
                }).success(function(n) {
                    var i = t.fireEvent("checkVerifycode", {
                        rsp: n
                    });
                    i && (0 == n.errInfo.no ? (e && e.success(n),
                    t.$hide("verifyCode_clearbtn"),
                    t.constant.CHECKVERIFYCODE = !0) : 500002 == n.errInfo.no || 500018 == n.errInfo.no ? (n.msg = n.errInfo.msg,
                    e && e.error(n),
                    t.$hide("verifyCodeSuccess"),
                    t.constant.CHECKVERIFYCODE = !1) : (e && e.success(n),
                    t.$hide("verifyCodeSuccess"),
                    t.constant.CHECKVERIFYCODE = !0))
                })
            }
        },
        _format: function(e, t) {
            e = String(e);
            var n = Array.prototype.slice.call(arguments, 1)
              , i = Object.prototype.toString;
            return n.length ? (n = 1 == n.length && null !== t && /\[object Array\]|\[object Object\]/.test(i.call(t)) ? t : n,
            e.replace(/#\{(.+?)\}/g, function(e, t) {
                var s = n[t];
                return "[object Function]" == i.call(s) && (s = s(t)),
                "undefined" == typeof s ? "" : s
            })) : e
        },
        loginConnect: function(e, t, n) {
            ({
                username: e.username,
                smsVcode: e.smsVcode || "",
                sms: e.sms || ""
            }),
            n()
        },
        checkPhone: function(e, t) {
            var n = this;
            checkPhoneWidget ? (checkPhoneWidget.setMakePhone && checkPhoneWidget.setMakePhone(t, e),
            n._ownerDialog && n._ownerDialog.hide("unHide"),
            checkPhoneWidget.show()) : checkPhoneExist || passport._load(n._domain.auto + "/passApi/js/uni_wrapper.js", !0, function() {
                checkPhoneWidget = passport.pop.init({
                    type: "checkPhone",
                    apiOpt: {
                        u: n.config.u,
                        product: n.config.product ? n.config.product : "",
                        phone: t,
                        apiMargicInstance: n,
                        token: n.bdPsWtoken,
                        username: e,
                        isuserid: 1,
                        noSynBdu: n.config.noSynBdu || "",
                        staticPage: n.config.staticPage
                    },
                    tangram: !0,
                    onHide: function() {
                        n._ownerDialog && n._ownerDialog.show()
                    }
                }),
                n._ownerDialog && n._ownerDialog.hide("unHide"),
                checkPhoneWidget.show()
            })
        },
        _loginCheck: function(e) {
            var t = this
              , n = document.getElementById("dv_Input") ? document.getElementById("dv_Input").value : window.LG_DV_ARG && window.LG_DV_ARG.dvjsInput || "";
            n = n.length > 1500 ? "" : n,
            e.length && t.validate("userName", {
                success: function() {
                    passport.data.loginCheck({
                        sub_source: "leadsetpwd",
                        userName: e,
                        loginVersion: "v4",
                        dv: n
                    }).success(function(e) {
                        0 == e.errInfo.no && e.data.userid ? (t.checkPhone(e.data.userid, e.data.mobile),
                        checkPhoneExist = !0,
                        t._ownerDialog && t._ownerDialog.hide("unHide")) : e.data.codeString.length ? (t.vcodetype = e.data.vcodetype,
                        t.getVerifyCode(e.data.codeString)) : t.clearVerifyCode()
                    })
                }
            })
        },
        _SBCtoDBC: function(e) {
            var t = "";
            if (e) {
                for (var n = e.length, i = 0; n > i; i++) {
                    var s = e.charCodeAt(i);
                    s = s >= 65281 && 65374 >= s ? s - 65248 : s,
                    s = 12288 == s ? 32 : s,
                    t += String.fromCharCode(s)
                }
                return t
            }
        },
        submit: function() {
            var e = this;
            (!e.internation || e._validatorforeignmobileFn(e.getElement("foreignMobile"))) && e.validateAll({
                success: function() {
                    function t() {
                        s.timeSpan = (new Date).getTime() - e.initTime,
                        passport.data.traceID && passport.data.traceID.startFlow && passport.data.traceID.startFlow("login"),
                        e.internation ? (s.username = e._SBCtoDBC(e.getElement("foreignMobile").value),
                        s.isPhone = !0,
                        s.countrycode = baidu(e.getElement("foreignMobileLabel")).attr("data-countrycode") || "") : s.countrycode = "",
                        s.FP_UID = e._getCookie("FP_UID") || "",
                        s.FP_INFO = window.PP_FP_INFO || "",
                        s.loginVersion = "v4",
                        s.dv = document.getElementById("dv_Input") ? document.getElementById("dv_Input").value : window.LG_DV_ARG && window.LG_DV_ARG.dvjsInput || "",
                        passport.data.login(s).success(function(t) {
                            if (e.submitStatus = 2,
                            t.loginType = "password",
                            0 == t.errInfo.no) {
                                var n = e.fireEvent("loginSuccess", {
                                    rsp: t
                                });
                                if (!n)
                                    return;
                                window.location ? window.location.href = t.data.u : document.location.href = t.data.u
                            } else {
                                c.value = e.lang.login,
                                e.getElement("submit").style.color = "#fff";
                                var n = e.fireEvent("loginError", {
                                    rsp: t
                                });
                                if (!n)
                                    return;
                                e._defaultLoginErr(t)
                            }
                        })
                    }
                    e._doFocus("submit"),
                    e.submitStatus = 1;
                    var n = e.fireEvent("beforeSubmit");
                    if (e.getElement("submit").style.color = "#9ebef4",
                    n) {
                        if (e.spLogin) {
                            var i = baidu('<input type="hidden" name="splogin" value="' + e.spLogin + '">');
                            e.getElement("hiddenFields").appendChild(i.get(0)),
                            e.spLogin = null
                        }
                        var s = baidu.form.json(e.getElement("form"));
                        s.token = e.bdPsWtoken,
                        passport.data.setContext(baidu.extend({}, e.config)),
                        s.foreignusername && (s.foreignusername = e._SBCtoDBC(s.foreignusername)),
                        s.userName = e._SBCtoDBC(s.userName),
                        s.verifyCode = e._SBCtoDBC(s.verifyCode);
                        var o = e._SBCtoDBC(e.getElement("password").value);
                        if (e.RSA && e.rsakey) {
                            var r = o;
                            r.length < 128 && !e.config.safeFlag && (s.password = baidu.url.escapeSymbol(e.RSA.encrypt(r)),
                            s.rsakey = e.rsakey,
                            s.crypttype = 12)
                        }
                        var a, c = e.getElement("submit"), l = 15e3;
                        e.getElement("submit").style.color = "#9ebef4",
                        c.value = e.lang.logining,
                        a = setTimeout(function() {
                            1 != e.submitStatus || e.config.connect || e.setGeneralError(e.lang.submitTimeup),
                            c.value = e.lang.login
                        }, l),
                        e.loginConnect({
                            username: s.userName,
                            password: s.password
                        }, {
                            success: function() {
                                clearTimeout(a),
                                c.value = e.lang.login
                            },
                            fail: function(t) {
                                clearTimeout(a),
                                c.value = e.lang.login,
                                e.setGeneralError(t)
                            }
                        }, t)
                    }
                }
            }, !0)
        },
        _eventHandler: function() {
            var e, t = {
                focus: function() {
                    var t = e.fireEvent("fieldFocus", {
                        ele: this
                    });
                    t && (this.addClass(e.constant.FOCUS_CLASS),
                    this.removeClass(e.constant.ERROR_CLASS))
                },
                blur: function() {
                    var t = e.fireEvent("fieldBlur", {
                        ele: this
                    });
                    t && this.removeClass(e.constant.FOCUS_CLASS)
                },
                mouseover: function() {
                    var t = e.fireEvent("fieldMouseover", {
                        ele: this
                    });
                    t && this.addClass(e.constant.HOVER_CLASS)
                },
                mouseout: function() {
                    var t = e.fireEvent("fieldMouseout", {
                        ele: this
                    });
                    t && this.removeClass(e.constant.HOVER_CLASS)
                },
                keyup: function() {
                    e.fireEvent("fieldKeyup", {
                        ele: this
                    })
                }
            }, n = {
                focus: {
                    userName: function() {
                        e.getElement("loginMerge") && (e.getElement("loginMerge").value = "true",
                        e.getElement("isPhone").value = "")
                    },
                    password: function() {
                        e._getRSA(function(t) {
                            e.RSA = t.RSA,
                            e.rsakey = t.rsakey
                        })
                    },
                    verifyCode: function() {}
                },
                blur: {
                    userName: function() {},
                    password: function(t) {
                        var n = this.get(0).value;
                        n.length && e.validate(t)
                    },
                    verifyCode: function(t) {
                        var n = this.get(0).value;
                        n.length && e.validate(t);
                        var i = e.getElement("verifyCode")
                          , s = baidu(i);
                        i.value ? e._asyncValidate.checkVerifycode.call(e, {
                            error: function(t) {
                                s.addClass(e.constant.ERROR_CLASS),
                                e.setGeneralError(t.msg)
                            },
                            success: function() {
                                s.removeClass(e.constant.ERROR_CLASS),
                                e.clearGeneralError()
                            }
                        }) : e.$hide("verifyCodeSuccess")
                    }
                },
                change: {
                    userName: function() {
                        var t = this.get(0).value;
                        e._loginCheck(t)
                    },
                    verifyCode: function() {}
                },
                click: {
                    verifyCodeChange: function(t, n) {
                        e.getElement("verifyCode").value = "",
                        e._doFocus("verifyCode"),
                        e.getVerifyCode(),
                        n.preventDefault()
                    }
                },
                keyup: {},
                submit: function(t) {
                    e.submit(),
                    t.preventDefault()
                }
            };
            return {
                entrance: function(i) {
                    e = this;
                    var s = (baidu(i.target),
                    i.target.name);
                    if (!s && i.target.id) {
                        var o = i.target.id.match(/\d+__(.*)$/);
                        o && (s = o[1])
                    }
                    s && (t.hasOwnProperty(i.type) && t[i.type].apply(baidu(i.target), [s, i]),
                    n.hasOwnProperty(i.type) && ("function" == typeof n[i.type] && n[i.type].apply(baidu(i.target), [i]),
                    n[i.type].hasOwnProperty(s) && n[i.type][s].apply(baidu(i.target), [s, i])),
                    e.initialized || "focus" != i.type || e._initApi())
                }
            }
        }(),
        $dispose: function() {
            var e = this;
            e.disposed || (baidu.dom(e.getElement()).removeClass(e.constant.CONTAINER_CLASS),
            e.getElement().removeChild(e.getElement("form")),
            magic.Base.prototype.$dispose.call(e))
        }
    }),
    magic
});

""")
a = ctx.call('escapeSymbol', 'test')
print(a)
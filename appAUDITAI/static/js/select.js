function MultiSelectTag(e, t = { shadow: false, rounded: true }) {
    var n = null,
      l = null,
      d = null,
      a = null,
      s = null,
      i = null,
      o = null,
      c = null,
      r = null,
      u = null,
      p = null,
      v = null,
      m = new DOMParser();
  
    function h(e = null) {
      for (var t of ((v.innerHTML = ""), l))
        if (t.selected) !g(t.value) && f(t);
        else {
            const n = document.createElement("li");
            (n.style.fontSize = "12px"), // Set the font-size to 12px
            (n.innerHTML = t.label),
              (n.dataset.value = t.value),
              e && t.label.toLowerCase().startsWith(e.toLowerCase())
                ? v.appendChild(n)
                : e || v.appendChild(n);
      
        }
    }
  
    function f(e) {
      const t = document.createElement("div");
      t.classList.add("item-container");
      t.style.backgroundColor = "#d5ecf7";
      const n = document.createElement("div");
      n.classList.add("item-label");
      n.innerHTML = e.label;
      n.dataset.value = e.value;
  
      // Update the selected items color
      n.style.color = "#red";
      n.style.backgroundColor = "#d5ecf7";

      const d = new DOMParser().parseFromString(
        '<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="item-close-svg">\n' +
          '<line x1="18" y1="6" x2="6" y2="18"></line>\n' +
          '<line x1="6" y1="6" x2="18" y2="18"></line>\n' +
          '</svg>',
        "image/svg+xml"
      ).documentElement;
  
      d.addEventListener("click", (t) => {
        (l.find((t) => t.value == e.value).selected = false), w(e.value), h(), E();
      });
  
      t.appendChild(n);
      t.appendChild(d);
      o.append(t);
    }
  
    function L() {
      for (var e of v.children)
        e.addEventListener("click", (e) => {
          (l.find((t) => t.value == e.target.dataset.value).selected = true),
            (r.value = null),
            h(),
            E(),
            r.focus();
        });
    }
  
    function g(e) {
      for (var t of o.children)
        if (
          !t.classList.contains("input-body") &&
          t.firstChild.dataset.value == e
        )
          return true;
      return false;
    }
  
    function w(e) {
      for (var t of o.children)
        t.classList.contains("input-body") ||
          t.firstChild.dataset.value != e ||
          o.removeChild(t);
    }
  
    function E(e = true) {
      selected_values = [];
      for (var d = 0; d < l.length; d++)
        (n.options[d].selected = l[d].selected),
          l[d].selected &&
            selected_values.push({ label: l[d].label, value: l[d].value });
      e && t.hasOwnProperty("onChange") && t.onChange(selected_values);
      document.getElementById("control_selected_values").value = JSON.stringify(selected_values);
    }
  
    (n = document.getElementById(e)),
      (function () {
        (l = [...n.options].map((e) => ({
          value: e.value,
          label: e.label,
          selected: e.selected,
        }))),
          n.classList.add("hidden"),
         
          (d = document.createElement("div")).classList.add("mult-select-tag"),
          (a = document.createElement("div")).classList.add("wrapper"),
          (i = document.createElement("div")).classList.add("body", "rounded"), 
          (o = document.createElement("div")).classList.add("input-container"),
          (r = document.createElement("input")).classList.add("input");

        (r.placeholder = `${t.placeholder || "Search Controls"}`),
        r.style.fontSize = "12px";
          (c = document.createElement("inputBody")).classList.add("input-body"),
          c.append(r),
          o.style.width = "400px"; // Set default width to 400px
          o.style.borderRadius = "5px";
          i.append(o),
          (s = document.createElement("div")).classList.add("btn-container"),
          ((u = document.createElement("button")).type = "button"),
          s.append(u);
        const e = m.parseFromString(
          '<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n' +
            '<polyline points="18 15 12 21 6 15"></polyline></svg>',
          "image/svg+xml"
        ).documentElement;
        u.append(e),
          i.append(s),
          a.append(i),
          (p = document.createElement("div")).classList.add("drawer", "hidden"),
          t.shadow && p.classList.add("shadow"),
          t.rounded && p.classList.add("rounded"),
          p.append(c),
          (v = document.createElement("ul")),
          p.appendChild(v),
          d.appendChild(a),
          d.appendChild(p),
          n.nextSibling
            ? n.parentNode.insertBefore(d, n.nextSibling)
            : n.parentNode.appendChild(d);
      })(),
      h(),
      L(),
      E(false),
      u.addEventListener("click", () => {
        p.classList.contains("hidden") &&
          (h(), L(), p.classList.remove("hidden"), r.focus());
      }),
      r.addEventListener("keyup", (e) => {
        h(e.target.value), L();
      }),
      r.addEventListener("keydown", (e) => {
        if ("Backspace" === e.key && !e.target.value && o.childElementCount > 1) {
          const e = i.children[o.childElementCount - 2].firstChild;
          (l.find((t) => t.value == e.dataset.value).selected = false),
            w(e.dataset.value),
            E();
        }
      }),
      window.addEventListener("click", (e) => {
        d.contains(e.target) || p.classList.add("hidden");
      });
  }
  
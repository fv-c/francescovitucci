document.addEventListener("DOMContentLoaded",async function(){const e=await fetch("{{ site.url }}/assets/posts.json"),s=await e.json(),t=JSON.parse("{{ page.categories | jsonify }}"),a=s.filter(e=>{return e.categories.split(",").map(e=>e.trim()).some(e=>t.includes(e))}).slice(0,3);let o="";a.forEach(e=>{o+=`\n            <div class="blogPostContainer">\n                <a href="${e.url}" class="blogPostFeatImg" style="background-image: url('${siteUrl}/assets/img/blog/lowRes/${e.featImg}');"></a>\n                <a href="${e.url}" class="blogCategory">${e.categories}</a>\n                <a href="${e.url}" class="blogTitle">${e.title}</a>\n                <p class="blogExcerpt">${e.excerpt}</p>\n            </div>\n        `}),document.querySelector(".blogReadMoreWrapper").innerHTML=o});
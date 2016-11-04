[title]: imgs/oc/titre.svg
[vue3D]: imgs/oc/vue3D.png
[map]: imgs/oc/map.svg

[code20]: http://www.codemagazine.fr/pdf/code9.pdf
    "Code 2.0 magazine #9"
[sourcesGitHub]: https://github.com/
    "Sources sur GitHub"

<div markdown=1 class="col-left">

![titre oc][title]
{: .titreImg .img}

Les dessins des constellations tels que nous les connaissons appartiennent à une époque révolue ; ils ne sont que la simple anamorphose d’un tracé beaucoup plus complexe qu'il est désormais possible de mettre en lumière.  
En récupérant la position des étoiles d'une constellation par rapport au Soleil, il est possible de modéliser un volume à facettes dont chaque sommet sera associé à la position « exacte » – d’après nos actuelles observations issus des calculs du satellite Hipparcos – de chacune des étoiles dans l'espace. Libérée du point de vue terrestre, la constellation retrouve dès lors sa troisième dimension.

![Grande Ourse 3D][vue3D]
_[modélisation de la Grande Ourse]_{: .altText}
{: .imgAlt}

Grâce à cette modélisation, de nouvelles formes et traductions sont envisageables : matérialiser les constellations grâce à une impression 3D à échelle extrêmement réduite, tenant dans la main ; associer en un volume global toutes les constellations et produire ainsi une carte/objet en trois dimensions de la sphère céleste ; ou encore, observer la déformation opérée par l’anamorphose d'un point de vue autre que celui de la Terre.

![Grande Ourse dessin][map]
_[dessin de la Grande Ourse]_{: .altText}
{: .imgAlt}

Il n'existe pas de convention ni de sélection officielle d'étoile définissant le dessin d'une constellation. La sélection des étoiles pour ce projet suis une méthode basique, chacune des étoiles possède une magnitude inférieure à 6 (au delà une étoile n'est pas visible à l'oeil nu) et sélectionne arbitrairement un nombre suffisant d'objets dans l'ordre de leur magnitude (aucune étoile ayant une magnitude inférieure à la plus faible n'a été rejetée) afin de trouver un dessin littéralement similaire à leur nom. La modélisation 3D est elle aussi arbitraire quoique générique (les faces partant du Soleil tente d'englober l'ensemble d'étoiles et se referme derrière).

</div>

<div markdown=1 class="col-right">

site ↑↑↑
{: .visit}

Projet interrompu au stade de prototype pour 8 constellations.  
Pourrait être repris et automatisé à l'occasion des résultats du satellite Gaia dont le catalogue est attendu pour 2020.
{: .comment .black}

[Sources <span class="sym">↗</span>][sourcesGitHub]{: .sources target="blank"}
{: .sourcesp}

~/objets_célestes = [
: 5-Cetus
: 38-Ursa Major
: 42-Hydra
: 53-Microscopium
: 73-Norma
: 77-Sculptor
: 80-Mensa
: 82-Telescopium  
]  

: /modèles3D <span class="done">✓</span>
    : modélisation des constellations, disponibles aux formats .dae & .stl sur le site.
    {: .desc}
: /cartes <span class="done">✓</span>
    : propositions et reprises de dessins se référant aux noms des constellations.
    {: .desc}
: /impressions3D <span class="done">✓</span>
    : prototypages d'impressions 3D des volumes à échelle extrêmement réduites.
    {: .desc}
: /exo-grande_ours <span class="done">✓</span>
    : carte de l'anamorphose de la Grande Ourse vue depuis Gliese 667C.
    {: .desc}
: /volume_céleste <span class="done">~</span>
    : matérialisation du volume global de toutes les constellations assemblées.
    {: .desc}
: /atlas  <span class="notdone">×</span>
    : atlas du ciel
    {: .desc}
: /atlas_extra-terrestre <span class="notdone">×</span>
    : prendre une exoplanète potentiellement propice à la vie, repérer ses étoiles les plus brillantes et tenter d'inventer ses constellations comme pourrait le faire un colon.
    {: .desc}

__Parutions :__{: .publicTitle}   
Une petite double page dans [Code 2.0][code20]{: target="blank"} vous propose de dessiner la Grande Ourse vue depuis Gliese 667C.
{: .public}

</div>

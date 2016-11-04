[nycthémère]: https://fr.wiktionary.org/wiki/nycth%C3%A9m%C3%A8re
    "Définition de nycthémère"
[toutArticle]: https://autre.space/tout
    "Lien vers l'article publié dans Tout"
[memoire]: https://autre.space/memoire
    "Lien vers la page du mémoire"
[sourcesGitHub]: https://github.com/hackstub/instrumentGeoTempsVariant
    "Sources sur GitHub"

[title]: imgs/igtv/titrePx.svg
[tradAnim]: imgs/igtv/tradAnim.gif
[schemaConcept]: imgs/igtv/concept.svg
[schemaVariationS]: imgs/igtv/variationS.svg

<div markdown=1 class="col-left">

![titre IGTV][title]
{: .titreImg .img}

Vous vous trouvez le 18 mai 2016 à Reykjavik, en Islande, aux coordonnées 64°08’07” Nord et 21°53’43” Ouest ; à votre poignet ou dans votre poche se trouve un petit cadran solaire numérique, composé d’un écran, d’un récepteur GPS et d’un micro-contrôleur : c’est l’instrument de géo-temps variant (IGTV). On observe dans cette région de la Terre des différences extrêmes entre la durée des jours et des nuits qui permettent d’éprouver pleinement les caractéristiques de cet instrument. À cet endroit précis, le [nycthémère][]{: target="blank"} se partage approximativement en 18 heures et 49 minutes de jour, et, par conséquent, 5 heures et 11 minutes de nuit. L’IGTV va convertir chacune de ces durées en 12 heures, à l’instar du système des heures inégales romaines et grecques, utilisé jusqu’à la fin du Moyen Âge.

En divisant la durée du jour (18 h 49 min, soit 67 740 secondes) en 12 heures (43 200 secondes), on obtient la valeur suivante : 1 seconde variable du jour (notée 1 ~s<sup>jour</sup>) équivaut à environ 1,57 seconde constante (notée 1 s). De la même manière, 1 ~s<sup>nuit</sup> représente 0,43 s (5 heures 11 minutes divisées par 12 heures). Lorsque 1 seconde variable de jour s’incrémente, il s’est écoulé 1,57 seconde constante (~s est plus lente que s) et la nuit, lorsque 1 seconde variable s’incrémente, il ne s’est écoulé que 0,43 seconde constante (~s est alors plus de deux fois plus rapide que s).

![Schéma concept][schemaConcept]
{: .img}

L’IGTV opère également un changement de rythme de la seconde variable, pour lisser le passage de la valeur de ~s<sup>jour</sup> à ~s<sup>nuit</sup> : plutôt que de passer brusquement de l’une à l’autre (de ~s = 1,57 à 0,43 au moment du coucher du soleil par exemple), l’instrument calcule une intégrale à l’intérieur même de la journée de manière à ce qu’au moment du coucher et du lever de soleil, 1 ~s soit égale à 1 s. La valeur de la seconde variable (irrégulière) va elle-même varier au cours de la journée et ne sera dès lors plus absolue elle-même. Elle sera égale à 1s au lever, augmentera progressivement jusqu’à atteindre un pic supérieur à la valeur précédemment calculée, 1,57s en milieu de journée, puis diminuera jusqu’à atteindre le palier de 1s au moment du coucher et évoluera de manière inverse durant la nuit et ainsi de suite.

![Schéma variation de s~][SchemavariationS]
_variation de ~s<sup>var</sup> sur le nycthémère_{: .altText}
{: .imgAlt}

Un troisième niveau de variation apparaît lorsque vous vous déplacez car vous intervenez dès lors dans un autre espace, un ailleurs qui n’a plus les mêmes durées de jour et de nuit. L’IGTV recalcule en permanence la valeur de la seconde variable selon votre position géographique précise récupéré par le GPS et affiche continuellement une heure propre au point géographique auquel vous vous trouvez. Il traduit un temps local.

Vous pouvez lire l'[article complet][toutArticle]{: target="blank"} publié dans la revue Tout pour plus d'informations et interrogations.

</div>

<div markdown=1 class="col-right">

site ↑↑↑
{: .visit}

L'instrument est toujours en développement, le code est accessible sur github et est d'ors et déjà exploitable en l'état même s'il manque une doc qui ne devrait plus trop tarder. Nous tentons actuellement de réaliser la première version standalone, un peu miniaturisée avec des premiers essais de traductions graphique sur un écran à encre.
{: .comment .black}

[Sources <span class="sym">↗</span>][sourcesGitHub]{: .sources target="blank"}
{: .sourcesp}

~/instrument_de_géo-temps_variant
: /igtv-arduino <span class="done">~</span>
    : version électronique et portative de l'instrument.
    {: .desc}
: /igtv-web <span class="notdone">×</span>
    : version web de l'instrument.
    {: .desc}
: /horloges_variables <span class="notdone">×</span>
    : portage du principe de l'igtv sur des horloges fixes pour définir l'heure d'un lieu en particulier sur lesquelles on peut se synchroniser pour partager une heure commune.
    {: .desc}
: /carte_de_variation_de_la_seconde_variable <span class="notdone">×</span>
    : représentation graphique 3D de la valeur actuelle de la seconde variable sur la surface de la Terre.
    {: .desc}
: /IGTV-Technis&Politique <span class="done">~</span>
    : Tentative de définition technique et politique des concepts liés et produis par la mesure du temps de l'igtv.
    {: .desc}


__Parutions :__{: .publicTitle}  
Il est possible de lire mes interrogations liées à la mesure du temps dans le tuto _[Hacker le temps][toutArticle]{: target="blank"}_, édité dans la revue Tout, ainsi que dans la 3ème partie de mon [mémoire][memoire]{: target="blank"} de fin de cursus.
{: .public}

![Animation cadran][tradAnim]
{: .img}

</div>

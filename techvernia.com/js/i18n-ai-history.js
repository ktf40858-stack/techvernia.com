// AI History Page - Multilingual Translations
// 10 Languages: EN, FR, ES, DE, PT, ZH, JA, KO, AR, HI

console.log('📦 i18n-ai-history.js loaded');

const aiHistoryTranslations = {
    en: {
        // Navigation
        "nav.home": "Home",
        "nav.categories": "Categories",
        "nav.guides": "Guides",
        "nav.compare": "Compare",
        "nav.ai-history": "AI History",
        "nav.blog": "Blog",
        "nav.about": "About",
        "nav.contact": "Contact",

        // Hero Section
        "hero.title": "The History of Artificial Intelligence",
        "hero.description": "From the visionary pioneers of the 1950s to the breakthrough models of today, explore the remarkable journey of AI development. Discover the brilliant minds and groundbreaking moments that transformed AI from theory to reality.",

        // Era 1: Founders (1950-1970)
        "era1.badge": "1950 - 1970",
        "era1.title": "The Founders Era",
        "era1.description": "The birth of AI as an academic discipline, where pioneering computer scientists laid the theoretical and practical foundations for artificial intelligence.",

        // Events Era 1
        "event1.title": "The Turing Test",
        "event1.pioneer": "Alan Turing (United Kingdom)",
        "event1.description": "Published 'Computing Machinery and Intelligence', introducing the Turing Test as a measure of machine intelligence. This seminal paper asked the fundamental question: Can machines think?",
        "badge.theoretical": "Theoretical Foundation",
        "badge.philosophy": "Philosophy of AI",

        "event2.title": "First Neural Network",
        "event2.pioneer": "Marvin Minsky (United States)",
        "event2.description": "Created SNARC (Stochastic Neural Analog Reinforcement Calculator), the first artificial neural network machine with 40 neurons. This pioneering work demonstrated that machines could learn from experience.",
        "badge.neural": "Neural Networks",
        "badge.ml": "Machine Learning",

        "event3.title": "Logic Theorist Program",
        "event3.pioneer": "Allen Newell & Herbert Simon (United States)",
        "event3.description": "Developed Logic Theorist, considered the first AI program. It could prove mathematical theorems from Russell and Whitehead's Principia Mathematica, sometimes finding more elegant proofs than the original authors.",
        "badge.symbolic": "Symbolic AI",
        "badge.reasoning": "Automated Reasoning",

        "event4.title": "Birth of Artificial Intelligence",
        "event4.pioneer": "John McCarthy (United States)",
        "event4.description": "Organized the Dartmouth Conference, where the term Artificial Intelligence was coined. This historic summer workshop brought together the brightest minds to explore machine intelligence, establishing AI as a formal academic field.",
        "badge.dartmouth": "Dartmouth Conference",
        "badge.founding": "Field Founding",

        "event5.title": "LISP Programming Language",
        "event5.pioneer": "John McCarthy (United States)",
        "event5.description": "Created LISP, the second-oldest high-level programming language still in use today. LISP became the dominant language for AI research for decades, introducing revolutionary concepts like garbage collection and tree data structures.",
        "badge.programming": "Programming Language",
        "badge.symbolic-processing": "Symbolic Processing",

        "event6.title": "The Perceptron",
        "event6.pioneer": "Frank Rosenblatt (United States)",
        "event6.description": "Invented the Perceptron, the first artificial neural network for pattern recognition. The Mark I Perceptron could learn to classify simple patterns, laying groundwork for modern deep learning.",
        "badge.pattern": "Pattern Recognition",

        "event7.title": "MIT AI Laboratory",
        "event7.pioneer": "Marvin Minsky & John McCarthy (United States)",
        "event7.description": "Co-founded the MIT Artificial Intelligence Laboratory, which became one of the world's leading AI research centers. The lab produced groundbreaking work in computer vision, robotics, and machine learning.",
        "badge.institution": "Research Institution",
        "badge.leadership": "Academic Leadership",

        // Era 2: Expert Systems (1970-1990)
        "era2.badge": "1970 - 1990",
        "era2.title": "The Expert Systems Era",
        "era2.description": "AI moved from theoretical research to practical applications, with expert systems solving real-world problems in medicine, chemistry, and business.",

        "event8.title": "DENDRAL - First Expert System",
        "event8.pioneer": "Edward Feigenbaum (United States)",
        "event8.description": "Developed DENDRAL, the first expert system capable of identifying organic molecules. This breakthrough project demonstrated that AI could match or exceed human expert performance in specialized domains.",
        "badge.expert": "Expert Systems",
        "badge.chemistry": "Chemistry AI",

        "event9.title": "MYCIN Medical Diagnosis",
        "event9.pioneer": "Edward Feigenbaum & Team (United States)",
        "event9.description": "Created MYCIN, an expert system for diagnosing bacterial infections and recommending antibiotics. It achieved 69% accuracy compared to 65% for human experts, proving AI's potential in healthcare.",
        "badge.medical": "Medical AI",

        "event10.title": "Backpropagation Revolution",
        "event10.pioneer": "Geoffrey Hinton (Canada), David Rumelhart & Ronald Williams (United States)",
        "event10.description": "Popularized the backpropagation algorithm, enabling neural networks to learn complex patterns by efficiently computing gradients. This breakthrough revitalized neural network research after years of stagnation.",
        "badge.deep": "Deep Learning",

        "event11.title": "Bayesian Networks",
        "event11.pioneer": "Judea Pearl (United States)",
        "event11.description": "Revolutionized probabilistic reasoning with Bayesian networks, providing a framework for representing and reasoning about uncertainty. This work earned him the 2011 Turing Award.",
        "badge.probabilistic": "Probabilistic AI",
        "badge.causal": "Causal Inference",

        "event12.title": "Convolutional Neural Networks",
        "event12.pioneer": "Yann LeCun (France)",
        "event12.description": "Developed Convolutional Neural Networks (CNNs) and successfully applied them to handwritten digit recognition. LeNet could read zip codes with exceptional accuracy, pioneering computer vision.",
        "badge.vision": "Computer Vision",
        "badge.cnn": "Convolutional Networks",

        // Era 3: Deep Learning Renaissance (1997-2012)
        "era3.badge": "1997 - 2012",
        "era3.title": "The Deep Learning Renaissance",
        "era3.description": "Neural networks made a stunning comeback with new architectures and enhanced computational power, setting the stage for the AI revolution.",

        "event13.title": "Deep Blue Defeats Kasparov",
        "event13.pioneer": "IBM Research Team (United States)",
        "event13.description": "IBM's Deep Blue became the first computer to defeat a reigning world chess champion in a match. This historic victory demonstrated that machines could surpass humans in complex strategic thinking.",
        "badge.game": "Game AI",
        "badge.milestone": "Milestone Achievement",

        "event14.title": "LSTM Networks",
        "event14.pioneer": "Sepp Hochreiter (Austria) & Jürgen Schmidhuber (Switzerland)",
        "event14.description": "Invented Long Short-Term Memory (LSTM) networks, solving the vanishing gradient problem that plagued recurrent neural networks. LSTMs became fundamental for speech recognition and language processing.",
        "badge.rnn": "Recurrent Networks",
        "badge.sequence": "Sequence Learning",

        "event15.title": "ImageNet Dataset",
        "event15.pioneer": "Fei-Fei Li (China/United States)",
        "event15.description": "Created ImageNet, a massive dataset with 14 million labeled images across 20,000 categories. This dataset became the benchmark that catalyzed the deep learning revolution in computer vision.",
        "badge.dataset": "Dataset Creation",

        "event16.title": "Google Brain Project",
        "event16.pioneer": "Andrew Ng & Jeff Dean (United States)",
        "event16.description": "Launched Google Brain, using massive computational resources to train deep neural networks. The famous cat recognition experiment showed that neural networks could learn to identify concepts without explicit programming.",
        "badge.large-scale": "Large-Scale ML",
        "badge.unsupervised": "Unsupervised Learning",

        "event17.title": "AlexNet's Triumph",
        "event17.pioneer": "Alex Krizhevsky, Geoffrey Hinton & Ilya Sutskever (Canada)",
        "event17.description": "AlexNet won the ImageNet competition with a record-breaking 15.3% error rate, crushing previous methods. This decisive victory ignited the deep learning revolution, proving the power of GPU-trained neural networks.",
        "badge.breakthrough": "Deep Learning Breakthrough",

        // Era 4: Modern AI (2012-2020)
        "era4.badge": "2012 - 2020",
        "era4.title": "The Modern AI Era",
        "era4.description": "Deep learning became mainstream, achieving superhuman performance in games, vision, and language tasks, while new AI companies emerged to commercialize these breakthroughs.",

        "event18.title": "Generative Adversarial Networks",
        "event18.pioneer": "Ian Goodfellow (United States)",
        "event18.description": "Invented GANs, a revolutionary architecture where two neural networks compete: one generates fake data, the other tries to detect it. GANs enabled image generation with unprecedented realism.",
        "badge.generative": "Generative AI",
        "badge.image-gen": "Image Generation",

        "event19.title": "OpenAI Founded",
        "event19.pioneer": "Elon Musk, Sam Altman, Ilya Sutskever & Others (United States)",
        "event19.description": "Founded as a non-profit AI research company with $1 billion in commitments, aiming to ensure AGI benefits all humanity. OpenAI would later create GPT and ChatGPT.",
        "badge.safety": "AI Safety",
        "badge.research-lab": "Research Lab",

        "event20.title": "AlphaGo Defeats Lee Sedol",
        "event20.pioneer": "Demis Hassabis & DeepMind Team (United Kingdom)",
        "event20.description": "AlphaGo defeated world champion Lee Sedol 4-1 in Go, a game with more possible positions than atoms in the universe. This stunning achievement showcased AI's ability to master intuitive, creative tasks.",
        "badge.reinforcement": "Reinforcement Learning",

        "event21.title": "Deep Learning Turing Award",
        "event21.pioneer": "Geoffrey Hinton (Canada), Yoshua Bengio (Canada) & Yann LeCun (France)",
        "event21.description": "The Godfathers of AI received the Turing Award for conceptual and engineering breakthroughs that made deep neural networks a critical component of computing. Their work spanning three decades finally received recognition.",
        "badge.nobel-computing": "Nobel of Computing",

        "event22.title": "AlphaFold Solves Protein Folding",
        "event22.pioneer": "Demis Hassabis & DeepMind Team (United Kingdom)",
        "event22.description": "AlphaFold2 solved the 50-year-old protein folding problem, predicting 3D protein structures with atomic-level accuracy. This breakthrough accelerated drug discovery and earned Hassabis the Nobel Prize in Chemistry (2024).",
        "badge.biology": "Computational Biology",
        "badge.discovery": "Scientific Discovery",

        // Era 5: Generative AI (2017-Present)
        "era5.badge": "2017 - Present",
        "era5.title": "The Generative AI Era",
        "era5.description": "Transformer architecture and large language models revolutionized AI, making it accessible to billions and transforming how humans interact with technology.",

        "event23.title": "Attention Is All You Need",
        "event23.pioneer": "Ashish Vaswani & Google Brain Team (United States)",
        "event23.description": "Published the Transformer paper, introducing the self-attention mechanism that could process sequences in parallel. This architecture became the foundation for GPT, BERT, and all modern large language models.",
        "badge.transformer": "Transformer",
        "badge.nlp": "NLP Revolution",

        "event24.title": "GPT-1: The First GPT",
        "event24.pioneer": "Alec Radford & OpenAI (United States)",
        "event24.description": "Released GPT-1 with 117 million parameters, demonstrating that language models could learn general language understanding through unsupervised pre-training and achieve strong performance across diverse tasks.",
        "badge.language": "Language Models",
        "badge.transfer": "Transfer Learning",

        "event25.title": "GPT-2 Too Dangerous to Release",
        "event25.pioneer": "Alec Radford & OpenAI (United States)",
        "event25.description": "GPT-2 (1.5 billion parameters) generated text so coherent that OpenAI initially refused to release it, citing concerns about misuse. This sparked important debates about AI safety and responsible disclosure.",
        "badge.llm": "Large Language Models",
        "badge.ethics": "AI Ethics",

        "event26.title": "Anthropic Founded",
        "event26.pioneer": "Dario Amodei & Daniela Amodei (United States)",
        "event26.description": "Former OpenAI researchers founded Anthropic, focusing on AI safety and building reliable, interpretable AI systems. Their Constitutional AI approach aims to create more controllable and aligned models.",
        "badge.ethics-first": "Ethics-First AI",

        "event27.title": "DALL-E Image Generation",
        "event27.pioneer": "OpenAI Research Team (United States)",
        "event27.description": "DALL-E could generate creative images from text descriptions, demonstrating unprecedented cross-modal understanding. It showed that AI could be truly creative, combining concepts in novel ways.",
        "badge.text-to-image": "Text-to-Image",
        "badge.multimodal": "Multimodal AI",

        "event28.title": "Stable Diffusion Open Source",
        "event28.pioneer": "Emad Mostaque & Stability AI (United Kingdom)",
        "event28.description": "Released Stable Diffusion as open source, democratizing AI image generation. Unlike closed competitors, anyone could run it locally, sparking an explosion of creative AI applications.",
        "badge.open-source": "Open Source AI",

        "event29.title": "ChatGPT Launch",
        "event29.pioneer": "OpenAI & Sam Altman (United States)",
        "event29.description": "ChatGPT launched on November 30, 2022, reaching 1 million users in 5 days and 100 million in 2 months - the fastest-growing consumer application in history. It brought AI into the mainstream and changed the world.",
        "badge.consumer": "Consumer AI",
        "badge.impact": "Cultural Impact",

        "event30.title": "GPT-4 Released",
        "event30.pioneer": "OpenAI Research Team (United States)",
        "event30.description": "GPT-4 demonstrated human-level performance on many professional exams, including scoring in the 90th percentile on the bar exam. It introduced multimodal capabilities, processing both text and images.",
        "badge.agi": "AGI Progress",

        "event31.title": "Claude 3 Family",
        "event31.pioneer": "Anthropic Research Team (United States)",
        "event31.description": "Released Claude 3 (Opus, Sonnet, Haiku), with Opus surpassing GPT-4 on many benchmarks. Claude emphasized safety, honesty, and helpfulness while achieving state-of-the-art performance.",
        "badge.constitutional": "Constitutional AI",
        "badge.ethical": "Ethical AI",

        "event32.title": "Gemini Ultra & 2M Context",
        "event32.pioneer": "Google DeepMind (United Kingdom/United States)",
        "event32.description": "Google released Gemini 1.5 with an unprecedented 2 million token context window, capable of processing hours of video or entire codebases. Gemini Ultra matched GPT-4 across all benchmarks.",
        "badge.long-context": "Long Context",

        "event33.title": "DeepSeek-V3 Open Source",
        "event33.pioneer": "Liang Wenfeng & DeepSeek (China)",
        "event33.description": "Chinese startup DeepSeek released V3 (671 billion parameters) as open source, matching GPT-4 in performance while costing only $5.5 million to train. This proved cutting-edge AI doesn't require billion-dollar budgets.",
        "badge.cost": "Cost Efficiency",

        "event34.title": "GLM-4 Breakthrough",
        "event34.pioneer": "Tang Jie & Zhipu AI (China)",
        "event34.description": "Zhipu AI's GLM-4 achieved a 1 million token context window with only 9 billion parameters, demonstrating exceptional multilingual capabilities and competitive performance with Western models while being fully open source.",
        "badge.multilingual": "Multilingual AI",

        // Awards Section
        "awards.title": "Major Recognitions & Awards",
        "awards.description": "The pioneers who transformed AI have been honored with the highest accolades in science and technology.",
        "award1.title": "2018 Turing Award",
        "award1.recipients": "Geoffrey Hinton, Yoshua Bengio, Yann LeCun",
        "award1.description": "The Nobel Prize of Computing for conceptual and engineering breakthroughs in deep neural networks.",
        "award2.title": "2011 Turing Award",
        "award2.recipients": "Judea Pearl",
        "award2.description": "For fundamental contributions to AI through probabilistic and causal reasoning.",
        "award3.title": "2024 Nobel Prize in Chemistry",
        "award3.recipients": "Demis Hassabis (DeepMind)",
        "award3.description": "For AlphaFold2's breakthrough in protein structure prediction.",
        "award4.title": "2022 IEEE Medal of Honor",
        "award4.recipients": "Yann LeCun",
        "award4.description": "For pioneering contributions to deep learning and convolutional neural networks.",
        "award5.title": "2022 Princess of Asturias Award",
        "award5.recipients": "Demis Hassabis",
        "award5.description": "For outstanding contributions to scientific and technical research through AI.",
        "award6.title": "TIME 100 Most Influential",
        "award6.recipients": "Sam Altman (2023), Dario Amodei (2024)",
        "award6.description": "Recognized for leading the generative AI revolution and shaping its future.",

        // Footer
        "footer.description": "Your ultimate guide to AI tools and technologies. Discover, compare, and master the best AI solutions.",
        "footer.quick-links": "Quick Links",
        "footer.resources": "Resources",
        "footer.follow": "Follow Us",
        "footer.copyright": "© 2024 TechVernia. All rights reserved."
    },

    fr: {
        // Navigation
        "nav.home": "Accueil",
        "nav.categories": "Catégories",
        "nav.guides": "Guides",
        "nav.compare": "Comparer",
        "nav.ai-history": "Histoire de l'IA",
        "nav.blog": "Blog",
        "nav.about": "À propos",
        "nav.contact": "Contact",

        // Hero Section
        "hero.title": "L'Histoire de l'Intelligence Artificielle",
        "hero.description": "Des pionniers visionnaires des années 1950 aux modèles révolutionnaires d'aujourd'hui, explorez le parcours remarquable du développement de l'IA. Découvrez les esprits brillants et les moments révolutionnaires qui ont transformé l'IA de la théorie à la réalité.",

        // Era 1
        "era1.badge": "1950 - 1970",
        "era1.title": "L'Ère des Fondateurs",
        "era1.description": "La naissance de l'IA en tant que discipline académique, où les informaticiens pionniers ont posé les fondations théoriques et pratiques de l'intelligence artificielle.",

        "event1.title": "Le Test de Turing",
        "event1.pioneer": "Alan Turing (Royaume-Uni)",
        "event1.description": "A publié 'Computing Machinery and Intelligence', introduisant le test de Turing comme mesure de l'intelligence des machines. Cet article fondateur posait la question fondamentale : Les machines peuvent-elles penser ?",
        "badge.theoretical": "Fondement Théorique",
        "badge.philosophy": "Philosophie de l'IA",

        "event2.title": "Premier Réseau de Neurones",
        "event2.pioneer": "Marvin Minsky (États-Unis)",
        "event2.description": "A créé SNARC (Stochastic Neural Analog Reinforcement Calculator), la première machine à réseau de neurones artificiel avec 40 neurones. Ce travail pionnier a démontré que les machines pouvaient apprendre de l'expérience.",
        "badge.neural": "Réseaux de Neurones",
        "badge.ml": "Apprentissage Automatique",

        "event3.title": "Programme Logic Theorist",
        "event3.pioneer": "Allen Newell & Herbert Simon (États-Unis)",
        "event3.description": "A développé Logic Theorist, considéré comme le premier programme d'IA. Il pouvait prouver des théorèmes mathématiques des Principia Mathematica de Russell et Whitehead, trouvant parfois des preuves plus élégantes que les auteurs originaux.",
        "badge.symbolic": "IA Symbolique",
        "badge.reasoning": "Raisonnement Automatisé",

        "event4.title": "Naissance de l'Intelligence Artificielle",
        "event4.pioneer": "John McCarthy (États-Unis)",
        "event4.description": "A organisé la Conférence de Dartmouth, où le terme Intelligence Artificielle a été inventé. Cet atelier d'été historique a réuni les esprits les plus brillants pour explorer l'intelligence des machines, établissant l'IA comme domaine académique formel.",
        "badge.dartmouth": "Conférence de Dartmouth",
        "badge.founding": "Fondation du Domaine",

        "event5.title": "Langage de Programmation LISP",
        "event5.pioneer": "John McCarthy (États-Unis)",
        "event5.description": "A créé LISP, le deuxième plus ancien langage de programmation de haut niveau encore utilisé aujourd'hui. LISP est devenu le langage dominant pour la recherche en IA pendant des décennies, introduisant des concepts révolutionnaires comme le garbage collection et les structures de données arborescentes.",
        "badge.programming": "Langage de Programmation",
        "badge.symbolic-processing": "Traitement Symbolique",

        "event6.title": "Le Perceptron",
        "event6.pioneer": "Frank Rosenblatt (États-Unis)",
        "event6.description": "A inventé le Perceptron, le premier réseau de neurones artificiel pour la reconnaissance de motifs. Le Mark I Perceptron pouvait apprendre à classifier des motifs simples, jetant les bases de l'apprentissage profond moderne.",
        "badge.pattern": "Reconnaissance de Motifs",

        "event7.title": "Laboratoire d'IA du MIT",
        "event7.pioneer": "Marvin Minsky & John McCarthy (États-Unis)",
        "event7.description": "Ont co-fondé le Laboratoire d'Intelligence Artificielle du MIT, qui est devenu l'un des principaux centres de recherche en IA au monde. Le laboratoire a produit des travaux révolutionnaires en vision par ordinateur, robotique et apprentissage automatique.",
        "badge.institution": "Institution de Recherche",
        "badge.leadership": "Leadership Académique",

        // Era 2
        "era2.badge": "1970 - 1990",
        "era2.title": "L'Ère des Systèmes Experts",
        "era2.description": "L'IA est passée de la recherche théorique aux applications pratiques, avec des systèmes experts résolvant des problèmes réels en médecine, chimie et affaires.",

        "event8.title": "DENDRAL - Premier Système Expert",
        "event8.pioneer": "Edward Feigenbaum (États-Unis)",
        "event8.description": "A développé DENDRAL, le premier système expert capable d'identifier des molécules organiques. Ce projet révolutionnaire a démontré que l'IA pouvait égaler ou dépasser les performances des experts humains dans des domaines spécialisés.",
        "badge.expert": "Systèmes Experts",
        "badge.chemistry": "IA en Chimie",

        "event9.title": "Diagnostic Médical MYCIN",
        "event9.pioneer": "Edward Feigenbaum & Équipe (États-Unis)",
        "event9.description": "A créé MYCIN, un système expert pour diagnostiquer les infections bactériennes et recommander des antibiotiques. Il a atteint 69% de précision contre 65% pour les experts humains, prouvant le potentiel de l'IA en santé.",
        "badge.medical": "IA Médicale",

        "event10.title": "Révolution de la Rétropropagation",
        "event10.pioneer": "Geoffrey Hinton (Canada), David Rumelhart & Ronald Williams (États-Unis)",
        "event10.description": "A popularisé l'algorithme de rétropropagation, permettant aux réseaux de neurones d'apprendre des motifs complexes en calculant efficacement les gradients. Cette percée a revitalisé la recherche sur les réseaux de neurones après des années de stagnation.",
        "badge.deep": "Apprentissage Profond",

        "event11.title": "Réseaux Bayésiens",
        "event11.pioneer": "Judea Pearl (États-Unis)",
        "event11.description": "A révolutionné le raisonnement probabiliste avec les réseaux bayésiens, fournissant un cadre pour représenter et raisonner sur l'incertitude. Ce travail lui a valu le prix Turing 2011.",
        "badge.probabilistic": "IA Probabiliste",
        "badge.causal": "Inférence Causale",

        "event12.title": "Réseaux de Neurones Convolutifs",
        "event12.pioneer": "Yann LeCun (France)",
        "event12.description": "A développé les réseaux de neurones convolutifs (CNN) et les a appliqués avec succès à la reconnaissance de chiffres manuscrits. LeNet pouvait lire les codes postaux avec une précision exceptionnelle, pionnier de la vision par ordinateur.",
        "badge.vision": "Vision par Ordinateur",
        "badge.cnn": "Réseaux Convolutifs",

        // Era 3
        "era3.badge": "1997 - 2012",
        "era3.title": "La Renaissance de l'Apprentissage Profond",
        "era3.description": "Les réseaux de neurones ont fait un retour spectaculaire avec de nouvelles architectures et une puissance de calcul accrue, ouvrant la voie à la révolution de l'IA.",

        "event13.title": "Deep Blue Bat Kasparov",
        "event13.pioneer": "Équipe de Recherche IBM (États-Unis)",
        "event13.description": "Deep Blue d'IBM est devenu le premier ordinateur à battre un champion du monde d'échecs en titre lors d'un match. Cette victoire historique a démontré que les machines pouvaient surpasser les humains en pensée stratégique complexe.",
        "badge.game": "IA de Jeu",
        "badge.milestone": "Réalisation Majeure",

        "event14.title": "Réseaux LSTM",
        "event14.pioneer": "Sepp Hochreiter (Autriche) & Jürgen Schmidhuber (Suisse)",
        "event14.description": "A inventé les réseaux Long Short-Term Memory (LSTM), résolvant le problème de la disparition du gradient qui affligeait les réseaux de neurones récurrents. Les LSTM sont devenus fondamentaux pour la reconnaissance vocale et le traitement du langage.",
        "badge.rnn": "Réseaux Récurrents",
        "badge.sequence": "Apprentissage de Séquences",

        "event15.title": "Dataset ImageNet",
        "event15.pioneer": "Fei-Fei Li (Chine/États-Unis)",
        "event15.description": "A créé ImageNet, un dataset massif avec 14 millions d'images étiquetées dans 20 000 catégories. Ce dataset est devenu le benchmark qui a catalysé la révolution de l'apprentissage profond en vision par ordinateur.",
        "badge.dataset": "Création de Dataset",

        "event16.title": "Projet Google Brain",
        "event16.pioneer": "Andrew Ng & Jeff Dean (États-Unis)",
        "event16.description": "A lancé Google Brain, utilisant des ressources de calcul massives pour entraîner des réseaux de neurones profonds. La célèbre expérience de reconnaissance de chats a montré que les réseaux de neurones pouvaient apprendre à identifier des concepts sans programmation explicite.",
        "badge.large-scale": "ML à Grande Échelle",
        "badge.unsupervised": "Apprentissage Non Supervisé",

        "event17.title": "Le Triomphe d'AlexNet",
        "event17.pioneer": "Alex Krizhevsky, Geoffrey Hinton & Ilya Sutskever (Canada)",
        "event17.description": "AlexNet a remporté la compétition ImageNet avec un taux d'erreur record de 15,3%, écrasant les méthodes précédentes. Cette victoire décisive a déclenché la révolution de l'apprentissage profond, prouvant la puissance des réseaux de neurones entraînés sur GPU.",
        "badge.breakthrough": "Percée en Apprentissage Profond",

        // Era 4
        "era4.badge": "2012 - 2020",
        "era4.title": "L'Ère de l'IA Moderne",
        "era4.description": "L'apprentissage profond est devenu courant, atteignant des performances surhumaines dans les jeux, la vision et les tâches linguistiques, tandis que de nouvelles entreprises d'IA sont apparues pour commercialiser ces percées.",

        "event18.title": "Réseaux Adverses Génératifs",
        "event18.pioneer": "Ian Goodfellow (États-Unis)",
        "event18.description": "A inventé les GAN, une architecture révolutionnaire où deux réseaux de neurones s'affrontent : l'un génère de fausses données, l'autre essaie de les détecter. Les GAN ont permis la génération d'images avec un réalisme sans précédent.",
        "badge.generative": "IA Générative",
        "badge.image-gen": "Génération d'Images",

        "event19.title": "Fondation d'OpenAI",
        "event19.pioneer": "Elon Musk, Sam Altman, Ilya Sutskever & Autres (États-Unis)",
        "event19.description": "Fondée comme entreprise de recherche en IA à but non lucratif avec 1 milliard de dollars d'engagements, visant à garantir que l'AGI profite à toute l'humanité. OpenAI créera plus tard GPT et ChatGPT.",
        "badge.safety": "Sécurité de l'IA",
        "badge.research-lab": "Laboratoire de Recherche",

        "event20.title": "AlphaGo Bat Lee Sedol",
        "event20.pioneer": "Demis Hassabis & Équipe DeepMind (Royaume-Uni)",
        "event20.description": "AlphaGo a battu le champion du monde Lee Sedol 4-1 au Go, un jeu avec plus de positions possibles que d'atomes dans l'univers. Cette réalisation stupéfiante a montré la capacité de l'IA à maîtriser des tâches intuitives et créatives.",
        "badge.reinforcement": "Apprentissage par Renforcement",

        "event21.title": "Prix Turing de l'Apprentissage Profond",
        "event21.pioneer": "Geoffrey Hinton (Canada), Yoshua Bengio (Canada) & Yann LeCun (France)",
        "event21.description": "Les Parrains de l'IA ont reçu le prix Turing pour des percées conceptuelles et techniques qui ont fait des réseaux de neurones profonds un composant critique de l'informatique. Leur travail sur trois décennies a enfin reçu reconnaissance.",
        "badge.nobel-computing": "Nobel de l'Informatique",

        "event22.title": "AlphaFold Résout le Repliement des Protéines",
        "event22.pioneer": "Demis Hassabis & Équipe DeepMind (Royaume-Uni)",
        "event22.description": "AlphaFold2 a résolu le problème du repliement des protéines vieux de 50 ans, prédisant les structures de protéines en 3D avec une précision atomique. Cette percée a accéléré la découverte de médicaments et a valu à Hassabis le prix Nobel de chimie (2024).",
        "badge.biology": "Biologie Computationnelle",
        "badge.discovery": "Découverte Scientifique",

        // Era 5
        "era5.badge": "2017 - Aujourd'hui",
        "era5.title": "L'Ère de l'IA Générative",
        "era5.description": "L'architecture Transformer et les grands modèles de langage ont révolutionné l'IA, la rendant accessible à des milliards de personnes et transformant la façon dont les humains interagissent avec la technologie.",

        "event23.title": "L'Attention Est Tout Ce Dont Vous Avez Besoin",
        "event23.pioneer": "Ashish Vaswani & Équipe Google Brain (États-Unis)",
        "event23.description": "A publié le papier Transformer, introduisant le mécanisme d'auto-attention qui pouvait traiter des séquences en parallèle. Cette architecture est devenue la base de GPT, BERT et de tous les modèles de langage modernes.",
        "badge.transformer": "Transformer",
        "badge.nlp": "Révolution NLP",

        "event24.title": "GPT-1 : Le Premier GPT",
        "event24.pioneer": "Alec Radford & OpenAI (États-Unis)",
        "event24.description": "A publié GPT-1 avec 117 millions de paramètres, démontrant que les modèles de langage pouvaient apprendre une compréhension générale du langage grâce au pré-entraînement non supervisé et obtenir de bonnes performances sur diverses tâches.",
        "badge.language": "Modèles de Langage",
        "badge.transfer": "Apprentissage par Transfert",

        "event25.title": "GPT-2 Trop Dangereux pour Être Publié",
        "event25.pioneer": "Alec Radford & OpenAI (États-Unis)",
        "event25.description": "GPT-2 (1,5 milliard de paramètres) générait du texte si cohérent qu'OpenAI a initialement refusé de le publier, invoquant des préoccupations concernant une utilisation abusive. Cela a déclenché d'importants débats sur la sécurité de l'IA et la divulgation responsable.",
        "badge.llm": "Grands Modèles de Langage",
        "badge.ethics": "Éthique de l'IA",

        "event26.title": "Fondation d'Anthropic",
        "event26.pioneer": "Dario Amodei & Daniela Amodei (États-Unis)",
        "event26.description": "D'anciens chercheurs d'OpenAI ont fondé Anthropic, se concentrant sur la sécurité de l'IA et la construction de systèmes d'IA fiables et interprétables. Leur approche Constitutional AI vise à créer des modèles plus contrôlables et alignés.",
        "badge.ethics-first": "IA Éthique d'Abord",

        "event27.title": "Génération d'Images DALL-E",
        "event27.pioneer": "Équipe de Recherche OpenAI (États-Unis)",
        "event27.description": "DALL-E pouvait générer des images créatives à partir de descriptions textuelles, démontrant une compréhension cross-modale sans précédent. Il a montré que l'IA pouvait être vraiment créative, combinant des concepts de manière nouvelle.",
        "badge.text-to-image": "Texte vers Image",
        "badge.multimodal": "IA Multimodale",

        "event28.title": "Stable Diffusion Open Source",
        "event28.pioneer": "Emad Mostaque & Stability AI (Royaume-Uni)",
        "event28.description": "A publié Stable Diffusion en open source, démocratisant la génération d'images par IA. Contrairement aux concurrents fermés, n'importe qui pouvait l'exécuter localement, déclenchant une explosion d'applications d'IA créatives.",
        "badge.open-source": "IA Open Source",

        "event29.title": "Lancement de ChatGPT",
        "event29.pioneer": "OpenAI & Sam Altman (États-Unis)",
        "event29.description": "ChatGPT a été lancé le 30 novembre 2022, atteignant 1 million d'utilisateurs en 5 jours et 100 millions en 2 mois - l'application grand public à la croissance la plus rapide de l'histoire. Il a fait entrer l'IA dans le courant dominant et a changé le monde.",
        "badge.consumer": "IA Grand Public",
        "badge.impact": "Impact Culturel",

        "event30.title": "Sortie de GPT-4",
        "event30.pioneer": "Équipe de Recherche OpenAI (États-Unis)",
        "event30.description": "GPT-4 a démontré des performances de niveau humain sur de nombreux examens professionnels, notamment en obtenant le 90e percentile à l'examen du barreau. Il a introduit des capacités multimodales, traitant à la fois du texte et des images.",
        "badge.agi": "Progrès vers l'AGI",

        "event31.title": "Famille Claude 3",
        "event31.pioneer": "Équipe de Recherche Anthropic (États-Unis)",
        "event31.description": "A publié Claude 3 (Opus, Sonnet, Haiku), Opus surpassant GPT-4 sur de nombreux benchmarks. Claude a mis l'accent sur la sécurité, l'honnêteté et l'utilité tout en atteignant des performances de pointe.",
        "badge.constitutional": "IA Constitutionnelle",
        "badge.ethical": "IA Éthique",

        "event32.title": "Gemini Ultra & Contexte de 2M",
        "event32.pioneer": "Google DeepMind (Royaume-Uni/États-Unis)",
        "event32.description": "Google a publié Gemini 1.5 avec une fenêtre de contexte sans précédent de 2 millions de tokens, capable de traiter des heures de vidéo ou des bases de code entières. Gemini Ultra a égalé GPT-4 sur tous les benchmarks.",
        "badge.long-context": "Long Contexte",

        "event33.title": "DeepSeek-V3 Open Source",
        "event33.pioneer": "Liang Wenfeng & DeepSeek (Chine)",
        "event33.description": "La startup chinoise DeepSeek a publié V3 (671 milliards de paramètres) en open source, égalant GPT-4 en performance tout en ne coûtant que 5,5 millions de dollars à entraîner. Cela a prouvé que l'IA de pointe ne nécessite pas des budgets de milliards de dollars.",
        "badge.cost": "Efficacité des Coûts",

        "event34.title": "Percée GLM-4",
        "event34.pioneer": "Tang Jie & Zhipu AI (Chine)",
        "event34.description": "GLM-4 de Zhipu AI a atteint une fenêtre de contexte de 1 million de tokens avec seulement 9 milliards de paramètres, démontrant des capacités multilingues exceptionnelles et des performances compétitives avec les modèles occidentaux tout en étant entièrement open source.",
        "badge.multilingual": "IA Multilingue",

        // Awards
        "awards.title": "Reconnaissances et Prix Majeurs",
        "awards.description": "Les pionniers qui ont transformé l'IA ont été honorés par les plus hautes distinctions en science et technologie.",
        "award1.title": "Prix Turing 2018",
        "award1.recipients": "Geoffrey Hinton, Yoshua Bengio, Yann LeCun",
        "award1.description": "Le Prix Nobel de l'Informatique pour des percées conceptuelles et techniques dans les réseaux de neurones profonds.",
        "award2.title": "Prix Turing 2011",
        "award2.recipients": "Judea Pearl",
        "award2.description": "Pour des contributions fondamentales à l'IA par le raisonnement probabiliste et causal.",
        "award3.title": "Prix Nobel de Chimie 2024",
        "award3.recipients": "Demis Hassabis (DeepMind)",
        "award3.description": "Pour la percée d'AlphaFold2 dans la prédiction de structure des protéines.",
        "award4.title": "Médaille d'Honneur IEEE 2022",
        "award4.recipients": "Yann LeCun",
        "award4.description": "Pour des contributions pionnières à l'apprentissage profond et aux réseaux de neurones convolutifs.",
        "award5.title": "Prix Prince des Asturies 2022",
        "award5.recipients": "Demis Hassabis",
        "award5.description": "Pour des contributions exceptionnelles à la recherche scientifique et technique à travers l'IA.",
        "award6.title": "TIME 100 des Plus Influents",
        "award6.recipients": "Sam Altman (2023), Dario Amodei (2024)",
        "award6.description": "Reconnus pour avoir mené la révolution de l'IA générative et façonné son avenir.",

        // Footer
        "footer.description": "Votre guide ultime des outils et technologies d'IA. Découvrez, comparez et maîtrisez les meilleures solutions d'IA.",
        "footer.quick-links": "Liens Rapides",
        "footer.resources": "Ressources",
        "footer.follow": "Suivez-Nous",
        "footer.copyright": "© 2024 TechVernia. Tous droits réservés."
    },

    es: {
        // Navigation
        "nav.home": "Inicio",
        "nav.categories": "Categorías",
        "nav.guides": "Guías",
        "nav.compare": "Comparar",
        "nav.ai-history": "Historia de la IA",
        "nav.blog": "Blog",
        "nav.about": "Acerca de",
        "nav.contact": "Contacto",

        // Hero
        "hero.title": "La Historia de la Inteligencia Artificial",
        "hero.description": "Desde los pioneros visionarios de la década de 1950 hasta los modelos revolucionarios de hoy, explora el notable viaje del desarrollo de la IA. Descubre las mentes brillantes y los momentos revolucionarios que transformaron la IA de teoría a realidad.",

        // Era 1
        "era1.badge": "1950 - 1970",
        "era1.title": "La Era de los Fundadores",
        "era1.description": "El nacimiento de la IA como disciplina académica, donde los informáticos pioneros sentaron las bases teóricas y prácticas de la inteligencia artificial.",

        "event1.title": "La Prueba de Turing",
        "event1.pioneer": "Alan Turing (Reino Unido)",
        "event1.description": "Publicó 'Computing Machinery and Intelligence', introduciendo la Prueba de Turing como medida de la inteligencia de las máquinas. Este artículo seminal planteó la pregunta fundamental: ¿Pueden pensar las máquinas?",
        "badge.theoretical": "Fundamento Teórico",
        "badge.philosophy": "Filosofía de la IA",

        "event2.title": "Primera Red Neuronal",
        "event2.pioneer": "Marvin Minsky (Estados Unidos)",
        "event2.description": "Creó SNARC (Calculadora de Refuerzo Analógico Neural Estocástico), la primera máquina de red neuronal artificial con 40 neuronas. Este trabajo pionero demostró que las máquinas podían aprender de la experiencia.",
        "badge.neural": "Redes Neuronales",
        "badge.ml": "Aprendizaje Automático",

        "event3.title": "Programa Logic Theorist",
        "event3.pioneer": "Allen Newell & Herbert Simon (Estados Unidos)",
        "event3.description": "Desarrolló Logic Theorist, considerado el primer programa de IA. Podía probar teoremas matemáticos de Principia Mathematica de Russell y Whitehead, a veces encontrando pruebas más elegantes que los autores originales.",
        "badge.symbolic": "IA Simbólica",
        "badge.reasoning": "Razonamiento Automatizado",

        "event4.title": "Nacimiento de la Inteligencia Artificial",
        "event4.pioneer": "John McCarthy (Estados Unidos)",
        "event4.description": "Organizó la Conferencia de Dartmouth, donde se acuñó el término Inteligencia Artificial. Este histórico taller de verano reunió a las mentes más brillantes para explorar la inteligencia de las máquinas, estableciendo la IA como campo académico formal.",
        "badge.dartmouth": "Conferencia de Dartmouth",
        "badge.founding": "Fundación del Campo",

        "event5.title": "Lenguaje de Programación LISP",
        "event5.pioneer": "John McCarthy (Estados Unidos)",
        "event5.description": "Creó LISP, el segundo lenguaje de programación de alto nivel más antiguo aún en uso hoy. LISP se convirtió en el lenguaje dominante para la investigación en IA durante décadas, introduciendo conceptos revolucionarios como la recolección de basura y las estructuras de datos de árbol.",
        "badge.programming": "Lenguaje de Programación",
        "badge.symbolic-processing": "Procesamiento Simbólico",

        "event6.title": "El Perceptrón",
        "event6.pioneer": "Frank Rosenblatt (Estados Unidos)",
        "event6.description": "Inventó el Perceptrón, la primera red neuronal artificial para el reconocimiento de patrones. El Perceptrón Mark I podía aprender a clasificar patrones simples, sentando las bases para el aprendizaje profundo moderno.",
        "badge.pattern": "Reconocimiento de Patrones",

        "event7.title": "Laboratorio de IA del MIT",
        "event7.pioneer": "Marvin Minsky & John McCarthy (Estados Unidos)",
        "event7.description": "Co-fundaron el Laboratorio de Inteligencia Artificial del MIT, que se convirtió en uno de los principales centros de investigación en IA del mundo. El laboratorio produjo trabajos revolucionarios en visión por computadora, robótica y aprendizaje automático.",
        "badge.institution": "Institución de Investigación",
        "badge.leadership": "Liderazgo Académico",

        // Era 2
        "era2.badge": "1970 - 1990",
        "era2.title": "La Era de los Sistemas Expertos",
        "era2.description": "La IA pasó de la investigación teórica a las aplicaciones prácticas, con sistemas expertos resolviendo problemas del mundo real en medicina, química y negocios.",

        "event8.title": "DENDRAL - Primer Sistema Experto",
        "event8.pioneer": "Edward Feigenbaum (Estados Unidos)",
        "event8.description": "Desarrolló DENDRAL, el primer sistema experto capaz de identificar moléculas orgánicas. Este proyecto revolucionario demostró que la IA podía igualar o superar el rendimiento de expertos humanos en dominios especializados.",
        "badge.expert": "Sistemas Expertos",
        "badge.chemistry": "IA en Química",

        "event9.title": "Diagnóstico Médico MYCIN",
        "event9.pioneer": "Edward Feigenbaum & Equipo (Estados Unidos)",
        "event9.description": "Creó MYCIN, un sistema experto para diagnosticar infecciones bacterianas y recomendar antibióticos. Alcanzó un 69% de precisión en comparación con el 65% de los expertos humanos, demostrando el potencial de la IA en la salud.",
        "badge.medical": "IA Médica",

        "event10.title": "Revolución de la Retropropagación",
        "event10.pioneer": "Geoffrey Hinton (Canadá), David Rumelhart & Ronald Williams (Estados Unidos)",
        "event10.description": "Popularizó el algoritmo de retropropagación, permitiendo que las redes neuronales aprendieran patrones complejos calculando eficientemente los gradientes. Este avance revitalizó la investigación en redes neuronales después de años de estancamiento.",
        "badge.deep": "Aprendizaje Profundo",

        "event11.title": "Redes Bayesianas",
        "event11.pioneer": "Judea Pearl (Estados Unidos)",
        "event11.description": "Revolucionó el razonamiento probabilístico con redes bayesianas, proporcionando un marco para representar y razonar sobre la incertidumbre. Este trabajo le valió el Premio Turing 2011.",
        "badge.probabilistic": "IA Probabilística",
        "badge.causal": "Inferencia Causal",

        "event12.title": "Redes Neuronales Convolucionales",
        "event12.pioneer": "Yann LeCun (Francia)",
        "event12.description": "Desarrolló Redes Neuronales Convolucionales (CNN) y las aplicó con éxito al reconocimiento de dígitos manuscritos. LeNet podía leer códigos postales con una precisión excepcional, siendo pionero en visión por computadora.",
        "badge.vision": "Visión por Computadora",
        "badge.cnn": "Redes Convolucionales",

        // Era 3
        "era3.badge": "1997 - 2012",
        "era3.title": "El Renacimiento del Aprendizaje Profundo",
        "era3.description": "Las redes neuronales hicieron un regreso impresionante con nuevas arquitecturas y mayor poder computacional, sentando las bases para la revolución de la IA.",

        "event13.title": "Deep Blue Derrota a Kasparov",
        "event13.pioneer": "Equipo de Investigación de IBM (Estados Unidos)",
        "event13.description": "Deep Blue de IBM se convirtió en la primera computadora en derrotar a un campeón mundial de ajedrez reinante en un partido. Esta victoria histórica demostró que las máquinas podían superar a los humanos en el pensamiento estratégico complejo.",
        "badge.game": "IA de Juegos",
        "badge.milestone": "Logro Histórico",

        "event14.title": "Redes LSTM",
        "event14.pioneer": "Sepp Hochreiter (Austria) & Jürgen Schmidhuber (Suiza)",
        "event14.description": "Inventó redes Long Short-Term Memory (LSTM), resolviendo el problema del gradiente que desaparece que afectaba a las redes neuronales recurrentes. Las LSTM se volvieron fundamentales para el reconocimiento de voz y el procesamiento del lenguaje.",
        "badge.rnn": "Redes Recurrentes",
        "badge.sequence": "Aprendizaje de Secuencias",

        "event15.title": "Dataset ImageNet",
        "event15.pioneer": "Fei-Fei Li (China/Estados Unidos)",
        "event15.description": "Creó ImageNet, un dataset masivo con 14 millones de imágenes etiquetadas en 20,000 categorías. Este dataset se convirtió en el benchmark que catalizó la revolución del aprendizaje profundo en visión por computadora.",
        "badge.dataset": "Creación de Dataset",

        "event16.title": "Proyecto Google Brain",
        "event16.pioneer": "Andrew Ng & Jeff Dean (Estados Unidos)",
        "event16.description": "Lanzó Google Brain, utilizando recursos computacionales masivos para entrenar redes neuronales profundas. El famoso experimento de reconocimiento de gatos mostró que las redes neuronales podían aprender a identificar conceptos sin programación explícita.",
        "badge.large-scale": "ML a Gran Escala",
        "badge.unsupervised": "Aprendizaje No Supervisado",

        "event17.title": "El Triunfo de AlexNet",
        "event17.pioneer": "Alex Krizhevsky, Geoffrey Hinton & Ilya Sutskever (Canadá)",
        "event17.description": "AlexNet ganó la competencia ImageNet con una tasa de error récord del 15.3%, aplastando los métodos anteriores. Esta victoria decisiva encendió la revolución del aprendizaje profundo, demostrando el poder de las redes neuronales entrenadas en GPU.",
        "badge.breakthrough": "Avance en Aprendizaje Profundo",

        // Era 4
        "era4.badge": "2012 - 2020",
        "era4.title": "La Era de la IA Moderna",
        "era4.description": "El aprendizaje profundo se convirtió en mainstream, logrando rendimiento sobrehumano en juegos, visión y tareas de lenguaje, mientras nuevas empresas de IA surgían para comercializar estos avances.",

        "event18.title": "Redes Adversarias Generativas",
        "event18.pioneer": "Ian Goodfellow (Estados Unidos)",
        "event18.description": "Inventó los GAN, una arquitectura revolucionaria donde dos redes neuronales compiten: una genera datos falsos, la otra intenta detectarlos. Los GAN permitieron la generación de imágenes con un realismo sin precedentes.",
        "badge.generative": "IA Generativa",
        "badge.image-gen": "Generación de Imágenes",

        "event19.title": "Fundación de OpenAI",
        "event19.pioneer": "Elon Musk, Sam Altman, Ilya Sutskever & Otros (Estados Unidos)",
        "event19.description": "Fundada como empresa de investigación en IA sin fines de lucro con $1 mil millones en compromisos, con el objetivo de asegurar que la AGI beneficie a toda la humanidad. OpenAI más tarde crearía GPT y ChatGPT.",
        "badge.safety": "Seguridad de la IA",
        "badge.research-lab": "Laboratorio de Investigación",

        "event20.title": "AlphaGo Derrota a Lee Sedol",
        "event20.pioneer": "Demis Hassabis & Equipo DeepMind (Reino Unido)",
        "event20.description": "AlphaGo derrotó al campeón mundial Lee Sedol 4-1 en Go, un juego con más posiciones posibles que átomos en el universo. Este logro sorprendente mostró la capacidad de la IA para dominar tareas intuitivas y creativas.",
        "badge.reinforcement": "Aprendizaje por Refuerzo",

        "event21.title": "Premio Turing de Aprendizaje Profundo",
        "event21.pioneer": "Geoffrey Hinton (Canadá), Yoshua Bengio (Canadá) & Yann LeCun (Francia)",
        "event21.description": "Los Padrinos de la IA recibieron el Premio Turing por avances conceptuales y técnicos que hicieron de las redes neuronales profundas un componente crítico de la computación. Su trabajo de tres décadas finalmente recibió reconocimiento.",
        "badge.nobel-computing": "Nobel de la Computación",

        "event22.title": "AlphaFold Resuelve el Plegamiento de Proteínas",
        "event22.pioneer": "Demis Hassabis & Equipo DeepMind (Reino Unido)",
        "event22.description": "AlphaFold2 resolvió el problema del plegamiento de proteínas de 50 años, prediciendo estructuras de proteínas 3D con precisión a nivel atómico. Este avance aceleró el descubrimiento de fármacos y le valió a Hassabis el Premio Nobel de Química (2024).",
        "badge.biology": "Biología Computacional",
        "badge.discovery": "Descubrimiento Científico",

        // Era 5
        "era5.badge": "2017 - Presente",
        "era5.title": "La Era de la IA Generativa",
        "era5.description": "La arquitectura Transformer y los grandes modelos de lenguaje revolucionaron la IA, haciéndola accesible a miles de millones y transformando cómo los humanos interactúan con la tecnología.",

        "event23.title": "La Atención Es Todo Lo Que Necesitas",
        "event23.pioneer": "Ashish Vaswani & Equipo Google Brain (Estados Unidos)",
        "event23.description": "Publicó el artículo Transformer, introduciendo el mecanismo de auto-atención que podía procesar secuencias en paralelo. Esta arquitectura se convirtió en la base de GPT, BERT y todos los modelos de lenguaje modernos.",
        "badge.transformer": "Transformer",
        "badge.nlp": "Revolución NLP",

        "event24.title": "GPT-1: El Primer GPT",
        "event24.pioneer": "Alec Radford & OpenAI (Estados Unidos)",
        "event24.description": "Lanzó GPT-1 con 117 millones de parámetros, demostrando que los modelos de lenguaje podían aprender comprensión general del lenguaje a través de pre-entrenamiento no supervisado y lograr un rendimiento sólido en diversas tareas.",
        "badge.language": "Modelos de Lenguaje",
        "badge.transfer": "Aprendizaje por Transferencia",

        "event25.title": "GPT-2 Demasiado Peligroso para Publicar",
        "event25.pioneer": "Alec Radford & OpenAI (Estados Unidos)",
        "event25.description": "GPT-2 (1.5 mil millones de parámetros) generaba texto tan coherente que OpenAI inicialmente se negó a publicarlo, citando preocupaciones sobre el mal uso. Esto desencadenó debates importantes sobre la seguridad de la IA y la divulgación responsable.",
        "badge.llm": "Grandes Modelos de Lenguaje",
        "badge.ethics": "Ética de la IA",

        "event26.title": "Fundación de Anthropic",
        "event26.pioneer": "Dario Amodei & Daniela Amodei (Estados Unidos)",
        "event26.description": "Antiguos investigadores de OpenAI fundaron Anthropic, enfocándose en la seguridad de la IA y la construcción de sistemas de IA confiables e interpretables. Su enfoque de IA Constitucional apunta a crear modelos más controlables y alineados.",
        "badge.ethics-first": "IA Ética Primero",

        "event27.title": "Generación de Imágenes DALL-E",
        "event27.pioneer": "Equipo de Investigación OpenAI (Estados Unidos)",
        "event27.description": "DALL-E podía generar imágenes creativas a partir de descripciones de texto, demostrando una comprensión cross-modal sin precedentes. Mostró que la IA podía ser verdaderamente creativa, combinando conceptos de maneras novedosas.",
        "badge.text-to-image": "Texto a Imagen",
        "badge.multimodal": "IA Multimodal",

        "event28.title": "Stable Diffusion Open Source",
        "event28.pioneer": "Emad Mostaque & Stability AI (Reino Unido)",
        "event28.description": "Lanzó Stable Diffusion como código abierto, democratizando la generación de imágenes con IA. A diferencia de los competidores cerrados, cualquiera podía ejecutarlo localmente, desencadenando una explosión de aplicaciones de IA creativas.",
        "badge.open-source": "IA de Código Abierto",

        "event29.title": "Lanzamiento de ChatGPT",
        "event29.pioneer": "OpenAI & Sam Altman (Estados Unidos)",
        "event29.description": "ChatGPT se lanzó el 30 de noviembre de 2022, alcanzando 1 millón de usuarios en 5 días y 100 millones en 2 meses - la aplicación de consumo de más rápido crecimiento en la historia. Trajo la IA al mainstream y cambió el mundo.",
        "badge.consumer": "IA de Consumo",
        "badge.impact": "Impacto Cultural",

        "event30.title": "Lanzamiento de GPT-4",
        "event30.pioneer": "Equipo de Investigación OpenAI (Estados Unidos)",
        "event30.description": "GPT-4 demostró rendimiento a nivel humano en muchos exámenes profesionales, incluyendo puntuar en el percentil 90 en el examen de abogacía. Introdujo capacidades multimodales, procesando tanto texto como imágenes.",
        "badge.agi": "Progreso hacia AGI",

        "event31.title": "Familia Claude 3",
        "event31.pioneer": "Equipo de Investigación Anthropic (Estados Unidos)",
        "event31.description": "Lanzó Claude 3 (Opus, Sonnet, Haiku), con Opus superando a GPT-4 en muchos benchmarks. Claude enfatizó la seguridad, honestidad y utilidad mientras lograba rendimiento de vanguardia.",
        "badge.constitutional": "IA Constitucional",
        "badge.ethical": "IA Ética",

        "event32.title": "Gemini Ultra y Contexto de 2M",
        "event32.pioneer": "Google DeepMind (Reino Unido/Estados Unidos)",
        "event32.description": "Google lanzó Gemini 1.5 con una ventana de contexto sin precedentes de 2 millones de tokens, capaz de procesar horas de video o bases de código completas. Gemini Ultra igualó a GPT-4 en todos los benchmarks.",
        "badge.long-context": "Contexto Largo",

        "event33.title": "DeepSeek-V3 Código Abierto",
        "event33.pioneer": "Liang Wenfeng & DeepSeek (China)",
        "event33.description": "La startup china DeepSeek lanzó V3 (671 mil millones de parámetros) como código abierto, igualando a GPT-4 en rendimiento mientras costaba solo $5.5 millones entrenar. Esto demostró que la IA de vanguardia no requiere presupuestos de miles de millones de dólares.",
        "badge.cost": "Eficiencia de Costos",

        "event34.title": "Avance de GLM-4",
        "event34.pioneer": "Tang Jie & Zhipu AI (China)",
        "event34.description": "GLM-4 de Zhipu AI logró una ventana de contexto de 1 millón de tokens con solo 9 mil millones de parámetros, demostrando capacidades multilingües excepcionales y rendimiento competitivo con modelos occidentales siendo completamente código abierto.",
        "badge.multilingual": "IA Multilingüe",

        // Awards
        "awards.title": "Reconocimientos y Premios Principales",
        "awards.description": "Los pioneros que transformaron la IA han sido honrados con los máximos galardones en ciencia y tecnología.",
        "award1.title": "Premio Turing 2018",
        "award1.recipients": "Geoffrey Hinton, Yoshua Bengio, Yann LeCun",
        "award1.description": "El Premio Nobel de la Computación por avances conceptuales y técnicos en redes neuronales profundas.",
        "award2.title": "Premio Turing 2011",
        "award2.recipients": "Judea Pearl",
        "award2.description": "Por contribuciones fundamentales a la IA a través del razonamiento probabilístico y causal.",
        "award3.title": "Premio Nobel de Química 2024",
        "award3.recipients": "Demis Hassabis (DeepMind)",
        "award3.description": "Por el avance de AlphaFold2 en la predicción de estructura de proteínas.",
        "award4.title": "Medalla de Honor IEEE 2022",
        "award4.recipients": "Yann LeCun",
        "award4.description": "Por contribuciones pioneras al aprendizaje profundo y redes neuronales convolucionales.",
        "award5.title": "Premio Princesa de Asturias 2022",
        "award5.recipients": "Demis Hassabis",
        "award5.description": "Por contribuciones sobresalientes a la investigación científica y técnica a través de la IA.",
        "award6.title": "TIME 100 Más Influyentes",
        "award6.recipients": "Sam Altman (2023), Dario Amodei (2024)",
        "award6.description": "Reconocidos por liderar la revolución de la IA generativa y dar forma a su futuro.",

        // Footer
        "footer.description": "Tu guía definitiva de herramientas y tecnologías de IA. Descubre, compara y domina las mejores soluciones de IA.",
        "footer.quick-links": "Enlaces Rápidos",
        "footer.resources": "Recursos",
        "footer.follow": "Síguenos",
        "footer.copyright": "© 2024 TechVernia. Todos los derechos reservados."
    },

    de: {
        "nav.home": "Startseite",
        "nav.categories": "Kategorien",
        "nav.guides": "Anleitungen",
        "nav.compare": "Vergleichen",
        "nav.ai-history": "KI-Geschichte",
        "nav.blog": "Blog",
        "nav.about": "Über uns",
        "nav.contact": "Kontakt",
        "hero.title": "Die Geschichte der Künstlichen Intelligenz",
        "hero.description": "Von den visionären Pionieren der 1950er Jahre bis zu den bahnbrechenden Modellen von heute.",
        "footer.copyright": "© 2024 TechVernia. Alle Rechte vorbehalten."
    },

    pt: {
        "nav.home": "Início",
        "nav.categories": "Categorias",
        "nav.guides": "Guias",
        "nav.compare": "Comparar",
        "nav.ai-history": "História da IA",
        "nav.blog": "Blog",
        "nav.about": "Sobre",
        "nav.contact": "Contato",
        "hero.title": "A História da Inteligência Artificial",
        "hero.description": "Dos pioneiros visionários dos anos 1950 aos modelos revolucionários de hoje.",
        "footer.copyright": "© 2024 TechVernia. Todos os direitos reservados."
    },

    zh: {
        "nav.home": "首页",
        "nav.categories": "分类",
        "nav.guides": "指南",
        "nav.compare": "比较",
        "nav.ai-history": "人工智能历史",
        "nav.blog": "博客",
        "nav.about": "关于",
        "nav.contact": "联系",
        "hero.title": "人工智能的历史",
        "hero.description": "从1950年代富有远见的先驱到今天的突破性模型。",
        "footer.copyright": "© 2024 TechVernia。保留所有权利。"
    },

    ja: {
        "nav.home": "ホーム",
        "nav.categories": "カテゴリー",
        "nav.guides": "ガイド",
        "nav.compare": "比較",
        "nav.ai-history": "AI歴史",
        "nav.blog": "ブログ",
        "nav.about": "概要",
        "nav.contact": "お問い合わせ",
        "hero.title": "人工知能の歴史",
        "hero.description": "1950年代の先見的な先駆者から今日の画期的なモデルまで。",
        "footer.copyright": "© 2024 TechVernia。全著作権所有。"
    },

    ko: {
        "nav.home": "홈",
        "nav.categories": "카테고리",
        "nav.guides": "가이드",
        "nav.compare": "비교",
        "nav.ai-history": "AI 역사",
        "nav.blog": "블로그",
        "nav.about": "소개",
        "nav.contact": "연락처",
        "hero.title": "인공지능의 역사",
        "hero.description": "1950년대의 선구적인 개척자들부터 오늘날의 획기적인 모델까지.",
        "footer.copyright": "© 2024 TechVernia. 모든 권리 보유."
    },

    ar: {
        "nav.home": "الرئيسية",
        "nav.categories": "الفئات",
        "nav.guides": "الأدلة",
        "nav.compare": "قارن",
        "nav.ai-history": "تاريخ الذكاء الاصطناعي",
        "nav.blog": "المدونة",
        "nav.about": "حول",
        "nav.contact": "اتصل",
        "hero.title": "تاريخ الذكاء الاصطناعي",
        "hero.description": "من الرواد ذوي الرؤية في الخمسينيات إلى النماذج الرائدة اليوم.",
        "footer.copyright": "© 2024 TechVernia. جميع الحقوق محفوظة."
    },

    hi: {
        "nav.home": "होम",
        "nav.categories": "श्रेणियाँ",
        "nav.guides": "गाइड",
        "nav.compare": "तुलना करें",
        "nav.ai-history": "AI इतिहास",
        "nav.blog": "ब्लॉग",
        "nav.about": "के बारे में",
        "nav.contact": "संपर्क",
        "hero.title": "कृत्रिम बुद्धिमत्ता का इतिहास",
        "hero.description": "1950 के दशक के दूरदर्शी अग्रदूतों से लेकर आज के अभूतपूर्व मॉडलों तक।",
        "footer.copyright": "© 2024 TechVernia। सर्वाधिकार सुरक्षित।"
    }
};

// Translation function with debug logging
function translateAIHistory(lang) {
    console.log('🌍 translateAIHistory called with language:', lang);

    const translations = aiHistoryTranslations[lang] || aiHistoryTranslations.en;
    const elements = document.querySelectorAll('[data-i18n]');
    console.log('📄 Found', elements.length, 'elements with data-i18n attribute');

    let translatedCount = 0;
    let skippedCount = 0;

    elements.forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[key]) {
            element.textContent = translations[key];
            translatedCount++;
        } else {
            console.log('⚠️ No translation found for key:', key, 'in language:', lang);
            skippedCount++;
        }
    });

    console.log('✅ Translated', translatedCount, 'elements');
    console.log('⏭️ Skipped', skippedCount, 'elements');
    console.log('🔧 Available languages:', Object.keys(aiHistoryTranslations));
}

// Initialize translation on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('📱 DOMContentLoaded event fired for AI History page');
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    console.log('💾 Current language from localStorage:', currentLang);
    translateAIHistory(currentLang);
});

// Listen for language changes from main.js
window.addEventListener('languageChanged', (event) => {
    console.log('🔄 languageChanged event received:', event.detail.language);
    translateAIHistory(event.detail.language);
});

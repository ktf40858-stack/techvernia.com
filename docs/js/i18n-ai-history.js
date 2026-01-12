// AI History Page - Multilingual Translations
// 10 Languages: EN, FR, ES, DE, PT, ZH, JA, KO, AR, HI



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
        // Navigation
        "nav.home": "Startseite",
        "nav.categories": "Kategorien",
        "nav.guides": "Anleitungen",
        "nav.compare": "Vergleichen",
        "nav.ai-history": "KI-Geschichte",
        "nav.blog": "Blog",
        "nav.about": "Über uns",
        "nav.contact": "Kontakt",

        // Hero Section
        "hero.title": "Die Geschichte der Künstlichen Intelligenz",
        "hero.description": "Von den visionären Pionieren der 1950er Jahre bis zu den bahnbrechenden Modellen von heute - erkunden Sie die bemerkenswerte Reise der KI-Entwicklung. Entdecken Sie die brillanten Köpfe und bahnbrechenden Momente, die KI von der Theorie zur Realität verwandelten.",

        // Era 1: Founders (1950-1970)
        "era1.badge": "1950 - 1970",
        "era1.title": "Die Gründerära",
        "era1.description": "Die Geburt der KI als akademische Disziplin, in der Pionier-Informatiker die theoretischen und praktischen Grundlagen für künstliche Intelligenz legten.",

        // Events Era 1
        "event1.title": "Der Turing-Test",
        "event1.pioneer": "Alan Turing (Vereinigtes Königreich)",
        "event1.description": "Veröffentlichte 'Computing Machinery and Intelligence' und führte den Turing-Test als Maßstab für Maschinenintelligenz ein. Dieses wegweisende Papier stellte die grundlegende Frage: Können Maschinen denken?",
        "badge.theoretical": "Theoretische Grundlage",
        "badge.philosophy": "Philosophie der KI",

        "event2.title": "Erstes Neuronales Netzwerk",
        "event2.pioneer": "Marvin Minsky (Vereinigte Staaten)",
        "event2.description": "Schuf SNARC (Stochastic Neural Analog Reinforcement Calculator), die erste künstliche neuronale Netzwerkmaschine mit 40 Neuronen. Diese Pionierarbeit zeigte, dass Maschinen aus Erfahrung lernen können.",
        "badge.neural": "Neuronale Netze",
        "badge.ml": "Maschinelles Lernen",

        "event3.title": "Logic Theorist Programm",
        "event3.pioneer": "Allen Newell & Herbert Simon (Vereinigte Staaten)",
        "event3.description": "Entwickelte den Logic Theorist, das erste KI-Programm. Es konnte mathematische Theoreme aus Russell und Whiteheads Principia Mathematica beweisen, manchmal elegantere Beweise als die Originalautoren finden.",
        "badge.symbolic": "Symbolische KI",
        "badge.reasoning": "Automatisiertes Schlussfolgern",

        "event4.title": "Geburt der Künstlichen Intelligenz",
        "event4.pioneer": "John McCarthy (Vereinigte Staaten)",
        "event4.description": "Organisierte die Dartmouth-Konferenz, bei der der Begriff 'Künstliche Intelligenz' geprägt wurde. Dieser historische Sommerworkshop brachte die klügsten Köpfe zusammen, um Maschinenintelligenz zu erforschen und KI als formales akademisches Feld zu etablieren.",
        "badge.dartmouth": "Dartmouth-Konferenz",
        "badge.founding": "Feldgründung",

        "event5.title": "LISP Programmiersprache",
        "event5.pioneer": "John McCarthy (Vereinigte Staaten)",
        "event5.description": "Schuf LISP, die zweitälteste Hochsprache, die heute noch verwendet wird. LISP wurde jahrzehntelang zur dominierenden Sprache für KI-Forschung und führte revolutionäre Konzepte wie Garbage Collection und Baumdatenstrukturen ein.",
        "badge.programming": "Programmiersprache",
        "badge.symbolic-processing": "Symbolische Verarbeitung",

        "event6.title": "Das Perzeptron",
        "event6.pioneer": "Frank Rosenblatt (Vereinigte Staaten)",
        "event6.description": "Erfand das Perzeptron, das erste künstliche neuronale Netzwerk zur Mustererkennung. Das Mark I Perzeptron konnte lernen, einfache Muster zu klassifizieren und legte damit den Grundstein für modernes Deep Learning.",
        "badge.pattern": "Mustererkennung",

        "event7.title": "MIT KI-Labor",
        "event7.pioneer": "Marvin Minsky & John McCarthy (Vereinigte Staaten)",
        "event7.description": "Mitbegründer des MIT Artificial Intelligence Laboratory, das zu einem der weltweit führenden KI-Forschungszentren wurde. Das Labor produzierte bahnbrechende Arbeiten in Computer Vision, Robotik und maschinellem Lernen.",
        "badge.institution": "Forschungseinrichtung",
        "badge.leadership": "Akademische Führung",

        // Era 2: Expert Systems (1970-1990)
        "era2.badge": "1970 - 1990",
        "era2.title": "Die Expertensystem-Ära",
        "era2.description": "KI entwickelte sich von theoretischer Forschung zu praktischen Anwendungen, mit Expertensystemen, die reale Probleme in Medizin, Chemie und Wirtschaft lösten.",

        "event8.title": "DENDRAL - Erstes Expertensystem",
        "event8.pioneer": "Edward Feigenbaum (Vereinigte Staaten)",
        "event8.description": "Entwickelte DENDRAL, das erste Expertensystem zur Identifizierung organischer Moleküle. Dieses bahnbrechende Projekt zeigte, dass KI menschliche Expertenleistung in spezialisierten Bereichen erreichen oder übertreffen kann.",
        "badge.expert": "Expertensysteme",
        "badge.chemistry": "Chemie-KI",

        "event9.title": "MYCIN Medizinische Diagnose",
        "event9.pioneer": "Edward Feigenbaum & Team (Vereinigte Staaten)",
        "event9.description": "Schuf MYCIN, ein Expertensystem zur Diagnose bakterieller Infektionen und Empfehlung von Antibiotika. Es erreichte 69% Genauigkeit im Vergleich zu 65% bei menschlichen Experten und bewies das Potenzial von KI im Gesundheitswesen.",
        "badge.medical": "Medizinische KI",

        "event10.title": "Backpropagation-Revolution",
        "event10.pioneer": "Geoffrey Hinton (Kanada), David Rumelhart & Ronald Williams (USA)",
        "event10.description": "Popularisierte den Backpropagation-Algorithmus, der es neuronalen Netzen ermöglichte, komplexe Muster durch effiziente Gradientenberechnung zu lernen. Dieser Durchbruch belebte die neuronale Netzwerkforschung nach Jahren der Stagnation wieder.",
        "badge.deep": "Deep Learning",

        "event11.title": "Bayessche Netze",
        "event11.pioneer": "Judea Pearl (Vereinigte Staaten)",
        "event11.description": "Revolutionierte probabilistisches Schlussfolgern mit Bayesschen Netzen und lieferte einen Rahmen für die Darstellung und das Schlussfolgern über Unsicherheit. Diese Arbeit brachte ihm 2011 den Turing Award ein.",
        "badge.probabilistic": "Probabilistische KI",
        "badge.causal": "Kausale Inferenz",

        "event12.title": "Convolutional Neural Networks",
        "event12.pioneer": "Yann LeCun (Frankreich)",
        "event12.description": "Entwickelte Convolutional Neural Networks (CNNs) und wendete sie erfolgreich auf handgeschriebene Ziffernerkennung an. LeNet konnte Postleitzahlen mit außergewöhnlicher Genauigkeit lesen und war Pionier in Computer Vision.",
        "badge.vision": "Computer Vision",
        "badge.cnn": "Faltungsnetze",

        // Era 3: Deep Learning Renaissance (1997-2012)
        "era3.badge": "1997 - 2012",
        "era3.title": "Die Deep Learning Renaissance",
        "era3.description": "Neuronale Netze erlebten ein beeindruckendes Comeback mit neuen Architekturen und erhöhter Rechenleistung und bereiteten den Weg für die KI-Revolution.",

        "event13.title": "Deep Blue besiegt Kasparov",
        "event13.pioneer": "IBM Forschungsteam (Vereinigte Staaten)",
        "event13.description": "IBMs Deep Blue wurde der erste Computer, der einen amtierenden Schachweltmeister in einem Match besiegte. Dieser historische Sieg zeigte, dass Maschinen Menschen in komplexem strategischem Denken übertreffen können.",
        "badge.game": "Spiel-KI",
        "badge.milestone": "Meilenstein-Leistung",

        "event14.title": "LSTM-Netze",
        "event14.pioneer": "Sepp Hochreiter (Österreich) & Jürgen Schmidhuber (Schweiz)",
        "event14.description": "Erfand Long Short-Term Memory (LSTM) Netze und löste das Vanishing-Gradient-Problem, das rekurrente neuronale Netze plagte. LSTMs wurden grundlegend für Spracherkennung und Sprachverarbeitung.",
        "badge.rnn": "Rekurrente Netze",
        "badge.sequence": "Sequenzlernen",

        "event15.title": "ImageNet-Datensatz",
        "event15.pioneer": "Fei-Fei Li (China/Vereinigte Staaten)",
        "event15.description": "Schuf ImageNet, einen massiven Datensatz mit 14 Millionen beschrifteten Bildern in 20.000 Kategorien. Dieser Datensatz wurde zum Benchmark, der die Deep-Learning-Revolution in Computer Vision katalysierte.",
        "badge.dataset": "Datensatz-Erstellung",

        "event16.title": "Google Brain Projekt",
        "event16.pioneer": "Andrew Ng & Jeff Dean (Vereinigte Staaten)",
        "event16.description": "Startete Google Brain unter Verwendung massiver Rechenressourcen zum Training tiefer neuronaler Netze. Das berühmte Katzenerkennungs-Experiment zeigte, dass neuronale Netze lernen können, Konzepte ohne explizite Programmierung zu identifizieren.",
        "badge.large-scale": "Großes ML",
        "badge.unsupervised": "Unüberwachtes Lernen",

        "event17.title": "AlexNets Triumph",
        "event17.pioneer": "Alex Krizhevsky, Geoffrey Hinton & Ilya Sutskever (Kanada)",
        "event17.description": "AlexNet gewann den ImageNet-Wettbewerb mit einer rekordverdächtigen Fehlerrate von 15,3% und zerquetschte frühere Methoden. Dieser entscheidende Sieg entfachte die Deep-Learning-Revolution und bewies die Kraft GPU-trainierter neuronaler Netze.",
        "badge.breakthrough": "Deep-Learning-Durchbruch",

        // Era 4: Modern AI (2012-2020)
        "era4.badge": "2012 - 2020",
        "era4.title": "Die Moderne KI-Ära",
        "era4.description": "Deep Learning wurde zum Mainstream und erreichte übermenschliche Leistung in Spielen, Vision und Sprachaufgaben, während neue KI-Unternehmen entstanden, um diese Durchbrüche zu kommerzialisieren.",

        "event18.title": "Generative Adversarial Networks",
        "event18.pioneer": "Ian Goodfellow (Vereinigte Staaten)",
        "event18.description": "Erfand GANs, eine revolutionäre Architektur, bei der zwei neuronale Netze konkurrieren: eines generiert gefälschte Daten, das andere versucht, sie zu erkennen. GANs ermöglichten Bildgenerierung mit beispiellosem Realismus.",
        "badge.generative": "Generative KI",
        "badge.image-gen": "Bildgenerierung",

        "event19.title": "OpenAI gegründet",
        "event19.pioneer": "Elon Musk, Sam Altman, Ilya Sutskever & Andere (Vereinigte Staaten)",
        "event19.description": "Als gemeinnütziges KI-Forschungsunternehmen mit 1 Milliarde Dollar Zusagen gegründet, um sicherzustellen, dass AGI der gesamten Menschheit zugute kommt. OpenAI würde später GPT und ChatGPT erstellen.",
        "badge.safety": "KI-Sicherheit",
        "badge.research-lab": "Forschungslabor",

        "event20.title": "AlphaGo besiegt Lee Sedol",
        "event20.pioneer": "Demis Hassabis & DeepMind Team (Vereinigtes Königreich)",
        "event20.description": "AlphaGo besiegte den Weltmeister Lee Sedol 4-1 in Go, einem Spiel mit mehr möglichen Positionen als Atomen im Universum. Diese beeindruckende Leistung zeigte die Fähigkeit der KI, intuitive, kreative Aufgaben zu meistern.",
        "badge.reinforcement": "Verstärkendes Lernen",

        "event21.title": "Deep Learning Turing Award",
        "event21.pioneer": "Geoffrey Hinton (Kanada), Yoshua Bengio (Kanada) & Yann LeCun (Frankreich)",
        "event21.description": "Die Paten der KI erhielten den Turing Award für konzeptionelle und technische Durchbrüche, die tiefe neuronale Netze zu einer kritischen Komponente des Computing machten. Ihre drei Jahrzehnte währende Arbeit erhielt endlich Anerkennung.",
        "badge.nobel-computing": "Nobel des Computing",

        "event22.title": "AlphaFold löst Proteinfaltung",
        "event22.pioneer": "Demis Hassabis & DeepMind Team (Vereinigtes Königreich)",
        "event22.description": "AlphaFold2 löste das 50 Jahre alte Proteinfaltungsproblem und sagte 3D-Proteinstrukturen mit atomarer Genauigkeit voraus. Dieser Durchbruch beschleunigte die Arzneimittelentwicklung und brachte Hassabis den Nobelpreis für Chemie (2024) ein.",
        "badge.biology": "Computerbiologie",
        "badge.discovery": "Wissenschaftliche Entdeckung",

        // Era 5: Generative AI (2017-Present)
        "era5.badge": "2017 - Gegenwart",
        "era5.title": "Die Generative KI-Ära",
        "era5.description": "Transformer-Architektur und große Sprachmodelle revolutionierten KI, machten sie Milliarden zugänglich und veränderten, wie Menschen mit Technologie interagieren.",

        "event23.title": "Attention Is All You Need",
        "event23.pioneer": "Ashish Vaswani & Google Brain Team (Vereinigte Staaten)",
        "event23.description": "Veröffentlichte das Transformer-Papier und führte den Self-Attention-Mechanismus ein, der Sequenzen parallel verarbeiten konnte. Diese Architektur wurde die Grundlage für GPT, BERT und alle modernen großen Sprachmodelle.",
        "badge.transformer": "Transformer",
        "badge.nlp": "NLP-Revolution",

        "event24.title": "GPT-1: Das erste GPT",
        "event24.pioneer": "Alec Radford & OpenAI (Vereinigte Staaten)",
        "event24.description": "Veröffentlichte GPT-1 mit 117 Millionen Parametern und zeigte, dass Sprachmodelle allgemeines Sprachverständnis durch unüberwachtes Vortraining lernen und starke Leistung über verschiedene Aufgaben erreichen können.",
        "badge.language": "Sprachmodelle",
        "badge.transfer": "Transfer Learning",

        "event25.title": "GPT-2 Zu gefährlich zur Veröffentlichung",
        "event25.pioneer": "Alec Radford & OpenAI (Vereinigte Staaten)",
        "event25.description": "GPT-2 (1,5 Milliarden Parameter) generierte so kohärenten Text, dass OpenAI sich zunächst weigerte, es zu veröffentlichen, unter Berufung auf Missbrauchsbedenken. Dies löste wichtige Debatten über KI-Sicherheit und verantwortungsvolle Offenlegung aus.",
        "badge.llm": "Große Sprachmodelle",
        "badge.ethics": "KI-Ethik",

        "event26.title": "Anthropic gegründet",
        "event26.pioneer": "Dario Amodei & Daniela Amodei (Vereinigte Staaten)",
        "event26.description": "Ehemalige OpenAI-Forscher gründeten Anthropic mit Fokus auf KI-Sicherheit und Aufbau zuverlässiger, interpretierbarer KI-Systeme. Ihr Constitutional-AI-Ansatz zielt darauf ab, kontrollierbarere und ausgerichtete Modelle zu schaffen.",
        "badge.ethics-first": "Ethik-zuerst-KI",

        "event27.title": "DALL-E Bildgenerierung",
        "event27.pioneer": "OpenAI Forschungsteam (Vereinigte Staaten)",
        "event27.description": "DALL-E konnte kreative Bilder aus Textbeschreibungen generieren und zeigte beispielloses cross-modales Verständnis. Es zeigte, dass KI wirklich kreativ sein kann und Konzepte auf neuartige Weise kombiniert.",
        "badge.text-to-image": "Text-zu-Bild",
        "badge.multimodal": "Multimodale KI",

        "event28.title": "Stable Diffusion Open Source",
        "event28.pioneer": "Emad Mostaque & Stability AI (Vereinigtes Königreich)",
        "event28.description": "Veröffentlichte Stable Diffusion als Open Source und demokratisierte KI-Bildgenerierung. Im Gegensatz zu geschlossenen Konkurrenten konnte es jeder lokal ausführen, was eine Explosion kreativer KI-Anwendungen auslöste.",
        "badge.open-source": "Open-Source-KI",

        "event29.title": "ChatGPT-Start",
        "event29.pioneer": "OpenAI & Sam Altman (Vereinigte Staaten)",
        "event29.description": "ChatGPT startete am 30. November 2022 und erreichte in 5 Tagen 1 Million Nutzer und in 2 Monaten 100 Millionen - die am schnellsten wachsende Verbraucheranwendung der Geschichte. Es brachte KI in den Mainstream und veränderte die Welt.",
        "badge.consumer": "Verbraucher-KI",
        "badge.impact": "Kultureller Einfluss",

        "event30.title": "GPT-4 veröffentlicht",
        "event30.pioneer": "OpenAI Forschungsteam (Vereinigte Staaten)",
        "event30.description": "GPT-4 zeigte menschliche Leistung bei vielen professionellen Prüfungen, einschließlich Punktzahl im 90. Perzentil bei der Anwaltsprüfung. Es führte multimodale Fähigkeiten ein und verarbeitete sowohl Text als auch Bilder.",
        "badge.agi": "AGI-Fortschritt",

        "event31.title": "Claude 3 Familie",
        "event31.pioneer": "Anthropic Forschungsteam (Vereinigte Staaten)",
        "event31.description": "Veröffentlichte Claude 3 (Opus, Sonnet, Haiku), wobei Opus GPT-4 bei vielen Benchmarks übertraf. Claude betonte Sicherheit, Ehrlichkeit und Hilfsbereitschaft bei gleichzeitiger Spitzenleistung.",
        "badge.constitutional": "Constitutional AI",
        "badge.ethical": "Ethische KI",

        "event32.title": "Gemini Ultra & 2M Kontext",
        "event32.pioneer": "Google DeepMind (Vereinigtes Königreich/Vereinigte Staaten)",
        "event32.description": "Google veröffentlichte Gemini 1.5 mit einem beispiellosen 2-Millionen-Token-Kontextfenster, das Stunden Video oder ganze Codebasen verarbeiten kann. Gemini Ultra entsprach GPT-4 über alle Benchmarks.",
        "badge.long-context": "Langer Kontext",

        "event33.title": "DeepSeek-V3 Open Source",
        "event33.pioneer": "Liang Wenfeng & DeepSeek (China)",
        "event33.description": "Das chinesische Startup DeepSeek veröffentlichte V3 (671 Milliarden Parameter) als Open Source und erreichte GPT-4-Leistung, während das Training nur 5,5 Millionen Dollar kostete. Dies bewies, dass modernste KI keine Milliarden-Dollar-Budgets erfordert.",
        "badge.cost": "Kosteneffizienz",

        "event34.title": "GLM-4 Durchbruch",
        "event34.pioneer": "Tang Jie & Zhipu AI (China)",
        "event34.description": "Zhipu AIs GLM-4 erreichte ein 1-Millionen-Token-Kontextfenster mit nur 9 Milliarden Parametern, zeigte außergewöhnliche mehrsprachige Fähigkeiten und wettbewerbsfähige Leistung mit westlichen Modellen bei vollständiger Open Source.",
        "badge.multilingual": "Mehrsprachige KI",

        // Awards Section
        "awards.title": "Wichtige Anerkennungen & Auszeichnungen",
        "awards.description": "Die Pioniere, die KI transformierten, wurden mit den höchsten Ehrungen in Wissenschaft und Technologie ausgezeichnet.",
        "award1.title": "Turing Award 2018",
        "award1.recipients": "Geoffrey Hinton, Yoshua Bengio, Yann LeCun",
        "award1.description": "Der Nobelpreis des Computing für konzeptionelle und technische Durchbrüche in tiefen neuronalen Netzen.",
        "award2.title": "Turing Award 2011",
        "award2.recipients": "Judea Pearl",
        "award2.description": "Für grundlegende Beiträge zur KI durch probabilistisches und kausales Schlussfolgern.",
        "award3.title": "Nobelpreis für Chemie 2024",
        "award3.recipients": "Demis Hassabis (DeepMind)",
        "award3.description": "Für AlphaFold2s Durchbruch in der Proteinstrukturvorhersage.",
        "award4.title": "IEEE Ehrenmedaille 2022",
        "award4.recipients": "Yann LeCun",
        "award4.description": "Für bahnbrechende Beiträge zu Deep Learning und Convolutional Neural Networks.",
        "award5.title": "Prinzessin-von-Asturien-Preis 2022",
        "award5.recipients": "Demis Hassabis",
        "award5.description": "Für herausragende Beiträge zur wissenschaftlichen und technischen Forschung durch KI.",
        "award6.title": "TIME 100 Einflussreichste",
        "award6.recipients": "Sam Altman (2023), Dario Amodei (2024)",
        "award6.description": "Anerkannt für die Führung der generativen KI-Revolution und die Gestaltung ihrer Zukunft.",

        // Footer
        "footer.description": "Ihr ultimativer Leitfaden für KI-Tools und -Technologien. Entdecken, vergleichen und meistern Sie die besten KI-Lösungen.",
        "footer.quick-links": "Schnellzugriff",
        "footer.resources": "Ressourcen",
        "footer.follow": "Folgen Sie uns",
        "footer.copyright": "© 2024 TechVernia. Alle Rechte vorbehalten."
    },

    pt: {
        // Navigation
        "nav.home": "Início",
        "nav.categories": "Categorias",
        "nav.guides": "Guias",
        "nav.compare": "Comparar",
        "nav.ai-history": "História da IA",
        "nav.blog": "Blog",
        "nav.about": "Sobre",
        "nav.contact": "Contato",

        // Hero Section
        "hero.title": "A História da Inteligência Artificial",
        "hero.description": "Dos pioneiros visionários dos anos 1950 aos modelos revolucionários de hoje, explore a jornada notável do desenvolvimento da IA. Descubra as mentes brilhantes e os momentos revolucionários que transformaram a IA da teoria à realidade.",

        // Era 1: Founders (1950-1970)
        "era1.badge": "1950 - 1970",
        "era1.title": "A Era dos Fundadores",
        "era1.description": "O nascimento da IA como disciplina acadêmica, onde cientistas da computação pioneiros estabeleceram as bases teóricas e práticas da inteligência artificial.",

        // Events Era 1
        "event1.title": "O Teste de Turing",
        "event1.pioneer": "Alan Turing (Reino Unido)",
        "event1.description": "Publicou 'Computing Machinery and Intelligence', introduzindo o Teste de Turing como medida de inteligência de máquinas. Este artigo seminal levantou a questão fundamental: As máquinas podem pensar?",
        "badge.theoretical": "Fundamento Teórico",
        "badge.philosophy": "Filosofia da IA",

        "event2.title": "Primeira Rede Neural",
        "event2.pioneer": "Marvin Minsky (Estados Unidos)",
        "event2.description": "Criou SNARC (Calculadora de Reforço Analógico Neural Estocástico), a primeira máquina de rede neural artificial com 40 neurônios. Este trabalho pioneiro demonstrou que máquinas podem aprender com a experiência.",
        "badge.neural": "Redes Neurais",
        "badge.ml": "Aprendizado de Máquina",

        "event3.title": "Programa Logic Theorist",
        "event3.pioneer": "Allen Newell & Herbert Simon (Estados Unidos)",
        "event3.description": "Desenvolveu o Logic Theorist, considerado o primeiro programa de IA. Ele podia provar teoremas matemáticos do Principia Mathematica de Russell e Whitehead, às vezes encontrando provas mais elegantes que os autores originais.",
        "badge.symbolic": "IA Simbólica",
        "badge.reasoning": "Raciocínio Automatizado",

        "event4.title": "Nascimento da Inteligência Artificial",
        "event4.pioneer": "John McCarthy (Estados Unidos)",
        "event4.description": "Organizou a Conferência de Dartmouth, onde o termo 'Inteligência Artificial' foi cunhado. Este histórico workshop de verão reuniu as mentes mais brilhantes para explorar a inteligência das máquinas, estabelecendo a IA como campo acadêmico formal.",
        "badge.dartmouth": "Conferência de Dartmouth",
        "badge.founding": "Fundação do Campo",

        "event5.title": "Linguagem de Programação LISP",
        "event5.pioneer": "John McCarthy (Estados Unidos)",
        "event5.description": "Criou LISP, a segunda linguagem de programação de alto nível mais antiga ainda em uso hoje. LISP tornou-se a linguagem dominante para pesquisa em IA por décadas, introduzindo conceitos revolucionários como coleta de lixo e estruturas de dados em árvore.",
        "badge.programming": "Linguagem de Programação",
        "badge.symbolic-processing": "Processamento Simbólico",

        "event6.title": "O Perceptron",
        "event6.pioneer": "Frank Rosenblatt (Estados Unidos)",
        "event6.description": "Inventou o Perceptron, a primeira rede neural artificial para reconhecimento de padrões. O Perceptron Mark I podia aprender a classificar padrões simples, lançando as bases para o aprendizado profundo moderno.",
        "badge.pattern": "Reconhecimento de Padrões",

        "event7.title": "Laboratório de IA do MIT",
        "event7.pioneer": "Marvin Minsky & John McCarthy (Estados Unidos)",
        "event7.description": "Co-fundaram o Laboratório de Inteligência Artificial do MIT, que se tornou um dos principais centros de pesquisa em IA do mundo. O laboratório produziu trabalhos revolucionários em visão computacional, robótica e aprendizado de máquina.",
        "badge.institution": "Instituição de Pesquisa",
        "badge.leadership": "Liderança Acadêmica",

        // Era 2: Expert Systems (1970-1990)
        "era2.badge": "1970 - 1990",
        "era2.title": "A Era dos Sistemas Especialistas",
        "era2.description": "A IA passou da pesquisa teórica para aplicações práticas, com sistemas especialistas resolvendo problemas do mundo real em medicina, química e negócios.",

        "event8.title": "DENDRAL - Primeiro Sistema Especialista",
        "event8.pioneer": "Edward Feigenbaum (Estados Unidos)",
        "event8.description": "Desenvolveu DENDRAL, o primeiro sistema especialista capaz de identificar moléculas orgânicas. Este projeto revolucionário demonstrou que a IA poderia igualar ou superar o desempenho de especialistas humanos em domínios especializados.",
        "badge.expert": "Sistemas Especialistas",
        "badge.chemistry": "IA em Química",

        "event9.title": "Diagnóstico Médico MYCIN",
        "event9.pioneer": "Edward Feigenbaum & Equipe (Estados Unidos)",
        "event9.description": "Criou MYCIN, um sistema especialista para diagnosticar infecções bacterianas e recomendar antibióticos. Alcançou 69% de precisão em comparação com 65% dos especialistas humanos, provando o potencial da IA na saúde.",
        "badge.medical": "IA Médica",

        "event10.title": "Revolução do Backpropagation",
        "event10.pioneer": "Geoffrey Hinton (Canadá), David Rumelhart & Ronald Williams (EUA)",
        "event10.description": "Popularizou o algoritmo de backpropagation, permitindo que redes neurais aprendessem padrões complexos através do cálculo eficiente de gradientes. Este avanço revitalizou a pesquisa em redes neurais após anos de estagnação.",
        "badge.deep": "Aprendizado Profundo",

        "event11.title": "Redes Bayesianas",
        "event11.pioneer": "Judea Pearl (Estados Unidos)",
        "event11.description": "Revolucionou o raciocínio probabilístico com redes bayesianas, fornecendo uma estrutura para representar e raciocinar sobre incerteza. Este trabalho lhe rendeu o Prêmio Turing em 2011.",
        "badge.probabilistic": "IA Probabilística",
        "badge.causal": "Inferência Causal",

        "event12.title": "Redes Neurais Convolucionais",
        "event12.pioneer": "Yann LeCun (França)",
        "event12.description": "Desenvolveu Redes Neurais Convolucionais (CNNs) e as aplicou com sucesso ao reconhecimento de dígitos manuscritos. LeNet podia ler códigos postais com precisão excepcional, sendo pioneira em visão computacional.",
        "badge.vision": "Visão Computacional",
        "badge.cnn": "Redes Convolucionais",

        // Era 3: Deep Learning Renaissance (1997-2012)
        "era3.badge": "1997 - 2012",
        "era3.title": "O Renascimento do Aprendizado Profundo",
        "era3.description": "Redes neurais fizeram um retorno impressionante com novas arquiteturas e maior poder computacional, preparando o terreno para a revolução da IA.",

        "event13.title": "Deep Blue Derrota Kasparov",
        "event13.pioneer": "Equipe de Pesquisa IBM (Estados Unidos)",
        "event13.description": "O Deep Blue da IBM se tornou o primeiro computador a derrotar um campeão mundial de xadrez reinante em uma partida. Esta vitória histórica demonstrou que máquinas podem superar humanos em pensamento estratégico complexo.",
        "badge.game": "IA de Jogos",
        "badge.milestone": "Conquista Histórica",

        "event14.title": "Redes LSTM",
        "event14.pioneer": "Sepp Hochreiter (Áustria) & Jürgen Schmidhuber (Suíça)",
        "event14.description": "Inventou redes Long Short-Term Memory (LSTM), resolvendo o problema do gradiente que desaparecia que afetava redes neurais recorrentes. LSTMs se tornaram fundamentais para reconhecimento de fala e processamento de linguagem.",
        "badge.rnn": "Redes Recorrentes",
        "badge.sequence": "Aprendizado de Sequências",

        "event15.title": "Dataset ImageNet",
        "event15.pioneer": "Fei-Fei Li (China/Estados Unidos)",
        "event15.description": "Criou ImageNet, um dataset massivo com 14 milhões de imagens rotuladas em 20.000 categorias. Este dataset se tornou o benchmark que catalisou a revolução do aprendizado profundo em visão computacional.",
        "badge.dataset": "Criação de Dataset",

        "event16.title": "Projeto Google Brain",
        "event16.pioneer": "Andrew Ng & Jeff Dean (Estados Unidos)",
        "event16.description": "Lançou o Google Brain, usando recursos computacionais massivos para treinar redes neurais profundas. O famoso experimento de reconhecimento de gatos mostrou que redes neurais podem aprender a identificar conceitos sem programação explícita.",
        "badge.large-scale": "ML em Grande Escala",
        "badge.unsupervised": "Aprendizado Não Supervisionado",

        "event17.title": "O Triunfo do AlexNet",
        "event17.pioneer": "Alex Krizhevsky, Geoffrey Hinton & Ilya Sutskever (Canadá)",
        "event17.description": "AlexNet venceu a competição ImageNet com uma taxa de erro recorde de 15,3%, esmagando métodos anteriores. Esta vitória decisiva acendeu a revolução do aprendizado profundo, provando o poder das redes neurais treinadas em GPU.",
        "badge.breakthrough": "Avanço em Aprendizado Profundo",

        // Era 4: Modern AI (2012-2020)
        "era4.badge": "2012 - 2020",
        "era4.title": "A Era da IA Moderna",
        "era4.description": "O aprendizado profundo se tornou mainstream, alcançando desempenho sobre-humano em jogos, visão e tarefas de linguagem, enquanto novas empresas de IA surgiram para comercializar esses avanços.",

        "event18.title": "Redes Adversariais Generativas",
        "event18.pioneer": "Ian Goodfellow (Estados Unidos)",
        "event18.description": "Inventou GANs, uma arquitetura revolucionária onde duas redes neurais competem: uma gera dados falsos, a outra tenta detectá-los. GANs permitiram geração de imagens com realismo sem precedentes.",
        "badge.generative": "IA Generativa",
        "badge.image-gen": "Geração de Imagens",

        "event19.title": "OpenAI Fundada",
        "event19.pioneer": "Elon Musk, Sam Altman, Ilya Sutskever & Outros (Estados Unidos)",
        "event19.description": "Fundada como empresa de pesquisa de IA sem fins lucrativos com US$ 1 bilhão em compromissos, visando garantir que a AGI beneficie toda a humanidade. A OpenAI criaria mais tarde GPT e ChatGPT.",
        "badge.safety": "Segurança da IA",
        "badge.research-lab": "Laboratório de Pesquisa",

        "event20.title": "AlphaGo Derrota Lee Sedol",
        "event20.pioneer": "Demis Hassabis & Equipe DeepMind (Reino Unido)",
        "event20.description": "AlphaGo derrotou o campeão mundial Lee Sedol 4-1 em Go, um jogo com mais posições possíveis do que átomos no universo. Esta conquista impressionante mostrou a capacidade da IA de dominar tarefas intuitivas e criativas.",
        "badge.reinforcement": "Aprendizado por Reforço",

        "event21.title": "Prêmio Turing de Aprendizado Profundo",
        "event21.pioneer": "Geoffrey Hinton (Canadá), Yoshua Bengio (Canadá) & Yann LeCun (França)",
        "event21.description": "Os Padrinhos da IA receberam o Prêmio Turing por avanços conceituais e técnicos que tornaram redes neurais profundas um componente crítico da computação. Seu trabalho de três décadas finalmente recebeu reconhecimento.",
        "badge.nobel-computing": "Nobel da Computação",

        "event22.title": "AlphaFold Resolve Dobramento de Proteínas",
        "event22.pioneer": "Demis Hassabis & Equipe DeepMind (Reino Unido)",
        "event22.description": "AlphaFold2 resolveu o problema do dobramento de proteínas de 50 anos, prevendo estruturas de proteínas 3D com precisão atômica. Este avanço acelerou a descoberta de medicamentos e rendeu a Hassabis o Prêmio Nobel de Química (2024).",
        "badge.biology": "Biologia Computacional",
        "badge.discovery": "Descoberta Científica",

        // Era 5: Generative AI (2017-Present)
        "era5.badge": "2017 - Presente",
        "era5.title": "A Era da IA Generativa",
        "era5.description": "A arquitetura Transformer e modelos de linguagem grandes revolucionaram a IA, tornando-a acessível a bilhões e transformando como humanos interagem com a tecnologia.",

        "event23.title": "Atenção É Tudo Que Você Precisa",
        "event23.pioneer": "Ashish Vaswani & Equipe Google Brain (Estados Unidos)",
        "event23.description": "Publicou o artigo Transformer, introduzindo o mecanismo de auto-atenção que podia processar sequências em paralelo. Esta arquitetura se tornou a base para GPT, BERT e todos os modelos de linguagem grandes modernos.",
        "badge.transformer": "Transformer",
        "badge.nlp": "Revolução NLP",

        "event24.title": "GPT-1: O Primeiro GPT",
        "event24.pioneer": "Alec Radford & OpenAI (Estados Unidos)",
        "event24.description": "Lançou GPT-1 com 117 milhões de parâmetros, demonstrando que modelos de linguagem podem aprender compreensão geral da linguagem através de pré-treinamento não supervisionado e alcançar forte desempenho em diversas tarefas.",
        "badge.language": "Modelos de Linguagem",
        "badge.transfer": "Aprendizado por Transferência",

        "event25.title": "GPT-2 Perigoso Demais para Lançar",
        "event25.pioneer": "Alec Radford & OpenAI (Estados Unidos)",
        "event25.description": "GPT-2 (1,5 bilhão de parâmetros) gerava texto tão coerente que a OpenAI inicialmente recusou lançá-lo, citando preocupações com uso indevido. Isso desencadeou debates importantes sobre segurança da IA e divulgação responsável.",
        "badge.llm": "Grandes Modelos de Linguagem",
        "badge.ethics": "Ética da IA",

        "event26.title": "Anthropic Fundada",
        "event26.pioneer": "Dario Amodei & Daniela Amodei (Estados Unidos)",
        "event26.description": "Ex-pesquisadores da OpenAI fundaram a Anthropic, focando em segurança da IA e construindo sistemas de IA confiáveis e interpretáveis. Sua abordagem de IA Constitucional visa criar modelos mais controláveis e alinhados.",
        "badge.ethics-first": "IA Ética em Primeiro Lugar",

        "event27.title": "Geração de Imagens DALL-E",
        "event27.pioneer": "Equipe de Pesquisa OpenAI (Estados Unidos)",
        "event27.description": "DALL-E podia gerar imagens criativas a partir de descrições de texto, demonstrando compreensão cross-modal sem precedentes. Mostrou que a IA pode ser verdadeiramente criativa, combinando conceitos de maneiras novas.",
        "badge.text-to-image": "Texto para Imagem",
        "badge.multimodal": "IA Multimodal",

        "event28.title": "Stable Diffusion Código Aberto",
        "event28.pioneer": "Emad Mostaque & Stability AI (Reino Unido)",
        "event28.description": "Lançou Stable Diffusion como código aberto, democratizando a geração de imagens por IA. Ao contrário dos concorrentes fechados, qualquer um poderia executá-lo localmente, desencadeando uma explosão de aplicações de IA criativas.",
        "badge.open-source": "IA de Código Aberto",

        "event29.title": "Lançamento do ChatGPT",
        "event29.pioneer": "OpenAI & Sam Altman (Estados Unidos)",
        "event29.description": "ChatGPT foi lançado em 30 de novembro de 2022, alcançando 1 milhão de usuários em 5 dias e 100 milhões em 2 meses - a aplicação de consumo de crescimento mais rápido da história. Trouxe a IA para o mainstream e mudou o mundo.",
        "badge.consumer": "IA de Consumo",
        "badge.impact": "Impacto Cultural",

        "event30.title": "GPT-4 Lançado",
        "event30.pioneer": "Equipe de Pesquisa OpenAI (Estados Unidos)",
        "event30.description": "GPT-4 demonstrou desempenho em nível humano em muitos exames profissionais, incluindo pontuação no 90º percentil no exame da ordem dos advogados. Introduziu capacidades multimodais, processando texto e imagens.",
        "badge.agi": "Progresso em AGI",

        "event31.title": "Família Claude 3",
        "event31.pioneer": "Equipe de Pesquisa Anthropic (Estados Unidos)",
        "event31.description": "Lançou Claude 3 (Opus, Sonnet, Haiku), com Opus superando GPT-4 em muitos benchmarks. Claude enfatizou segurança, honestidade e utilidade enquanto alcançava desempenho de ponta.",
        "badge.constitutional": "IA Constitucional",
        "badge.ethical": "IA Ética",

        "event32.title": "Gemini Ultra & Contexto de 2M",
        "event32.pioneer": "Google DeepMind (Reino Unido/Estados Unidos)",
        "event32.description": "Google lançou Gemini 1.5 com uma janela de contexto sem precedentes de 2 milhões de tokens, capaz de processar horas de vídeo ou bases de código inteiras. Gemini Ultra igualou GPT-4 em todos os benchmarks.",
        "badge.long-context": "Contexto Longo",

        "event33.title": "DeepSeek-V3 Código Aberto",
        "event33.pioneer": "Liang Wenfeng & DeepSeek (China)",
        "event33.description": "A startup chinesa DeepSeek lançou V3 (671 bilhões de parâmetros) como código aberto, igualando GPT-4 em desempenho enquanto custava apenas US$ 5,5 milhões para treinar. Isso provou que IA de ponta não requer orçamentos de bilhões de dólares.",
        "badge.cost": "Eficiência de Custo",

        "event34.title": "Avanço do GLM-4",
        "event34.pioneer": "Tang Jie & Zhipu AI (China)",
        "event34.description": "GLM-4 da Zhipu AI alcançou uma janela de contexto de 1 milhão de tokens com apenas 9 bilhões de parâmetros, demonstrando capacidades multilíngues excepcionais e desempenho competitivo com modelos ocidentais sendo totalmente código aberto.",
        "badge.multilingual": "IA Multilíngue",

        // Awards Section
        "awards.title": "Principais Reconhecimentos e Prêmios",
        "awards.description": "Os pioneiros que transformaram a IA foram homenageados com as mais altas honrarias em ciência e tecnologia.",
        "award1.title": "Prêmio Turing 2018",
        "award1.recipients": "Geoffrey Hinton, Yoshua Bengio, Yann LeCun",
        "award1.description": "O Prêmio Nobel da Computação por avanços conceituais e técnicos em redes neurais profundas.",
        "award2.title": "Prêmio Turing 2011",
        "award2.recipients": "Judea Pearl",
        "award2.description": "Por contribuições fundamentais à IA através de raciocínio probabilístico e causal.",
        "award3.title": "Prêmio Nobel de Química 2024",
        "award3.recipients": "Demis Hassabis (DeepMind)",
        "award3.description": "Pelo avanço do AlphaFold2 na previsão de estrutura de proteínas.",
        "award4.title": "Medalha de Honra IEEE 2022",
        "award4.recipients": "Yann LeCun",
        "award4.description": "Por contribuições pioneiras ao aprendizado profundo e redes neurais convolucionais.",
        "award5.title": "Prêmio Princesa de Asturias 2022",
        "award5.recipients": "Demis Hassabis",
        "award5.description": "Por contribuições notáveis à pesquisa científica e técnica através da IA.",
        "award6.title": "TIME 100 Mais Influentes",
        "award6.recipients": "Sam Altman (2023), Dario Amodei (2024)",
        "award6.description": "Reconhecidos por liderar a revolução da IA generativa e moldar seu futuro.",

        // Footer
        "footer.description": "Seu guia definitivo para ferramentas e tecnologias de IA. Descubra, compare e domine as melhores soluções de IA.",
        "footer.quick-links": "Links Rápidos",
        "footer.resources": "Recursos",
        "footer.follow": "Siga-nos",
        "footer.copyright": "© 2024 TechVernia. Todos os direitos reservados."
    },

    zh: {
        // Navigation
        "nav.home": "首页",
        "nav.categories": "分类",
        "nav.guides": "指南",
        "nav.compare": "比较",
        "nav.ai-history": "人工智能历史",
        "nav.blog": "博客",
        "nav.about": "关于",
        "nav.contact": "联系",

        // Hero Section
        "hero.title": "人工智能的历史",
        "hero.description": "从1950年代富有远见的先驱到今天的突破性模型，探索人工智能发展的非凡历程。发现将人工智能从理论转化为现实的杰出思想家和突破性时刻。",

        // Era 1: Founders (1950-1970)
        "era1.badge": "1950 - 1970",
        "era1.title": "创始人时代",
        "era1.description": "人工智能作为一门学科的诞生，先驱计算机科学家为人工智能奠定了理论和实践基础。",

        // Events Era 1
        "event1.title": "图灵测试",
        "event1.pioneer": "艾伦·图灵（英国）",
        "event1.description": "发表了《计算机器与智能》，引入图灵测试作为机器智能的衡量标准。这篇开创性论文提出了一个根本性问题：机器能思考吗？",
        "badge.theoretical": "理论基础",
        "badge.philosophy": "人工智能哲学",

        "event2.title": "首个神经网络",
        "event2.pioneer": "马文·明斯基（美国）",
        "event2.description": "创建了SNARC（随机神经模拟强化计算器），第一台拥有40个神经元的人工神经网络机器。这项开创性工作证明了机器可以从经验中学习。",
        "badge.neural": "神经网络",
        "badge.ml": "机器学习",

        "event3.title": "逻辑理论家程序",
        "event3.pioneer": "艾伦·纽厄尔和赫伯特·西蒙（美国）",
        "event3.description": "开发了逻辑理论家，被认为是第一个人工智能程序。它可以证明罗素和怀特海德《数学原理》中的数学定理，有时能找到比原作者更优雅的证明。",
        "badge.symbolic": "符号人工智能",
        "badge.reasoning": "自动推理",

        "event4.title": "人工智能的诞生",
        "event4.pioneer": "约翰·麦卡锡（美国）",
        "event4.description": "组织了达特茅斯会议，人工智能一词在此诞生。这次历史性的夏季研讨会汇聚了最杰出的思想家探索机器智能，确立了人工智能作为正式学术领域。",
        "badge.dartmouth": "达特茅斯会议",
        "badge.founding": "领域创建",

        "event5.title": "LISP编程语言",
        "event5.pioneer": "约翰·麦卡锡（美国）",
        "event5.description": "创建了LISP，这是目前仍在使用的第二古老的高级编程语言。LISP在数十年间成为人工智能研究的主导语言，引入了垃圾收集和树数据结构等革命性概念。",
        "badge.programming": "编程语言",
        "badge.symbolic-processing": "符号处理",

        "event6.title": "感知器",
        "event6.pioneer": "弗兰克·罗森布拉特（美国）",
        "event6.description": "发明了感知器，第一个用于模式识别的人工神经网络。Mark I感知器可以学习分类简单模式，为现代深度学习奠定了基础。",
        "badge.pattern": "模式识别",

        "event7.title": "麻省理工学院人工智能实验室",
        "event7.pioneer": "马文·明斯基和约翰·麦卡锡（美国）",
        "event7.description": "共同创立了麻省理工学院人工智能实验室，该实验室成为世界领先的人工智能研究中心之一。该实验室在计算机视觉、机器人技术和机器学习方面产生了突破性工作。",
        "badge.institution": "研究机构",
        "badge.leadership": "学术领导力",

        // Era 2: Expert Systems (1970-1990)
        "era2.badge": "1970 - 1990",
        "era2.title": "专家系统时代",
        "era2.description": "人工智能从理论研究转向实际应用，专家系统解决了医学、化学和商业领域的实际问题。",

        "event8.title": "DENDRAL - 首个专家系统",
        "event8.pioneer": "爱德华·费根鲍姆（美国）",
        "event8.description": "开发了DENDRAL，第一个能够识别有机分子的专家系统。这个突破性项目证明了人工智能可以在专业领域达到或超越人类专家的表现。",
        "badge.expert": "专家系统",
        "badge.chemistry": "化学人工智能",

        "event9.title": "MYCIN医疗诊断",
        "event9.pioneer": "爱德华·费根鲍姆及团队（美国）",
        "event9.description": "创建了MYCIN，用于诊断细菌感染和推荐抗生素的专家系统。它达到了69%的准确率，而人类专家为65%，证明了人工智能在医疗保健方面的潜力。",
        "badge.medical": "医疗人工智能",

        "event10.title": "反向传播革命",
        "event10.pioneer": "杰弗里·辛顿（加拿大）、大卫·鲁梅尔哈特和罗纳德·威廉姆斯（美国）",
        "event10.description": "推广了反向传播算法，使神经网络能够通过有效计算梯度来学习复杂模式。这一突破在多年停滞后重振了神经网络研究。",
        "badge.deep": "深度学习",

        "event11.title": "贝叶斯网络",
        "event11.pioneer": "朱迪亚·珀尔（美国）",
        "event11.description": "用贝叶斯网络革新了概率推理，提供了表示和推理不确定性的框架。这项工作为他赢得了2011年图灵奖。",
        "badge.probabilistic": "概率人工智能",
        "badge.causal": "因果推理",

        "event12.title": "卷积神经网络",
        "event12.pioneer": "杨立昆（法国）",
        "event12.description": "开发了卷积神经网络（CNN）并成功应用于手写数字识别。LeNet能够以卓越的准确率读取邮政编码，开创了计算机视觉的先河。",
        "badge.vision": "计算机视觉",
        "badge.cnn": "卷积网络",

        // Era 3: Deep Learning Renaissance (1997-2012)
        "era3.badge": "1997 - 2012",
        "era3.title": "深度学习复兴",
        "era3.description": "神经网络以新的架构和增强的计算能力惊人地复兴，为人工智能革命奠定了基础。",

        "event13.title": "深蓝击败卡斯帕罗夫",
        "event13.pioneer": "IBM研究团队（美国）",
        "event13.description": "IBM的深蓝成为第一台在比赛中击败在位世界国际象棋冠军的计算机。这一历史性胜利证明了机器可以在复杂战略思维方面超越人类。",
        "badge.game": "游戏人工智能",
        "badge.milestone": "里程碑成就",

        "event14.title": "LSTM网络",
        "event14.pioneer": "塞普·霍克赖特（奥地利）和于尔根·施密德胡伯（瑞士）",
        "event14.description": "发明了长短期记忆（LSTM）网络，解决了困扰循环神经网络的梯度消失问题。LSTM成为语音识别和语言处理的基础。",
        "badge.rnn": "循环网络",
        "badge.sequence": "序列学习",

        "event15.title": "ImageNet数据集",
        "event15.pioneer": "李飞飞（中国/美国）",
        "event15.description": "创建了ImageNet，一个包含1400万张标记图像的大规模数据集，涵盖2万个类别。该数据集成为催化计算机视觉深度学习革命的基准。",
        "badge.dataset": "数据集创建",

        "event16.title": "谷歌大脑项目",
        "event16.pioneer": "吴恩达和杰夫·迪恩（美国）",
        "event16.description": "启动了谷歌大脑，使用大规模计算资源训练深度神经网络。著名的猫识别实验表明，神经网络可以在没有明确编程的情况下学习识别概念。",
        "badge.large-scale": "大规模机器学习",
        "badge.unsupervised": "无监督学习",

        "event17.title": "AlexNet的胜利",
        "event17.pioneer": "亚历克斯·克里热夫斯基、杰弗里·辛顿和伊利亚·苏茨克维（加拿大）",
        "event17.description": "AlexNet以破纪录的15.3%错误率赢得ImageNet竞赛，碾压了之前的方法。这一决定性胜利点燃了深度学习革命，证明了GPU训练神经网络的力量。",
        "badge.breakthrough": "深度学习突破",

        // Era 4: Modern AI (2012-2020)
        "era4.badge": "2012 - 2020",
        "era4.title": "现代人工智能时代",
        "era4.description": "深度学习成为主流，在游戏、视觉和语言任务方面达到超人表现，同时新的人工智能公司涌现以将这些突破商业化。",

        "event18.title": "生成对抗网络",
        "event18.pioneer": "伊恩·古德费洛（美国）",
        "event18.description": "发明了GAN，一种革命性架构，两个神经网络相互竞争：一个生成假数据，另一个试图检测它。GAN使图像生成达到了前所未有的真实性。",
        "badge.generative": "生成式人工智能",
        "badge.image-gen": "图像生成",

        "event19.title": "OpenAI成立",
        "event19.pioneer": "埃隆·马斯克、萨姆·奥特曼、伊利亚·苏茨克维等人（美国）",
        "event19.description": "作为非营利性人工智能研究公司成立，承诺投入10亿美元，旨在确保AGI造福全人类。OpenAI后来创建了GPT和ChatGPT。",
        "badge.safety": "人工智能安全",
        "badge.research-lab": "研究实验室",

        "event20.title": "AlphaGo击败李世石",
        "event20.pioneer": "杰米斯·哈萨比斯和DeepMind团队（英国）",
        "event20.description": "AlphaGo以4-1击败世界冠军李世石，围棋是一个可能位置比宇宙中的原子还多的游戏。这一惊人成就展示了人工智能掌握直觉性、创造性任务的能力。",
        "badge.reinforcement": "强化学习",

        "event21.title": "深度学习图灵奖",
        "event21.pioneer": "杰弗里·辛顿（加拿大）、约书亚·本吉奥（加拿大）和杨立昆（法国）",
        "event21.description": "人工智能教父们因在概念和工程方面的突破获得图灵奖，这些突破使深度神经网络成为计算的关键组成部分。他们长达三十年的工作终于获得认可。",
        "badge.nobel-computing": "计算机诺贝尔奖",

        "event22.title": "AlphaFold解决蛋白质折叠",
        "event22.pioneer": "杰米斯·哈萨比斯和DeepMind团队（英国）",
        "event22.description": "AlphaFold2解决了50年来的蛋白质折叠问题，以原子级精度预测3D蛋白质结构。这一突破加速了药物发现，并为哈萨比斯赢得了2024年诺贝尔化学奖。",
        "badge.biology": "计算生物学",
        "badge.discovery": "科学发现",

        // Era 5: Generative AI (2017-Present)
        "era5.badge": "2017 - 至今",
        "era5.title": "生成式人工智能时代",
        "era5.description": "Transformer架构和大型语言模型革新了人工智能，使其惠及数十亿人，并改变了人类与技术互动的方式。",

        "event23.title": "注意力机制就是你所需要的",
        "event23.pioneer": "阿希什·瓦斯瓦尼和谷歌大脑团队（美国）",
        "event23.description": "发表了Transformer论文，引入了可以并行处理序列的自注意力机制。这种架构成为GPT、BERT和所有现代大型语言模型的基础。",
        "badge.transformer": "Transformer",
        "badge.nlp": "自然语言处理革命",

        "event24.title": "GPT-1：第一个GPT",
        "event24.pioneer": "亚历克·拉德福德和OpenAI（美国）",
        "event24.description": "发布了拥有1.17亿参数的GPT-1，证明语言模型可以通过无监督预训练学习通用语言理解，并在各种任务上取得强大性能。",
        "badge.language": "语言模型",
        "badge.transfer": "迁移学习",

        "event25.title": "GPT-2太危险不能发布",
        "event25.pioneer": "亚历克·拉德福德和OpenAI（美国）",
        "event25.description": "GPT-2（15亿参数）生成的文本如此连贯，以至于OpenAI最初拒绝发布它，理由是担心被滥用。这引发了关于人工智能安全和负责任披露的重要辩论。",
        "badge.llm": "大型语言模型",
        "badge.ethics": "人工智能伦理",

        "event26.title": "Anthropic成立",
        "event26.pioneer": "达里奥·阿莫代和丹妮拉·阿莫代（美国）",
        "event26.description": "前OpenAI研究人员创立了Anthropic，专注于人工智能安全和构建可靠、可解释的人工智能系统。他们的宪法性人工智能方法旨在创建更可控和对齐的模型。",
        "badge.ethics-first": "伦理优先的人工智能",

        "event27.title": "DALL-E图像生成",
        "event27.pioneer": "OpenAI研究团队（美国）",
        "event27.description": "DALL-E可以从文本描述生成创意图像，展示了前所未有的跨模态理解。它表明人工智能可以真正具有创造性，以新颖的方式组合概念。",
        "badge.text-to-image": "文本到图像",
        "badge.multimodal": "多模态人工智能",

        "event28.title": "Stable Diffusion开源",
        "event28.pioneer": "埃马德·莫斯塔克和Stability AI（英国）",
        "event28.description": "将Stable Diffusion作为开源发布，使人工智能图像生成民主化。与封闭的竞争对手不同，任何人都可以在本地运行它，引发了创意人工智能应用的爆炸式增长。",
        "badge.open-source": "开源人工智能",

        "event29.title": "ChatGPT发布",
        "event29.pioneer": "OpenAI和萨姆·奥特曼（美国）",
        "event29.description": "ChatGPT于2022年11月30日发布，5天内达到100万用户，2个月内达到1亿用户——历史上增长最快的消费应用程序。它将人工智能带入主流并改变了世界。",
        "badge.consumer": "消费者人工智能",
        "badge.impact": "文化影响",

        "event30.title": "GPT-4发布",
        "event30.pioneer": "OpenAI研究团队（美国）",
        "event30.description": "GPT-4在许多专业考试中展示了人类级别的表现，包括在律师资格考试中获得第90百分位的成绩。它引入了多模态能力，可以处理文本和图像。",
        "badge.agi": "通用人工智能进展",

        "event31.title": "Claude 3系列",
        "event31.pioneer": "Anthropic研究团队（美国）",
        "event31.description": "发布了Claude 3（Opus、Sonnet、Haiku），Opus在许多基准测试中超越了GPT-4。Claude强调安全、诚实和有用性，同时实现了最先进的性能。",
        "badge.constitutional": "宪法性人工智能",
        "badge.ethical": "伦理人工智能",

        "event32.title": "Gemini Ultra和200万上下文",
        "event32.pioneer": "谷歌DeepMind（英国/美国）",
        "event32.description": "谷歌发布了Gemini 1.5，拥有前所未有的200万令牌上下文窗口，能够处理数小时的视频或整个代码库。Gemini Ultra在所有基准测试中与GPT-4持平。",
        "badge.long-context": "长上下文",

        "event33.title": "DeepSeek-V3开源",
        "event33.pioneer": "梁文锋和DeepSeek（中国）",
        "event33.description": "中国初创公司DeepSeek将V3（6710亿参数）作为开源发布，性能与GPT-4相当，而训练成本仅为550万美元。这证明了尖端人工智能不需要数十亿美元的预算。",
        "badge.cost": "成本效率",

        "event34.title": "GLM-4突破",
        "event34.pioneer": "唐杰和智谱AI（中国）",
        "event34.description": "智谱AI的GLM-4仅用90亿参数就实现了100万令牌的上下文窗口，展示了卓越的多语言能力，与西方模型相比具有竞争力的性能，同时完全开源。",
        "badge.multilingual": "多语言人工智能",

        // Awards Section
        "awards.title": "主要认可与奖项",
        "awards.description": "改变人工智能的先驱们获得了科学和技术领域的最高荣誉。",
        "award1.title": "2018年图灵奖",
        "award1.recipients": "杰弗里·辛顿、约书亚·本吉奥、杨立昆",
        "award1.description": "因在深度神经网络方面的概念和工程突破而获得计算机诺贝尔奖。",
        "award2.title": "2011年图灵奖",
        "award2.recipients": "朱迪亚·珀尔",
        "award2.description": "通过概率和因果推理对人工智能做出了根本性贡献。",
        "award3.title": "2024年诺贝尔化学奖",
        "award3.recipients": "杰米斯·哈萨比斯（DeepMind）",
        "award3.description": "因AlphaFold2在蛋白质结构预测方面的突破。",
        "award4.title": "2022年IEEE荣誉奖章",
        "award4.recipients": "杨立昆",
        "award4.description": "因对深度学习和卷积神经网络的开创性贡献。",
        "award5.title": "2022年阿斯图里亚斯王子奖",
        "award5.recipients": "杰米斯·哈萨比斯",
        "award5.description": "因通过人工智能对科学和技术研究做出的杰出贡献。",
        "award6.title": "《时代》100位最具影响力人物",
        "award6.recipients": "萨姆·奥特曼（2023）、达里奥·阿莫代（2024）",
        "award6.description": "因领导生成式人工智能革命并塑造其未来而受到认可。",

        // Footer
        "footer.description": "您的人工智能工具和技术终极指南。发现、比较和掌握最佳人工智能解决方案。",
        "footer.quick-links": "快速链接",
        "footer.resources": "资源",
        "footer.follow": "关注我们",
        "footer.copyright": "© 2024 TechVernia。保留所有权利。"
    },

    ja: {
        // Navigation
        "nav.home": "ホーム",
        "nav.categories": "カテゴリー",
        "nav.guides": "ガイド",
        "nav.compare": "比較",
        "nav.ai-history": "AI歴史",
        "nav.blog": "ブログ",
        "nav.about": "概要",
        "nav.contact": "お問い合わせ",

        // Hero Section
        "hero.title": "人工知能の歴史",
        "hero.description": "1950年代の先見的な先駆者から今日の画期的なモデルまで、AI開発の驚くべき旅を探求します。AIを理論から現実へと変えた優れた頭脳と画期的な瞬間を発見してください。",

        // Era 1: Founders (1950-1970)
        "era1.badge": "1950 - 1970",
        "era1.title": "創設者の時代",
        "era1.description": "学問分野としてのAIの誕生。先駆的なコンピュータ科学者たちが人工知能の理論的・実践的基礎を築きました。",

        // Events Era 1
        "event1.title": "チューリングテスト",
        "event1.pioneer": "アラン・チューリング（イギリス）",
        "event1.description": "『計算機械と知能』を発表し、機械の知能を測る尺度としてチューリングテストを導入しました。この画期的な論文は根本的な問いを提起しました：機械は考えることができるか？",
        "badge.theoretical": "理論的基礎",
        "badge.philosophy": "AIの哲学",

        "event2.title": "最初のニューラルネットワーク",
        "event2.pioneer": "マービン・ミンスキー（アメリカ）",
        "event2.description": "SNARC（確率的ニューラルアナログ強化計算機）を作成。40個のニューロンを持つ最初の人工ニューラルネットワークマシンです。この先駆的な研究は、機械が経験から学習できることを実証しました。",
        "badge.neural": "ニューラルネットワーク",
        "badge.ml": "機械学習",

        "event3.title": "ロジック・セオリストプログラム",
        "event3.pioneer": "アレン・ニューウェルとハーバート・サイモン（アメリカ）",
        "event3.description": "最初のAIプログラムと考えられるロジック・セオリストを開発しました。ラッセルとホワイトヘッドの『プリンキピア・マセマティカ』の数学定理を証明でき、時には原著者よりも優雅な証明を見つけることができました。",
        "badge.symbolic": "シンボリックAI",
        "badge.reasoning": "自動推論",

        "event4.title": "人工知能の誕生",
        "event4.pioneer": "ジョン・マッカーシー（アメリカ）",
        "event4.description": "ダートマス会議を組織し、人工知能という用語が生まれました。この歴史的な夏期ワークショップは、機械知能を探求するために最も優秀な頭脳を集め、AIを正式な学問分野として確立しました。",
        "badge.dartmouth": "ダートマス会議",
        "badge.founding": "分野の創設",

        "event5.title": "LISPプログラミング言語",
        "event5.pioneer": "ジョン・マッカーシー（アメリカ）",
        "event5.description": "現在も使用されている2番目に古い高級プログラミング言語であるLISPを作成しました。LISPは数十年にわたってAI研究の支配的な言語となり、ガベージコレクションやツリーデータ構造などの革命的な概念を導入しました。",
        "badge.programming": "プログラミング言語",
        "badge.symbolic-processing": "シンボリック処理",

        "event6.title": "パーセプトロン",
        "event6.pioneer": "フランク・ローゼンブラット（アメリカ）",
        "event6.description": "パターン認識のための最初の人工ニューラルネットワークであるパーセプトロンを発明しました。Mark Iパーセプトロンは単純なパターンを分類することを学習でき、現代の深層学習の基礎を築きました。",
        "badge.pattern": "パターン認識",

        "event7.title": "MIT AI研究所",
        "event7.pioneer": "マービン・ミンスキーとジョン・マッカーシー（アメリカ）",
        "event7.description": "MIT人工知能研究所を共同設立しました。この研究所は世界有数のAI研究センターの1つになりました。研究所はコンピュータビジョン、ロボット工学、機械学習において画期的な研究を生み出しました。",
        "badge.institution": "研究機関",
        "badge.leadership": "学術的リーダーシップ",

        // Era 2: Expert Systems (1970-1990)
        "era2.badge": "1970 - 1990",
        "era2.title": "エキスパートシステムの時代",
        "era2.description": "AIは理論的研究から実用的応用へと移行し、エキスパートシステムが医学、化学、ビジネスにおける実世界の問題を解決しました。",

        "event8.title": "DENDRAL - 最初のエキスパートシステム",
        "event8.pioneer": "エドワード・ファイゲンバウム（アメリカ）",
        "event8.description": "有機分子を識別できる最初のエキスパートシステムであるDENDRALを開発しました。この画期的なプロジェクトは、AIが専門分野で人間の専門家のパフォーマンスに匹敵または凌駕できることを実証しました。",
        "badge.expert": "エキスパートシステム",
        "badge.chemistry": "化学AI",

        "event9.title": "MYCIN医療診断",
        "event9.pioneer": "エドワード・ファイゲンバウムとチーム（アメリカ）",
        "event9.description": "細菌感染を診断し抗生物質を推奨するエキスパートシステムであるMYCINを作成しました。人間の専門家が65%であるのに対し、69%の精度を達成し、医療におけるAIの可能性を証明しました。",
        "badge.medical": "医療AI",

        "event10.title": "バックプロパゲーション革命",
        "event10.pioneer": "ジェフリー・ヒントン（カナダ）、デビッド・ルメルハートとロナルド・ウィリアムズ（アメリカ）",
        "event10.description": "バックプロパゲーションアルゴリズムを普及させ、ニューラルネットワークが効率的に勾配を計算することで複雑なパターンを学習できるようにしました。この画期的な進歩は、長年の停滞の後、ニューラルネットワーク研究を活性化させました。",
        "badge.deep": "深層学習",

        "event11.title": "ベイジアンネットワーク",
        "event11.pioneer": "ジューディア・パール（アメリカ）",
        "event11.description": "ベイジアンネットワークで確率的推論に革命を起こし、不確実性を表現し推論するためのフレームワークを提供しました。この研究により、彼は2011年のチューリング賞を受賞しました。",
        "badge.probabilistic": "確率的AI",
        "badge.causal": "因果推論",

        "event12.title": "畳み込みニューラルネットワーク",
        "event12.pioneer": "ヤン・ルカン（フランス）",
        "event12.description": "畳み込みニューラルネットワーク（CNN）を開発し、手書き数字認識に成功しました。LeNetは郵便番号を驚異的な精度で読み取ることができ、コンピュータビジョンのパイオニアとなりました。",
        "badge.vision": "コンピュータビジョン",
        "badge.cnn": "畳み込みネットワーク",

        // Era 3: Deep Learning Renaissance (1997-2012)
        "era3.badge": "1997 - 2012",
        "era3.title": "深層学習ルネサンス",
        "era3.description": "ニューラルネットワークは新しいアーキテクチャと強化された計算能力で驚異的な復活を遂げ、AI革命への道を開きました。",

        "event13.title": "ディープブルーがカスパロフを破る",
        "event13.pioneer": "IBM研究チーム（アメリカ）",
        "event13.description": "IBMのディープブルーは、マッチで現役の世界チェスチャンピオンを破った最初のコンピュータとなりました。この歴史的な勝利は、機械が複雑な戦略的思考において人間を凌駕できることを実証しました。",
        "badge.game": "ゲームAI",
        "badge.milestone": "マイルストーン達成",

        "event14.title": "LSTMネットワーク",
        "event14.pioneer": "セップ・ホックライターとユルゲン・シュミットフーバー（スイス）",
        "event14.description": "長短期記憶（LSTM）ネットワークを発明し、再帰型ニューラルネットワークを悩ませていた勾配消失問題を解決しました。LSTMは音声認識と言語処理の基礎となりました。",
        "badge.rnn": "再帰型ネットワーク",
        "badge.sequence": "シーケンス学習",

        "event15.title": "ImageNetデータセット",
        "event15.pioneer": "フェイフェイ・リー（中国/アメリカ）",
        "event15.description": "2万カテゴリにわたる1400万枚のラベル付き画像を持つ大規模データセットImageNetを作成しました。このデータセットは、コンピュータビジョンにおける深層学習革命を触媒したベンチマークとなりました。",
        "badge.dataset": "データセット作成",

        "event16.title": "Google Brainプロジェクト",
        "event16.pioneer": "アンドリュー・ングとジェフ・ディーン（アメリカ）",
        "event16.description": "Google Brainを立ち上げ、大規模な計算リソースを使用して深層ニューラルネットワークを訓練しました。有名な猫認識実験は、ニューラルネットワークが明示的なプログラミングなしで概念を識別することを学習できることを示しました。",
        "badge.large-scale": "大規模機械学習",
        "badge.unsupervised": "教師なし学習",

        "event17.title": "AlexNetの勝利",
        "event17.pioneer": "アレックス・クリジェフスキー、ジェフリー・ヒントンとイリヤ・サツケヴァー（カナダ）",
        "event17.description": "AlexNetは記録的な15.3%のエラー率でImageNetコンペティションに勝利し、以前の手法を圧倒しました。この決定的な勝利は深層学習革命に火をつけ、GPU訓練ニューラルネットワークの力を証明しました。",
        "badge.breakthrough": "深層学習のブレークスルー",

        // Era 4: Modern AI (2012-2020)
        "era4.badge": "2012 - 2020",
        "era4.title": "現代AIの時代",
        "era4.description": "深層学習が主流となり、ゲーム、視覚、言語タスクで超人的なパフォーマンスを達成し、新しいAI企業がこれらのブレークスルーを商業化するために登場しました。",

        "event18.title": "敵対的生成ネットワーク",
        "event18.pioneer": "イアン・グッドフェロー（アメリカ）",
        "event18.description": "2つのニューラルネットワークが競い合う革命的なアーキテクチャであるGANを発明しました：1つは偽データを生成し、もう1つはそれを検出しようとします。GANは前例のないリアリズムで画像生成を可能にしました。",
        "badge.generative": "生成AI",
        "badge.image-gen": "画像生成",

        "event19.title": "OpenAI設立",
        "event19.pioneer": "イーロン・マスク、サム・アルトマン、イリヤ・サツケヴァーほか（アメリカ）",
        "event19.description": "10億ドルのコミットメントを持つ非営利AI研究会社として設立され、AGIがすべての人類に利益をもたらすことを保証することを目指しました。OpenAIは後にGPTとChatGPTを作成します。",
        "badge.safety": "AI安全性",
        "badge.research-lab": "研究所",

        "event20.title": "AlphaGoがイ・セドルを破る",
        "event20.pioneer": "デミス・ハサビスとDeepMindチーム（イギリス）",
        "event20.description": "AlphaGoは世界チャンピオンのイ・セドルを4-1で破りました。囲碁は宇宙の原子よりも多くの可能な位置を持つゲームです。この驚異的な達成は、AIが直感的で創造的なタスクをマスターする能力を示しました。",
        "badge.reinforcement": "強化学習",

        "event21.title": "深層学習チューリング賞",
        "event21.pioneer": "ジェフリー・ヒントン（カナダ）、ヨシュア・ベンジオ（カナダ）とヤン・ルカン（フランス）",
        "event21.description": "AIのゴッドファーザーたちは、深層ニューラルネットワークをコンピューティングの重要な構成要素にした概念的および工学的なブレークスルーによりチューリング賞を受賞しました。彼らの30年にわたる研究がついに認められました。",
        "badge.nobel-computing": "コンピューティングのノーベル賞",

        "event22.title": "AlphaFoldがタンパク質折り畳み問題を解決",
        "event22.pioneer": "デミス・ハサビスとDeepMindチーム（イギリス）",
        "event22.description": "AlphaFold2は50年来のタンパク質折り畳み問題を解決し、原子レベルの精度で3Dタンパク質構造を予測しました。このブレークスルーは創薬を加速し、ハサビスに2024年のノーベル化学賞をもたらしました。",
        "badge.biology": "計算生物学",
        "badge.discovery": "科学的発見",

        // Era 5: Generative AI (2017-Present)
        "era5.badge": "2017 - 現在",
        "era5.title": "生成AIの時代",
        "era5.description": "Transformerアーキテクチャと大規模言語モデルがAIに革命を起こし、数十億の人々がアクセスできるようになり、人間がテクノロジーと対話する方法を変革しました。",

        "event23.title": "注意機構がすべて",
        "event23.pioneer": "アシシュ・ヴァスワニとGoogle Brainチーム（アメリカ）",
        "event23.description": "Transformer論文を発表し、シーケンスを並列処理できる自己注意メカニズムを導入しました。このアーキテクチャはGPT、BERT、およびすべての現代的な大規模言語モデルの基礎となりました。",
        "badge.transformer": "Transformer",
        "badge.nlp": "NLP革命",

        "event24.title": "GPT-1：最初のGPT",
        "event24.pioneer": "アレック・ラドフォードとOpenAI（アメリカ）",
        "event24.description": "1億1700万パラメータを持つGPT-1をリリースし、言語モデルが教師なし事前学習を通じて一般的な言語理解を学習でき、多様なタスクで強力なパフォーマンスを達成できることを実証しました。",
        "badge.language": "言語モデル",
        "badge.transfer": "転移学習",

        "event25.title": "GPT-2はリリースするには危険すぎる",
        "event25.pioneer": "アレック・ラドフォードとOpenAI（アメリカ）",
        "event25.description": "GPT-2（15億パラメータ）は非常に一貫性のあるテキストを生成したため、OpenAIは当初、悪用の懸念を理由にリリースを拒否しました。これはAIの安全性と責任ある開示についての重要な議論を引き起こしました。",
        "badge.llm": "大規模言語モデル",
        "badge.ethics": "AI倫理",

        "event26.title": "Anthropic設立",
        "event26.pioneer": "ダリオ・アモデイとダニエラ・アモデイ（アメリカ）",
        "event26.description": "元OpenAI研究者がAnthropicを設立し、AI安全性と信頼性の高い解釈可能なAIシステムの構築に焦点を当てました。彼らの憲法的AIアプローチは、より制御可能で整合性のあるモデルを作成することを目指しています。",
        "badge.ethics-first": "倫理優先AI",

        "event27.title": "DALL-E画像生成",
        "event27.pioneer": "OpenAI研究チーム（アメリカ）",
        "event27.description": "DALL-Eはテキスト記述から創造的な画像を生成でき、前例のないクロスモーダル理解を実証しました。それはAIが真に創造的であり、新しい方法で概念を組み合わせることができることを示しました。",
        "badge.text-to-image": "テキストから画像へ",
        "badge.multimodal": "マルチモーダルAI",

        "event28.title": "Stable Diffusionオープンソース",
        "event28.pioneer": "エマド・モスタクとStability AI（イギリス）",
        "event28.description": "Stable Diffusionをオープンソースとしてリリースし、AI画像生成を民主化しました。クローズドな競合他社とは異なり、誰でもローカルで実行でき、創造的なAIアプリケーションの爆発的増加を引き起こしました。",
        "badge.open-source": "オープンソースAI",

        "event29.title": "ChatGPTローンチ",
        "event29.pioneer": "OpenAIとサム・アルトマン（アメリカ）",
        "event29.description": "ChatGPTは2022年11月30日に発売され、5日で100万ユーザー、2か月で1億ユーザーに達しました - 史上最速で成長した消費者アプリケーションです。それはAIを主流にし、世界を変えました。",
        "badge.consumer": "消費者AI",
        "badge.impact": "文化的影響",

        "event30.title": "GPT-4リリース",
        "event30.pioneer": "OpenAI研究チーム（アメリカ）",
        "event30.description": "GPT-4は多くの専門試験で人間レベルのパフォーマンスを実証し、司法試験で90パーセンタイルのスコアを獲得しました。テキストと画像の両方を処理するマルチモーダル機能を導入しました。",
        "badge.agi": "AGI進歩",

        "event31.title": "Claude 3ファミリー",
        "event31.pioneer": "Anthropic研究チーム（アメリカ）",
        "event31.description": "Claude 3（Opus、Sonnet、Haiku）をリリースし、Opusは多くのベンチマークでGPT-4を上回りました。Claudeは最先端のパフォーマンスを達成しながら、安全性、正直さ、有用性を重視しました。",
        "badge.constitutional": "憲法的AI",
        "badge.ethical": "倫理的AI",

        "event32.title": "Gemini Ultraと200万コンテキスト",
        "event32.pioneer": "Google DeepMind（イギリス/アメリカ）",
        "event32.description": "Googleは前例のない200万トークンのコンテキストウィンドウを持つGemini 1.5をリリースし、数時間のビデオや完全なコードベースを処理できます。Gemini UltraはすべてのベンチマークでGPT-4に匹敵しました。",
        "badge.long-context": "長コンテキスト",

        "event33.title": "DeepSeek-V3オープンソース",
        "event33.pioneer": "梁文鋒とDeepSeek（中国）",
        "event33.description": "中国のスタートアップDeepSeekはV3（6710億パラメータ）をオープンソースとしてリリースし、GPT-4と同等のパフォーマンスを発揮しながら、トレーニングコストはわずか550万ドルでした。これは最先端のAIが数十億ドルの予算を必要としないことを証明しました。",
        "badge.cost": "コスト効率",

        "event34.title": "GLM-4ブレークスルー",
        "event34.pioneer": "唐傑と智譜AI（中国）",
        "event34.description": "智譜AIのGLM-4はわずか90億パラメータで100万トークンのコンテキストウィンドウを実現し、優れた多言語機能を実証し、完全にオープンソースでありながら西洋のモデルと競争力のあるパフォーマンスを発揮しました。",
        "badge.multilingual": "多言語AI",

        // Awards Section
        "awards.title": "主要な認識と賞",
        "awards.description": "AIを変革した先駆者たちは、科学技術における最高の栄誉を授与されました。",
        "award1.title": "2018年チューリング賞",
        "award1.recipients": "ジェフリー・ヒントン、ヨシュア・ベンジオ、ヤン・ルカン",
        "award1.description": "深層ニューラルネットワークにおける概念的および工学的ブレークスルーによるコンピューティングのノーベル賞。",
        "award2.title": "2011年チューリング賞",
        "award2.recipients": "ジューディア・パール",
        "award2.description": "確率的および因果的推論を通じたAIへの根本的な貢献。",
        "award3.title": "2024年ノーベル化学賞",
        "award3.recipients": "デミス・ハサビス（DeepMind）",
        "award3.description": "AlphaFold2のタンパク質構造予測におけるブレークスルー。",
        "award4.title": "2022年IEEE栄誉メダル",
        "award4.recipients": "ヤン・ルカン",
        "award4.description": "深層学習と畳み込みニューラルネットワークへの先駆的貢献。",
        "award5.title": "2022年アストゥリアス皇太子賞",
        "award5.recipients": "デミス・ハサビス",
        "award5.description": "AIを通じた科学技術研究への卓越した貢献。",
        "award6.title": "TIME 100最も影響力のある人物",
        "award6.recipients": "サム・アルトマン（2023）、ダリオ・アモデイ（2024）",
        "award6.description": "生成AI革命をリードし、その未来を形作ったことで認められました。",

        // Footer
        "footer.description": "AIツールとテクノロジーの究極のガイド。最高のAIソリューションを発見、比較、マスターしましょう。",
        "footer.quick-links": "クイックリンク",
        "footer.resources": "リソース",
        "footer.follow": "フォローする",
        "footer.copyright": "© 2024 TechVernia。全著作権所有。"
    },

    ko: {
        // Navigation
        "nav.home": "홈",
        "nav.categories": "카테고리",
        "nav.guides": "가이드",
        "nav.compare": "비교",
        "nav.ai-history": "AI 역사",
        "nav.blog": "블로그",
        "nav.about": "소개",
        "nav.contact": "연락처",

        // Hero Section
        "hero.title": "인공지능의 역사",
        "hero.description": "1950년대의 선구적인 개척자들부터 오늘날의 획기적인 모델까지, AI 개발의 놀라운 여정을 탐험하세요. AI를 이론에서 현실로 변화시킨 뛰어난 정신과 획기적인 순간들을 발견하세요.",

        // Era 1: Founders (1950-1970)
        "era1.badge": "1950 - 1970",
        "era1.title": "창시자 시대",
        "era1.description": "학문 분야로서 AI의 탄생, 선구적인 컴퓨터 과학자들이 인공지능의 이론적, 실용적 기반을 다졌습니다.",

        // Events Era 1
        "event1.title": "튜링 테스트",
        "event1.pioneer": "앨런 튜링 (영국)",
        "event1.description": "'계산 기계와 지능'을 발표하여 기계 지능의 척도로 튜링 테스트를 도입했습니다. 이 획기적인 논문은 근본적인 질문을 제기했습니다: 기계가 생각할 수 있는가?",
        "badge.theoretical": "이론적 기초",
        "badge.philosophy": "AI 철학",

        "event2.title": "최초의 신경망",
        "event2.pioneer": "마빈 민스키 (미국)",
        "event2.description": "40개의 뉴런을 가진 최초의 인공 신경망 기계인 SNARC(확률적 신경 아날로그 강화 계산기)를 만들었습니다. 이 선구적인 작업은 기계가 경험으로부터 학습할 수 있음을 입증했습니다.",
        "badge.neural": "신경망",
        "badge.ml": "머신러닝",

        "event3.title": "로직 이론가 프로그램",
        "event3.pioneer": "앨런 뉴웰 & 허버트 사이먼 (미국)",
        "event3.description": "최초의 AI 프로그램으로 간주되는 로직 이론가를 개발했습니다. 러셀과 화이트헤드의 수학 원리에서 수학 정리를 증명할 수 있었으며, 때로는 원저자보다 더 우아한 증명을 찾아냈습니다.",
        "badge.symbolic": "기호 AI",
        "badge.reasoning": "자동 추론",

        "event4.title": "인공지능의 탄생",
        "event4.pioneer": "존 매카시 (미국)",
        "event4.description": "다트머스 회의를 조직하여 인공지능이라는 용어가 만들어졌습니다. 이 역사적인 여름 워크숍은 기계 지능을 탐구하기 위해 가장 뛰어난 두뇌들을 모았으며, AI를 공식적인 학문 분야로 확립했습니다.",
        "badge.dartmouth": "다트머스 회의",
        "badge.founding": "분야 창립",

        "event5.title": "LISP 프로그래밍 언어",
        "event5.pioneer": "존 매카시 (미국)",
        "event5.description": "오늘날에도 사용되는 두 번째로 오래된 고급 프로그래밍 언어인 LISP를 만들었습니다. LISP는 수십 년 동안 AI 연구의 지배적인 언어가 되었으며, 가비지 컬렉션과 트리 데이터 구조와 같은 혁명적인 개념을 도입했습니다.",
        "badge.programming": "프로그래밍 언어",
        "badge.symbolic-processing": "기호 처리",

        "event6.title": "퍼셉트론",
        "event6.pioneer": "프랭크 로젠블랫 (미국)",
        "event6.description": "패턴 인식을 위한 최초의 인공 신경망인 퍼셉트론을 발명했습니다. Mark I 퍼셉트론은 간단한 패턴을 분류하는 법을 배울 수 있었으며, 현대 딥러닝의 토대를 마련했습니다.",
        "badge.pattern": "패턴 인식",

        "event7.title": "MIT AI 연구소",
        "event7.pioneer": "마빈 민스키 & 존 매카시 (미국)",
        "event7.description": "세계 최고의 AI 연구 센터 중 하나가 된 MIT 인공지능 연구소를 공동 설립했습니다. 이 연구소는 컴퓨터 비전, 로봇 공학, 머신러닝 분야에서 획기적인 연구를 생산했습니다.",
        "badge.institution": "연구 기관",
        "badge.leadership": "학술적 리더십",

        // Era 2: Expert Systems (1970-1990)
        "era2.badge": "1970 - 1990",
        "era2.title": "전문가 시스템 시대",
        "era2.description": "AI가 이론 연구에서 실용적 응용으로 이동하여, 전문가 시스템이 의학, 화학, 비즈니스 분야의 실제 문제를 해결했습니다.",

        "event8.title": "DENDRAL - 최초의 전문가 시스템",
        "event8.pioneer": "에드워드 파이겐바움 (미국)",
        "event8.description": "유기 분자를 식별할 수 있는 최초의 전문가 시스템인 DENDRAL을 개발했습니다. 이 획기적인 프로젝트는 AI가 전문 분야에서 인간 전문가의 성능을 일치시키거나 초과할 수 있음을 입증했습니다.",
        "badge.expert": "전문가 시스템",
        "badge.chemistry": "화학 AI",

        "event9.title": "MYCIN 의료 진단",
        "event9.pioneer": "에드워드 파이겐바움 & 팀 (미국)",
        "event9.description": "세균 감염을 진단하고 항생제를 권장하는 전문가 시스템인 MYCIN을 만들었습니다. 인간 전문가의 65%에 비해 69%의 정확도를 달성하여 의료 분야에서 AI의 잠재력을 증명했습니다.",
        "badge.medical": "의료 AI",

        "event10.title": "역전파 혁명",
        "event10.pioneer": "제프리 힌튼 (캐나다), 데이비드 루멜하트 & 로널드 윌리엄스 (미국)",
        "event10.description": "역전파 알고리즘을 대중화하여 신경망이 효율적으로 기울기를 계산하여 복잡한 패턴을 학습할 수 있게 했습니다. 이 획기적인 발전은 수년간의 정체 후 신경망 연구를 활성화했습니다.",
        "badge.deep": "딥러닝",

        "event11.title": "베이지안 네트워크",
        "event11.pioneer": "주디아 펄 (미국)",
        "event11.description": "베이지안 네트워크로 확률적 추론에 혁명을 일으켜 불확실성을 표현하고 추론하는 프레임워크를 제공했습니다. 이 작업으로 그는 2011년 튜링상을 수상했습니다.",
        "badge.probabilistic": "확률적 AI",
        "badge.causal": "인과 추론",

        "event12.title": "합성곱 신경망",
        "event12.pioneer": "얀 르쿤 (프랑스)",
        "event12.description": "합성곱 신경망(CNN)을 개발하고 손글씨 숫자 인식에 성공적으로 적용했습니다. LeNet은 놀라운 정확도로 우편번호를 읽을 수 있었으며, 컴퓨터 비전을 개척했습니다.",
        "badge.vision": "컴퓨터 비전",
        "badge.cnn": "합성곱 네트워크",

        // Era 3: Deep Learning Renaissance (1997-2012)
        "era3.badge": "1997 - 2012",
        "era3.title": "딥러닝 르네상스",
        "era3.description": "신경망이 새로운 아키텍처와 향상된 계산 능력으로 놀라운 복귀를 했으며, AI 혁명의 무대를 마련했습니다.",

        "event13.title": "딥블루가 카스파로프를 격파",
        "event13.pioneer": "IBM 연구팀 (미국)",
        "event13.description": "IBM의 딥블루가 재임 중인 세계 체스 챔피언을 경기에서 격파한 최초의 컴퓨터가 되었습니다. 이 역사적인 승리는 기계가 복잡한 전략적 사고에서 인간을 능가할 수 있음을 입증했습니다.",
        "badge.game": "게임 AI",
        "badge.milestone": "이정표 달성",

        "event14.title": "LSTM 네트워크",
        "event14.pioneer": "세프 호크라이터 (오스트리아) & 위르겐 슈미트후버 (스위스)",
        "event14.description": "순환 신경망을 괴롭혔던 기울기 소실 문제를 해결한 장단기 메모리(LSTM) 네트워크를 발명했습니다. LSTM은 음성 인식과 언어 처리의 기초가 되었습니다.",
        "badge.rnn": "순환 네트워크",
        "badge.sequence": "시퀀스 학습",

        "event15.title": "ImageNet 데이터세트",
        "event15.pioneer": "페이페이 리 (중국/미국)",
        "event15.description": "20,000개 카테고리에 걸쳐 1,400만 개의 레이블이 지정된 이미지를 가진 대규모 데이터세트 ImageNet을 만들었습니다. 이 데이터세트는 컴퓨터 비전에서 딥러닝 혁명을 촉매한 벤치마크가 되었습니다.",
        "badge.dataset": "데이터세트 생성",

        "event16.title": "구글 브레인 프로젝트",
        "event16.pioneer": "앤드류 응 & 제프 딘 (미국)",
        "event16.description": "대규모 계산 자원을 사용하여 심층 신경망을 훈련하는 구글 브레인을 시작했습니다. 유명한 고양이 인식 실험은 신경망이 명시적인 프로그래밍 없이 개념을 식별하는 법을 배울 수 있음을 보여주었습니다.",
        "badge.large-scale": "대규모 머신러닝",
        "badge.unsupervised": "비지도 학습",

        "event17.title": "AlexNet의 승리",
        "event17.pioneer": "알렉스 크리체프스키, 제프리 힌튼 & 일리야 서츠케버 (캐나다)",
        "event17.description": "AlexNet이 기록적인 15.3%의 오류율로 ImageNet 대회에서 우승하여 이전 방법들을 압도했습니다. 이 결정적인 승리는 딥러닝 혁명에 불을 붙이고 GPU로 훈련된 신경망의 힘을 증명했습니다.",
        "badge.breakthrough": "딥러닝 돌파구",

        // Era 4: Modern AI (2012-2020)
        "era4.badge": "2012 - 2020",
        "era4.title": "현대 AI 시대",
        "era4.description": "딥러닝이 주류가 되어 게임, 비전, 언어 작업에서 초인적인 성능을 달성했으며, 새로운 AI 회사들이 이러한 혁신을 상업화하기 위해 등장했습니다.",

        "event18.title": "생성적 적대 신경망",
        "event18.pioneer": "이안 굿펠로 (미국)",
        "event18.description": "두 개의 신경망이 경쟁하는 혁명적인 아키텍처인 GAN을 발명했습니다: 하나는 가짜 데이터를 생성하고, 다른 하나는 이를 감지하려고 시도합니다. GAN은 전례 없는 사실성으로 이미지 생성을 가능하게 했습니다.",
        "badge.generative": "생성 AI",
        "badge.image-gen": "이미지 생성",

        "event19.title": "OpenAI 설립",
        "event19.pioneer": "일론 머스크, 샘 알트만, 일리야 서츠케버 외 (미국)",
        "event19.description": "10억 달러의 약속으로 비영리 AI 연구 회사로 설립되어 AGI가 모든 인류에게 이익을 주도록 하는 것을 목표로 했습니다. OpenAI는 나중에 GPT와 ChatGPT를 만들게 됩니다.",
        "badge.safety": "AI 안전",
        "badge.research-lab": "연구소",

        "event20.title": "AlphaGo가 이세돌을 격파",
        "event20.pioneer": "데미스 하사비스 & DeepMind 팀 (영국)",
        "event20.description": "AlphaGo가 세계 챔피언 이세돌을 4-1로 격파했습니다. 바둑은 우주의 원자보다 더 많은 가능한 위치를 가진 게임입니다. 이 놀라운 성취는 AI가 직관적이고 창의적인 작업을 마스터할 수 있는 능력을 보여주었습니다.",
        "badge.reinforcement": "강화 학습",

        "event21.title": "딥러닝 튜링상",
        "event21.pioneer": "제프리 힌튼 (캐나다), 요슈아 벤지오 (캐나다) & 얀 르쿤 (프랑스)",
        "event21.description": "AI의 대부들이 심층 신경망을 컴퓨팅의 중요한 구성 요소로 만든 개념적, 공학적 혁신으로 튜링상을 수상했습니다. 30년에 걸친 그들의 작업이 마침내 인정받았습니다.",
        "badge.nobel-computing": "컴퓨팅의 노벨상",

        "event22.title": "AlphaFold가 단백질 접힘 해결",
        "event22.pioneer": "데미스 하사비스 & DeepMind 팀 (영국)",
        "event22.description": "AlphaFold2가 50년 된 단백질 접힘 문제를 해결하고 원자 수준의 정확도로 3D 단백질 구조를 예측했습니다. 이 혁신은 신약 발견을 가속화했으며 하사비스에게 2024년 노벨 화학상을 안겨주었습니다.",
        "badge.biology": "계산 생물학",
        "badge.discovery": "과학적 발견",

        // Era 5: Generative AI (2017-Present)
        "era5.badge": "2017 - 현재",
        "era5.title": "생성 AI 시대",
        "era5.description": "트랜스포머 아키텍처와 대규모 언어 모델이 AI를 혁신하여 수십억 명이 접근할 수 있게 하고 인간이 기술과 상호 작용하는 방식을 변화시켰습니다.",

        "event23.title": "어텐션이 전부입니다",
        "event23.pioneer": "아시시 바스와니 & 구글 브레인 팀 (미국)",
        "event23.description": "시퀀스를 병렬로 처리할 수 있는 자기 주의 메커니즘을 도입한 트랜스포머 논문을 발표했습니다. 이 아키텍처는 GPT, BERT 및 모든 현대 대규모 언어 모델의 기초가 되었습니다.",
        "badge.transformer": "트랜스포머",
        "badge.nlp": "NLP 혁명",

        "event24.title": "GPT-1: 최초의 GPT",
        "event24.pioneer": "알렉 래드포드 & OpenAI (미국)",
        "event24.description": "1억 1,700만 개의 매개변수를 가진 GPT-1을 출시하여 언어 모델이 비지도 사전 훈련을 통해 일반적인 언어 이해를 학습하고 다양한 작업에서 강력한 성능을 달성할 수 있음을 입증했습니다.",
        "badge.language": "언어 모델",
        "badge.transfer": "전이 학습",

        "event25.title": "GPT-2는 출시하기에 너무 위험",
        "event25.pioneer": "알렉 래드포드 & OpenAI (미국)",
        "event25.description": "GPT-2(15억 매개변수)가 너무 일관된 텍스트를 생성하여 OpenAI가 처음에는 오용에 대한 우려를 이유로 출시를 거부했습니다. 이는 AI 안전과 책임 있는 공개에 대한 중요한 논쟁을 촉발했습니다.",
        "badge.llm": "대규모 언어 모델",
        "badge.ethics": "AI 윤리",

        "event26.title": "Anthropic 설립",
        "event26.pioneer": "다리오 아모데이 & 다니엘라 아모데이 (미국)",
        "event26.description": "전직 OpenAI 연구자들이 AI 안전과 신뢰할 수 있고 해석 가능한 AI 시스템 구축에 초점을 맞춘 Anthropic을 설립했습니다. 그들의 헌법적 AI 접근법은 더 제어 가능하고 정렬된 모델을 만드는 것을 목표로 합니다.",
        "badge.ethics-first": "윤리 우선 AI",

        "event27.title": "DALL-E 이미지 생성",
        "event27.pioneer": "OpenAI 연구팀 (미국)",
        "event27.description": "DALL-E는 텍스트 설명에서 창의적인 이미지를 생성할 수 있어 전례 없는 크로스 모달 이해를 보여주었습니다. AI가 진정으로 창의적일 수 있으며 새로운 방식으로 개념을 결합할 수 있음을 보여주었습니다.",
        "badge.text-to-image": "텍스트에서 이미지로",
        "badge.multimodal": "멀티모달 AI",

        "event28.title": "Stable Diffusion 오픈소스",
        "event28.pioneer": "에마드 모스타크 & Stability AI (영국)",
        "event28.description": "Stable Diffusion을 오픈소스로 출시하여 AI 이미지 생성을 민주화했습니다. 폐쇄된 경쟁사들과 달리, 누구나 로컬에서 실행할 수 있어 창의적인 AI 애플리케이션의 폭발적인 증가를 촉발했습니다.",
        "badge.open-source": "오픈소스 AI",

        "event29.title": "ChatGPT 출시",
        "event29.pioneer": "OpenAI & 샘 알트만 (미국)",
        "event29.description": "ChatGPT는 2022년 11월 30일에 출시되어 5일 만에 100만 사용자, 2개월 만에 1억 사용자에 도달했습니다 - 역사상 가장 빠르게 성장한 소비자 애플리케이션입니다. AI를 주류로 가져왔고 세상을 바꿨습니다.",
        "badge.consumer": "소비자 AI",
        "badge.impact": "문화적 영향",

        "event30.title": "GPT-4 출시",
        "event30.pioneer": "OpenAI 연구팀 (미국)",
        "event30.description": "GPT-4는 많은 전문 시험에서 인간 수준의 성능을 보여주었으며, 변호사 시험에서 90백분위수를 기록했습니다. 텍스트와 이미지를 모두 처리하는 멀티모달 기능을 도입했습니다.",
        "badge.agi": "AGI 진전",

        "event31.title": "Claude 3 패밀리",
        "event31.pioneer": "Anthropic 연구팀 (미국)",
        "event31.description": "Claude 3(Opus, Sonnet, Haiku)을 출시했으며, Opus는 많은 벤치마크에서 GPT-4를 능가했습니다. Claude는 최첨단 성능을 달성하면서 안전, 정직, 유용성을 강조했습니다.",
        "badge.constitutional": "헌법적 AI",
        "badge.ethical": "윤리적 AI",

        "event32.title": "Gemini Ultra & 200만 컨텍스트",
        "event32.pioneer": "구글 DeepMind (영국/미국)",
        "event32.description": "구글은 전례 없는 200만 토큰의 컨텍스트 창을 가진 Gemini 1.5를 출시하여 몇 시간의 비디오나 전체 코드베이스를 처리할 수 있습니다. Gemini Ultra는 모든 벤치마크에서 GPT-4와 일치했습니다.",
        "badge.long-context": "긴 컨텍스트",

        "event33.title": "DeepSeek-V3 오픈소스",
        "event33.pioneer": "량원펑 & DeepSeek (중국)",
        "event33.description": "중국 스타트업 DeepSeek는 V3(6,710억 매개변수)를 오픈소스로 출시하여 GPT-4와 동등한 성능을 보이면서 훈련 비용은 단지 550만 달러였습니다. 이는 최첨단 AI가 수십억 달러의 예산을 필요로 하지 않음을 증명했습니다.",
        "badge.cost": "비용 효율성",

        "event34.title": "GLM-4 돌파구",
        "event34.pioneer": "탕지에 & Zhipu AI (중국)",
        "event34.description": "Zhipu AI의 GLM-4는 단지 90억 매개변수로 100만 토큰의 컨텍스트 창을 달성하여 뛰어난 다국어 기능과 서구 모델과 경쟁력 있는 성능을 보여주면서 완전히 오픈소스입니다.",
        "badge.multilingual": "다국어 AI",

        // Awards Section
        "awards.title": "주요 인정 및 상",
        "awards.description": "AI를 변화시킨 선구자들은 과학과 기술 분야에서 최고의 영예를 받았습니다.",
        "award1.title": "2018년 튜링상",
        "award1.recipients": "제프리 힌튼, 요슈아 벤지오, 얀 르쿤",
        "award1.description": "심층 신경망의 개념적, 공학적 혁신으로 컴퓨팅의 노벨상 수상.",
        "award2.title": "2011년 튜링상",
        "award2.recipients": "주디아 펄",
        "award2.description": "확률적, 인과적 추론을 통한 AI에 대한 근본적인 기여.",
        "award3.title": "2024년 노벨 화학상",
        "award3.recipients": "데미스 하사비스 (DeepMind)",
        "award3.description": "AlphaFold2의 단백질 구조 예측 혁신.",
        "award4.title": "2022년 IEEE 명예 메달",
        "award4.recipients": "얀 르쿤",
        "award4.description": "딥러닝과 합성곱 신경망에 대한 선구적 기여.",
        "award5.title": "2022년 아스투리아스 공주상",
        "award5.recipients": "데미스 하사비스",
        "award5.description": "AI를 통한 과학 및 기술 연구에 대한 뛰어난 기여.",
        "award6.title": "TIME 100 가장 영향력 있는 인물",
        "award6.recipients": "샘 알트만 (2023), 다리오 아모데이 (2024)",
        "award6.description": "생성 AI 혁명을 이끌고 미래를 형성한 것으로 인정받았습니다.",

        // Footer
        "footer.description": "AI 도구 및 기술에 대한 궁극적인 가이드. 최고의 AI 솔루션을 발견하고, 비교하고, 마스터하세요.",
        "footer.quick-links": "빠른 링크",
        "footer.resources": "리소스",
        "footer.follow": "팔로우하기",
        "footer.copyright": "© 2024 TechVernia. 모든 권리 보유."
    },

    ar: {
        // Navigation
        "nav.home": "الرئيسية",
        "nav.categories": "الفئات",
        "nav.guides": "الأدلة",
        "nav.compare": "قارن",
        "nav.ai-history": "تاريخ الذكاء الاصطناعي",
        "nav.blog": "المدونة",
        "nav.about": "حول",
        "nav.contact": "اتصل",

        // Hero Section
        "hero.title": "تاريخ الذكاء الاصطناعي",
        "hero.description": "من الرواد ذوي الرؤية في الخمسينيات إلى النماذج الرائدة اليوم، استكشف الرحلة الرائعة لتطوير الذكاء الاصطناعي. اكتشف العقول البارعة واللحظات الثورية التي حولت الذكاء الاصطناعي من النظرية إلى الواقع.",

        // Era 1: Founders (1950-1970)
        "era1.badge": "1950 - 1970",
        "era1.title": "عصر المؤسسين",
        "era1.description": "ولادة الذكاء الاصطناعي كتخصص أكاديمي، حيث وضع علماء الحاسوب الرواد الأسس النظرية والعملية للذكاء الاصطناعي.",

        // Events Era 1
        "event1.title": "اختبار تورينج",
        "event1.pioneer": "آلان تورينج (المملكة المتحدة)",
        "event1.description": "نشر 'آلة الحوسبة والذكاء'، مقدماً اختبار تورينج كمقياس لذكاء الآلة. طرح هذا البحث الرائد السؤال الأساسي: هل يمكن للآلات أن تفكر؟",
        "badge.theoretical": "الأساس النظري",
        "badge.philosophy": "فلسفة الذكاء الاصطناعي",

        "event2.title": "أول شبكة عصبية",
        "event2.pioneer": "مارفن مينسكي (الولايات المتحدة)",
        "event2.description": "أنشأ SNARC (حاسبة التعزيز التناظرية العصبية العشوائية)، أول آلة شبكة عصبية اصطناعية مع 40 عصبوناً. أظهر هذا العمل الرائد أن الآلات يمكنها التعلم من التجربة.",
        "badge.neural": "الشبكات العصبية",
        "badge.ml": "التعلم الآلي",

        "event3.title": "برنامج منظّر المنطق",
        "event3.pioneer": "آلن نيويل وهربرت سايمون (الولايات المتحدة)",
        "event3.description": "طوّرا منظّر المنطق، الذي يُعتبر أول برنامج ذكاء اصطناعي. كان يمكنه إثبات النظريات الرياضية من كتاب مبادئ الرياضيات لراسل وويتهيد، وأحياناً يجد براهين أكثر أناقة من المؤلفين الأصليين.",
        "badge.symbolic": "الذكاء الاصطناعي الرمزي",
        "badge.reasoning": "الاستدلال الآلي",

        "event4.title": "ولادة الذكاء الاصطناعي",
        "event4.pioneer": "جون مكارثي (الولايات المتحدة)",
        "event4.description": "نظّم مؤتمر دارتموث، حيث صِيغ مصطلح الذكاء الاصطناعي. جمعت ورشة العمل الصيفية التاريخية هذه ألمع العقول لاستكشاف ذكاء الآلة، مؤسسةً الذكاء الاصطناعي كمجال أكاديمي رسمي.",
        "badge.dartmouth": "مؤتمر دارتموث",
        "badge.founding": "تأسيس المجال",

        "event5.title": "لغة برمجة LISP",
        "event5.pioneer": "جون مكارثي (الولايات المتحدة)",
        "event5.description": "أنشأ LISP، ثاني أقدم لغة برمجة عالية المستوى لا تزال مستخدمة حتى اليوم. أصبحت LISP اللغة المهيمنة لبحوث الذكاء الاصطناعي لعقود، مقدمةً مفاهيم ثورية مثل جمع القمامة وهياكل بيانات الأشجار.",
        "badge.programming": "لغة البرمجة",
        "badge.symbolic-processing": "المعالجة الرمزية",

        "event6.title": "البيرسيبترون",
        "event6.pioneer": "فرانك روزنبلات (الولايات المتحدة)",
        "event6.description": "اخترع البيرسيبترون، أول شبكة عصبية اصطناعية للتعرف على الأنماط. كان بيرسيبترون Mark I يمكنه تعلم تصنيف الأنماط البسيطة، واضعاً الأساس للتعلم العميق الحديث.",
        "badge.pattern": "التعرف على الأنماط",

        "event7.title": "مختبر الذكاء الاصطناعي في MIT",
        "event7.pioneer": "مارفن مينسكي وجون مكارثي (الولايات المتحدة)",
        "event7.description": "شاركا في تأسيس مختبر الذكاء الاصطناعي في معهد ماساتشوستس للتكنولوجيا، الذي أصبح أحد المراكز البحثية الرائدة في مجال الذكاء الاصطناعي في العالم. أنتج المختبر أعمالاً رائدة في رؤية الحاسوب والروبوتات والتعلم الآلي.",
        "badge.institution": "مؤسسة بحثية",
        "badge.leadership": "القيادة الأكاديمية",

        // Era 2: Expert Systems (1970-1990)
        "era2.badge": "1970 - 1990",
        "era2.title": "عصر الأنظمة الخبيرة",
        "era2.description": "انتقل الذكاء الاصطناعي من البحث النظري إلى التطبيقات العملية، مع أنظمة خبيرة تحل مشاكل العالم الحقيقي في الطب والكيمياء والأعمال.",

        "event8.title": "DENDRAL - أول نظام خبير",
        "event8.pioneer": "إدوارد فايجنباوم (الولايات المتحدة)",
        "event8.description": "طوّر DENDRAL، أول نظام خبير قادر على تحديد الجزيئات العضوية. أظهر هذا المشروع الرائد أن الذكاء الاصطناعي يمكن أن يضاهي أو يتفوق على أداء الخبراء البشريين في المجالات المتخصصة.",
        "badge.expert": "الأنظمة الخبيرة",
        "badge.chemistry": "ذكاء اصطناعي كيميائي",

        "event9.title": "تشخيص MYCIN الطبي",
        "event9.pioneer": "إدوارد فايجنباوم والفريق (الولايات المتحدة)",
        "event9.description": "أنشأ MYCIN، نظام خبير لتشخيص الالتهابات البكتيرية والتوصية بالمضادات الحيوية. حقق دقة 69٪ مقارنة بـ 65٪ للخبراء البشريين، مثبتاً إمكانات الذكاء الاصطناعي في الرعاية الصحية.",
        "badge.medical": "الذكاء الاصطناعي الطبي",

        "event10.title": "ثورة الانتشار العكسي",
        "event10.pioneer": "جيفري هينتون (كندا)، ديفيد روميلهارت ورونالد ويليامز (الولايات المتحدة)",
        "event10.description": "شاع خوارزمية الانتشار العكسي، ممكّناً الشبكات العصبية من تعلم الأنماط المعقدة من خلال حساب التدرجات بكفاءة. أحيت هذه الطفرة أبحاث الشبكات العصبية بعد سنوات من الركود.",
        "badge.deep": "التعلم العميق",

        "event11.title": "الشبكات البايزية",
        "event11.pioneer": "جوديا بيرل (الولايات المتحدة)",
        "event11.description": "أحدث ثورة في الاستدلال الاحتمالي بالشبكات البايزية، موفراً إطاراً لتمثيل والاستدلال حول عدم اليقين. نال هذا العمل جائزة تورينج 2011.",
        "badge.probabilistic": "الذكاء الاصطناعي الاحتمالي",
        "badge.causal": "الاستدلال السببي",

        "event12.title": "الشبكات العصبية الالتفافية",
        "event12.pioneer": "يان لوكون (فرنسا)",
        "event12.description": "طوّر الشبكات العصبية الالتفافية (CNN) وطبقها بنجاح على التعرف على الأرقام المكتوبة بخط اليد. استطاع LeNet قراءة الرموز البريدية بدقة استثنائية، رائداً في رؤية الحاسوب.",
        "badge.vision": "رؤية الحاسوب",
        "badge.cnn": "الشبكات الالتفافية",

        // Era 3: Deep Learning Renaissance (1997-2012)
        "era3.badge": "1997 - 2012",
        "era3.title": "نهضة التعلم العميق",
        "era3.description": "عادت الشبكات العصبية بشكل مذهل مع معماريات جديدة وقوة حوسبة محسّنة، ممهدةً الطريق لثورة الذكاء الاصطناعي.",

        "event13.title": "ديب بلو يهزم كاسباروف",
        "event13.pioneer": "فريق أبحاث IBM (الولايات المتحدة)",
        "event13.description": "أصبح ديب بلو من IBM أول حاسوب يهزم بطل العالم الحالي للشطرنج في مباراة. أظهر هذا الانتصار التاريخي أن الآلات يمكنها تجاوز البشر في التفكير الاستراتيجي المعقد.",
        "badge.game": "ذكاء اصطناعي للألعاب",
        "badge.milestone": "إنجاز بارز",

        "event14.title": "شبكات LSTM",
        "event14.pioneer": "سيب هوكريتر (النمسا) ويورغن شميدهوبر (سويسرا)",
        "event14.description": "اخترع شبكات الذاكرة طويلة قصيرة الأمد (LSTM)، حالاً مشكلة اختفاء التدرج التي ابتليت بها الشبكات العصبية المتكررة. أصبحت LSTM أساسية للتعرف على الكلام ومعالجة اللغة.",
        "badge.rnn": "الشبكات المتكررة",
        "badge.sequence": "تعلم التسلسل",

        "event15.title": "مجموعة بيانات ImageNet",
        "event15.pioneer": "فاي فاي لي (الصين/الولايات المتحدة)",
        "event15.description": "أنشأت ImageNet، مجموعة بيانات ضخمة تضم 14 مليون صورة موسومة عبر 20,000 فئة. أصبحت مجموعة البيانات هذه المعيار الذي حفز ثورة التعلم العميق في رؤية الحاسوب.",
        "badge.dataset": "إنشاء مجموعة البيانات",

        "event16.title": "مشروع جوجل برين",
        "event16.pioneer": "أندرو نج وجيف دين (الولايات المتحدة)",
        "event16.description": "أطلق جوجل برين، مستخدماً موارد حوسبة هائلة لتدريب الشبكات العصبية العميقة. أظهرت تجربة التعرف على القطط الشهيرة أن الشبكات العصبية يمكنها تعلم تحديد المفاهيم دون برمجة صريحة.",
        "badge.large-scale": "تعلم آلي واسع النطاق",
        "badge.unsupervised": "التعلم غير الموجّه",

        "event17.title": "انتصار AlexNet",
        "event17.pioneer": "أليكس كريجيفسكي، جيفري هينتون وإيليا سوتسكيفر (كندا)",
        "event17.description": "فاز AlexNet في مسابقة ImageNet بمعدل خطأ قياسي 15.3٪، ساحقاً الطرق السابقة. أشعل هذا الانتصار الحاسم ثورة التعلم العميق، مثبتاً قوة الشبكات العصبية المدربة على GPU.",
        "badge.breakthrough": "اختراق في التعلم العميق",

        // Era 4: Modern AI (2012-2020)
        "era4.badge": "2012 - 2020",
        "era4.title": "عصر الذكاء الاصطناعي الحديث",
        "era4.description": "أصبح التعلم العميق سائداً، محققاً أداءً خارقاً في الألعاب والرؤية ومهام اللغة، بينما ظهرت شركات ذكاء اصطناعي جديدة لتسويق هذه الاختراقات.",

        "event18.title": "الشبكات التوليدية التنافسية",
        "event18.pioneer": "إيان جودفيلو (الولايات المتحدة)",
        "event18.description": "اخترع GANs، معمارية ثورية حيث تتنافس شبكتان عصبيتان: واحدة تولد بيانات مزيفة، والأخرى تحاول اكتشافها. مكّنت GANs توليد صور بواقعية غير مسبوقة.",
        "badge.generative": "الذكاء الاصطناعي التوليدي",
        "badge.image-gen": "توليد الصور",

        "event19.title": "تأسيس OpenAI",
        "event19.pioneer": "إيلون ماسك، سام ألتمان، إيليا سوتسكيفر وآخرون (الولايات المتحدة)",
        "event19.description": "تأسست كشركة أبحاث ذكاء اصطناعي غير ربحية بالتزامات بقيمة مليار دولار، تهدف لضمان أن الذكاء الاصطناعي العام يفيد البشرية جمعاء. ستنشئ OpenAI لاحقاً GPT و ChatGPT.",
        "badge.safety": "سلامة الذكاء الاصطناعي",
        "badge.research-lab": "مختبر أبحاث",

        "event20.title": "AlphaGo يهزم لي سيدول",
        "event20.pioneer": "ديميس هاسابيس وفريق DeepMind (المملكة المتحدة)",
        "event20.description": "هزم AlphaGo البطل العالمي لي سيدول 4-1 في لعبة جو، لعبة ذات مواضع محتملة أكثر من ذرات الكون. أظهر هذا الإنجاز المذهل قدرة الذكاء الاصطناعي على إتقان المهام الحدسية والإبداعية.",
        "badge.reinforcement": "التعلم المعزز",

        "event21.title": "جائزة تورينج للتعلم العميق",
        "event21.pioneer": "جيفري هينتون (كندا)، يوشوا بينجيو (كندا) ويان لوكون (فرنسا)",
        "event21.description": "حصل آباء الذكاء الاصطناعي على جائزة تورينج للاختراقات المفاهيمية والهندسية التي جعلت الشبكات العصبية العميقة مكوناً حاسماً في الحوسبة. حظي عملهم الممتد لثلاثة عقود أخيراً بالتقدير.",
        "badge.nobel-computing": "نوبل الحوسبة",

        "event22.title": "AlphaFold يحل طي البروتين",
        "event22.pioneer": "ديميس هاسابيس وفريق DeepMind (المملكة المتحدة)",
        "event22.description": "حل AlphaFold2 مشكلة طي البروتين البالغة من العمر 50 عاماً، متنبئاً ببنى البروتين ثلاثية الأبعاد بدقة على المستوى الذري. عجّل هذا الاختراق اكتشاف الأدوية وأكسب هاسابيس جائزة نوبل في الكيمياء (2024).",
        "badge.biology": "البيولوجيا الحاسوبية",
        "badge.discovery": "الاكتشاف العلمي",

        // Era 5: Generative AI (2017-Present)
        "era5.badge": "2017 - الحاضر",
        "era5.title": "عصر الذكاء الاصطناعي التوليدي",
        "era5.description": "أحدثت معمارية المحوّل ونماذج اللغة الكبيرة ثورة في الذكاء الاصطناعي، جاعلةً إياه متاحاً لمليارات البشر وم transformando كيفية تفاعل البشر مع التكنولوجيا.",

        "event23.title": "الانتباه هو كل ما تحتاجه",
        "event23.pioneer": "أشيش فاسواني وفريق جوجل برين (الولايات المتحدة)",
        "event23.description": "نشر ورقة المحوّل، مقدماً آلية الانتباه الذاتي التي يمكنها معالجة التسلسلات بالتوازي. أصبحت هذه المعمارية أساس GPT و BERT وجميع نماذج اللغة الكبيرة الحديثة.",
        "badge.transformer": "المحوّل",
        "badge.nlp": "ثورة معالجة اللغة الطبيعية",

        "event24.title": "GPT-1: أول GPT",
        "event24.pioneer": "أليك رادفورد و OpenAI (الولايات المتحدة)",
        "event24.description": "أطلق GPT-1 بـ 117 مليون معامل، مظهراً أن نماذج اللغة يمكنها تعلم الفهم العام للغة من خلال التدريب المسبق غير الموجّه وتحقيق أداء قوي عبر مهام متنوعة.",
        "badge.language": "نماذج اللغة",
        "badge.transfer": "التعلم بالنقل",

        "event25.title": "GPT-2 خطير جداً للإصدار",
        "event25.pioneer": "أليك رادفورد و OpenAI (الولايات المتحدة)",
        "event25.description": "ولّد GPT-2 (1.5 مليار معامل) نصاً متماسكاً لدرجة أن OpenAI رفضت في البداية إطلاقه، مستشهدةً بمخاوف إساءة الاستخدام. أثار هذا نقاشات مهمة حول سلامة الذكاء الاصطناعي والإفصاح المسؤول.",
        "badge.llm": "نماذج اللغة الكبيرة",
        "badge.ethics": "أخلاقيات الذكاء الاصطناعي",

        "event26.title": "تأسيس Anthropic",
        "event26.pioneer": "داريو أموديي ودانييلا أموديي (الولايات المتحدة)",
        "event26.description": "أسس باحثون سابقون في OpenAI شركة Anthropic، مركزين على سلامة الذكاء الاصطناعي وبناء أنظمة ذكاء اصطناعي موثوقة وقابلة للتفسير. يهدف نهجهم للذكاء الاصطناعي الدستوري إلى إنشاء نماذج أكثر قابلية للتحكم ومحاذاة.",
        "badge.ethics-first": "الذكاء الاصطناعي الأخلاقي أولاً",

        "event27.title": "توليد صور DALL-E",
        "event27.pioneer": "فريق أبحاث OpenAI (الولايات المتحدة)",
        "event27.description": "استطاع DALL-E توليد صور إبداعية من أوصاف نصية، مظهراً فهماً عبر الوسائط غير مسبوق. أظهر أن الذكاء الاصطناعي يمكن أن يكون إبداعياً حقاً، جامعاً المفاهيم بطرق جديدة.",
        "badge.text-to-image": "من النص إلى الصورة",
        "badge.multimodal": "الذكاء الاصطناعي متعدد الوسائط",

        "event28.title": "Stable Diffusion مفتوح المصدر",
        "event28.pioneer": "عماد مصطقى و Stability AI (المملكة المتحدة)",
        "event28.description": "أطلق Stable Diffusion كمصدر مفتوح، ديمقراطياً توليد الصور بالذكاء الاصطناعي. على عكس المنافسين المغلقين، يمكن لأي شخص تشغيله محلياً، مشعلاً انفجاراً في تطبيقات الذكاء الاصطناعي الإبداعية.",
        "badge.open-source": "الذكاء الاصطناعي مفتوح المصدر",

        "event29.title": "إطلاق ChatGPT",
        "event29.pioneer": "OpenAI وسام ألتمان (الولايات المتحدة)",
        "event29.description": "أُطلق ChatGPT في 30 نوفمبر 2022، محققاً مليون مستخدم في 5 أيام و100 مليون في شهرين - التطبيق الاستهلاكي الأسرع نمواً في التاريخ. جلب الذكاء الاصطناعي إلى السائد وغيّر العالم.",
        "badge.consumer": "الذكاء الاصطناعي الاستهلاكي",
        "badge.impact": "التأثير الثقافي",

        "event30.title": "إصدار GPT-4",
        "event30.pioneer": "فريق أبحاث OpenAI (الولايات المتحدة)",
        "event30.description": "أظهر GPT-4 أداءً على مستوى البشر في العديد من الامتحانات المهنية، بما في ذلك الحصول على المئين التسعين في امتحان المحاماة. قدّم قدرات متعددة الوسائط، معالجاً النص والصور معاً.",
        "badge.agi": "تقدم نحو الذكاء الاصطناعي العام",

        "event31.title": "عائلة Claude 3",
        "event31.pioneer": "فريق أبحاث Anthropic (الولايات المتحدة)",
        "event31.description": "أطلق Claude 3 (Opus، Sonnet، Haiku)، مع تفوق Opus على GPT-4 في العديد من المعايير. ركز Claude على السلامة والصدق والفائدة مع تحقيق أداء حديث.",
        "badge.constitutional": "الذكاء الاصطناعي الدستوري",
        "badge.ethical": "الذكاء الاصطناعي الأخلاقي",

        "event32.title": "Gemini Ultra وسياق 2 مليون",
        "event32.pioneer": "جوجل DeepMind (المملكة المتحدة/الولايات المتحدة)",
        "event32.description": "أطلقت جوجل Gemini 1.5 بنافذة سياق غير مسبوقة تبلغ 2 مليون رمز، قادرة على معالجة ساعات من الفيديو أو قواعد أكواد كاملة. طابق Gemini Ultra GPT-4 عبر جميع المعايير.",
        "badge.long-context": "السياق الطويل",

        "event33.title": "DeepSeek-V3 مفتوح المصدر",
        "event33.pioneer": "ليانج وينفنغ و DeepSeek (الصين)",
        "event33.description": "أطلقت الشركة الناشئة الصينية DeepSeek نموذج V3 (671 مليار معامل) كمصدر مفتوح، مطابقاً GPT-4 في الأداء بينما تكلف تدريبه 5.5 مليون دولار فقط. أثبت هذا أن الذكاء الاصطناعي المتطور لا يتطلب ميزانيات بالمليارات.",
        "badge.cost": "كفاءة التكلفة",

        "event34.title": "اختراق GLM-4",
        "event34.pioneer": "تانغ جيه و Zhipu AI (الصين)",
        "event34.description": "حقق GLM-4 من Zhipu AI نافذة سياق بمليون رمز بـ 9 مليارات معامل فقط، مظهراً قدرات متعددة اللغات استثنائية وأداء تنافسي مع النماذج الغربية مع كونه مفتوح المصدر بالكامل.",
        "badge.multilingual": "الذكاء الاصطناعي متعدد اللغات",

        // Awards Section
        "awards.title": "الاعترافات والجوائز الرئيسية",
        "awards.description": "كُرّم الرواد الذين حوّلوا الذكاء الاصطناعي بأعلى الأوسمة في العلوم والتكنولوجيا.",
        "award1.title": "جائزة تورينج 2018",
        "award1.recipients": "جيفري هينتون، يوشوا بينجيو، يان لوكون",
        "award1.description": "جائزة نوبل الحوسبة للاختراقات المفاهيمية والهندسية في الشبكات العصبية العميقة.",
        "award2.title": "جائزة تورينج 2011",
        "award2.recipients": "جوديا بيرل",
        "award2.description": "للمساهمات الأساسية في الذكاء الاصطناعي من خلال الاستدلال الاحتمالي والسببي.",
        "award3.title": "جائزة نوبل في الكيمياء 2024",
        "award3.recipients": "ديميس هاسابيس (DeepMind)",
        "award3.description": "لاختراق AlphaFold2 في التنبؤ ببنية البروتين.",
        "award4.title": "ميدالية IEEE الشرفية 2022",
        "award4.recipients": "يان لوكون",
        "award4.description": "للمساهمات الرائدة في التعلم العميق والشبكات العصبية الالتفافية.",
        "award5.title": "جائزة أميرة أستورياس 2022",
        "award5.recipients": "ديميس هاسابيس",
        "award5.description": "للمساهمات المتميزة في البحث العلمي والتقني من خلال الذكاء الاصطناعي.",
        "award6.title": "TIME 100 الأكثر تأثيراً",
        "award6.recipients": "سام ألتمان (2023)، داريو أموديي (2024)",
        "award6.description": "تم تكريمهم لقيادة ثورة الذكاء الاصطناعي التوليدي وتشكيل مستقبله.",

        // Footer
        "footer.description": "دليلك النهائي لأدوات وتقنيات الذكاء الاصطناعي. اكتشف، قارن، وأتقن أفضل حلول الذكاء الاصطناعي.",
        "footer.quick-links": "روابط سريعة",
        "footer.resources": "الموارد",
        "footer.follow": "تابعنا",
        "footer.copyright": "© 2024 TechVernia. جميع الحقوق محفوظة."
    },

    hi: {
        // Navigation
        "nav.home": "होम",
        "nav.categories": "श्रेणियाँ",
        "nav.guides": "गाइड",
        "nav.compare": "तुलना करें",
        "nav.ai-history": "AI इतिहास",
        "nav.blog": "ब्लॉग",
        "nav.about": "के बारे में",
        "nav.contact": "संपर्क",

        // Hero Section
        "hero.title": "कृत्रिम बुद्धिमत्ता का इतिहास",
        "hero.description": "1950 के दशक के दूरदर्शी अग्रदूतों से लेकर आज के अभूतपूर्व मॉडलों तक, AI विकास की उल्लेखनीय यात्रा का अन्वेषण करें। उन शानदार दिमागों और क्रांतिकारी क्षणों की खोज करें जिन्होंने AI को सिद्धांत से वास्तविकता में बदल दिया।",

        // Era 1: Founders (1950-1970)
        "era1.badge": "1950 - 1970",
        "era1.title": "संस्थापकों का युग",
        "era1.description": "एक शैक्षणिक अनुशासन के रूप में AI का जन्म, जहाँ अग्रणी कंप्यूटर वैज्ञानिकों ने कृत्रिम बुद्धिमत्ता के लिए सैद्धांतिक और व्यावहारिक नींव रखी।",

        // Events Era 1
        "event1.title": "ट्यूरिंग परीक्षण",
        "event1.pioneer": "एलन ट्यूरिंग (यूनाइटेड किंगडम)",
        "event1.description": "'कम्प्यूटिंग मशीनरी और बुद्धिमत्ता' प्रकाशित की, मशीन बुद्धिमत्ता के माप के रूप में ट्यूरिंग परीक्षण को पेश किया। इस मौलिक पत्र ने मूलभूत प्रश्न उठाया: क्या मशीनें सोच सकती हैं?",
        "badge.theoretical": "सैद्धांतिक आधार",
        "badge.philosophy": "AI का दर्शन",

        "event2.title": "पहला न्यूरल नेटवर्क",
        "event2.pioneer": "मार्विन मिन्स्की (संयुक्त राज्य अमेरिका)",
        "event2.description": "SNARC (स्टोकास्टिक न्यूरल एनालॉग रीइन्फोर्समेंट कैलकुलेटर) बनाया, 40 न्यूरॉन्स वाली पहली कृत्रिम न्यूरल नेटवर्क मशीन। इस अग्रणी कार्य ने दिखाया कि मशीनें अनुभव से सीख सकती हैं।",
        "badge.neural": "न्यूरल नेटवर्क",
        "badge.ml": "मशीन लर्निंग",

        "event3.title": "लॉजिक थियोरिस्ट प्रोग्राम",
        "event3.pioneer": "एलन न्यूवेल और हर्बर्ट साइमन (संयुक्त राज्य अमेरिका)",
        "event3.description": "लॉजिक थियोरिस्ट विकसित किया, जिसे पहला AI प्रोग्राम माना जाता है। यह रसेल और व्हाइटहेड के प्रिंसिपिया मैथमेटिका से गणितीय प्रमेयों को सिद्ध कर सकता था, कभी-कभी मूल लेखकों से अधिक सुरुचिपूर्ण प्रमाण पाता था।",
        "badge.symbolic": "सिम्बॉलिक AI",
        "badge.reasoning": "स्वचालित तर्क",

        "event4.title": "कृत्रिम बुद्धिमत्ता का जन्म",
        "event4.pioneer": "जॉन मैकार्थी (संयुक्त राज्य अमेरिका)",
        "event4.description": "डार्टमाउथ सम्मेलन का आयोजन किया, जहाँ कृत्रिम बुद्धिमत्ता शब्द गढ़ा गया। इस ऐतिहासिक ग्रीष्मकालीन कार्यशाला ने मशीन बुद्धिमत्ता की खोज के लिए सबसे चमकीले दिमागों को एक साथ लाया, AI को एक औपचारिक शैक्षणिक क्षेत्र के रूप में स्थापित किया।",
        "badge.dartmouth": "डार्टमाउथ सम्मेलन",
        "badge.founding": "क्षेत्र की स्थापना",

        "event5.title": "LISP प्रोग्रामिंग भाषा",
        "event5.pioneer": "जॉन मैकार्थी (संयुक्त राज्य अमेरिका)",
        "event5.description": "LISP बनाया, दूसरी सबसे पुरानी उच्च-स्तरीय प्रोग्रामिंग भाषा जो आज भी उपयोग में है। LISP दशकों तक AI अनुसंधान के लिए प्रमुख भाषा बन गई, गार्बेज कलेक्शन और ट्री डेटा संरचनाओं जैसी क्रांतिकारी अवधारणाओं को पेश किया।",
        "badge.programming": "प्रोग्रामिंग भाषा",
        "badge.symbolic-processing": "सिम्बॉलिक प्रोसेसिंग",

        "event6.title": "परसेप्ट्रॉन",
        "event6.pioneer": "फ्रैंक रोसेनब्लैट (संयुक्त राज्य अमेरिका)",
        "event6.description": "पैटर्न पहचान के लिए पहला कृत्रिम न्यूरल नेटवर्क, परसेप्ट्रॉन का आविष्कार किया। Mark I परसेप्ट्रॉन सरल पैटर्न को वर्गीकृत करना सीख सकता था, आधुनिक डीप लर्निंग के लिए आधार तैयार किया।",
        "badge.pattern": "पैटर्न पहचान",

        "event7.title": "MIT AI प्रयोगशाला",
        "event7.pioneer": "मार्विन मिन्स्की और जॉन मैकार्थी (संयुक्त राज्य अमेरिका)",
        "event7.description": "MIT आर्टिफिशियल इंटेलिजेंस लेबोरेटरी की सह-स्थापना की, जो दुनिया के अग्रणी AI अनुसंधान केंद्रों में से एक बन गई। प्रयोगशाला ने कंप्यूटर विज़न, रोबोटिक्स और मशीन लर्निंग में अभूतपूर्व कार्य किया।",
        "badge.institution": "अनुसंधान संस्थान",
        "badge.leadership": "शैक्षणिक नेतृत्व",

        // Era 2: Expert Systems (1970-1990)
        "era2.badge": "1970 - 1990",
        "era2.title": "विशेषज्ञ प्रणाली युग",
        "era2.description": "AI सैद्धांतिक अनुसंधान से व्यावहारिक अनुप्रयोगों की ओर बढ़ा, विशेषज्ञ प्रणालियों के साथ चिकित्सा, रसायन विज्ञान और व्यवसाय में वास्तविक दुनिया की समस्याओं को हल किया।",

        "event8.title": "DENDRAL - पहली विशेषज्ञ प्रणाली",
        "event8.pioneer": "एडवर्ड फीगेनबाम (संयुक्त राज्य अमेरिका)",
        "event8.description": "DENDRAL विकसित किया, जैविक अणुओं की पहचान करने में सक्षम पहली विशेषज्ञ प्रणाली। इस अभूतपूर्व परियोजना ने प्रदर्शित किया कि AI विशेष क्षेत्रों में मानव विशेषज्ञ के प्रदर्शन को मिला या पार कर सकता है।",
        "badge.expert": "विशेषज्ञ प्रणालियाँ",
        "badge.chemistry": "रसायन विज्ञान AI",

        "event9.title": "MYCIN चिकित्सा निदान",
        "event9.pioneer": "एडवर्ड फीगेनबाम और टीम (संयुक्त राज्य अमेरिका)",
        "event9.description": "MYCIN बनाया, बैक्टीरियल संक्रमणों का निदान करने और एंटीबायोटिक्स की सिफारिश करने के लिए एक विशेषज्ञ प्रणाली। इसने मानव विशेषज्ञों के 65% की तुलना में 69% सटीकता हासिल की, स्वास्थ्य सेवा में AI की क्षमता को साबित किया।",
        "badge.medical": "चिकित्सा AI",

        "event10.title": "बैकप्रोपेगेशन क्रांति",
        "event10.pioneer": "जेफ्री हिंटन (कनाडा), डेविड रुमेलहार्ट और रोनाल्ड विलियम्स (संयुक्त राज्य अमेरिका)",
        "event10.description": "बैकप्रोपेगेशन एल्गोरिदम को लोकप्रिय बनाया, न्यूरल नेटवर्क को कुशलता से ग्रेडिएंट की गणना करके जटिल पैटर्न सीखने में सक्षम बनाया। इस सफलता ने वर्षों की स्थिरता के बाद न्यूरल नेटवर्क अनुसंधान को पुनर्जीवित किया।",
        "badge.deep": "डीप लर्निंग",

        "event11.title": "बेयेसियन नेटवर्क",
        "event11.pioneer": "जुडिया पर्ल (संयुक्त राज्य अमेरिका)",
        "event11.description": "बेयेसियन नेटवर्क के साथ संभाव्य तर्क में क्रांति ला दी, अनिश्चितता का प्रतिनिधित्व करने और तर्क करने के लिए एक ढांचा प्रदान किया। इस कार्य ने उन्हें 2011 का ट्यूरिंग पुरस्कार दिलाया।",
        "badge.probabilistic": "संभाव्य AI",
        "badge.causal": "कारण अनुमान",

        "event12.title": "कन्वोल्यूशनल न्यूरल नेटवर्क",
        "event12.pioneer": "यान लेकुन (फ्रांस)",
        "event12.description": "कन्वोल्यूशनल न्यूरल नेटवर्क (CNN) विकसित किया और उन्हें हस्तलिखित अंक पहचान पर सफलतापूर्वक लागू किया। LeNet असाधारण सटीकता के साथ ज़िप कोड पढ़ सकता था, कंप्यूटर विज़न में अग्रणी।",
        "badge.vision": "कंप्यूटर विज़न",
        "badge.cnn": "कन्वोल्यूशनल नेटवर्क",

        // Era 3: Deep Learning Renaissance (1997-2012)
        "era3.badge": "1997 - 2012",
        "era3.title": "डीप लर्निंग पुनर्जागरण",
        "era3.description": "न्यूरल नेटवर्क ने नई वास्तुकला और बढ़ी हुई कम्प्यूटेशनल शक्ति के साथ शानदार वापसी की, AI क्रांति के लिए मंच तैयार किया।",

        "event13.title": "डीप ब्लू ने कास्परोव को हराया",
        "event13.pioneer": "IBM अनुसंधान टीम (संयुक्त राज्य अमेरिका)",
        "event13.description": "IBM का डीप ब्लू एक मैच में शासक विश्व शतरंज चैंपियन को हराने वाला पहला कंप्यूटर बन गया। इस ऐतिहासिक जीत ने दिखाया कि मशीनें जटिल रणनीतिक सोच में मनुष्यों से आगे निकल सकती हैं।",
        "badge.game": "गेम AI",
        "badge.milestone": "मील का पत्थर उपलब्धि",

        "event14.title": "LSTM नेटवर्क",
        "event14.pioneer": "सेप होचराइटर (ऑस्ट्रिया) और जुर्गन श्मिडहुबर (स्विट्जरलैंड)",
        "event14.description": "लॉन्ग शॉर्ट-टर्म मेमोरी (LSTM) नेटवर्क का आविष्कार किया, वैनिशिंग ग्रेडिएंट समस्या को हल किया जो आवर्ती न्यूरल नेटवर्क को परेशान करती थी। LSTM भाषण पहचान और भाषा प्रसंस्करण के लिए मौलिक बन गए।",
        "badge.rnn": "आवर्ती नेटवर्क",
        "badge.sequence": "अनुक्रम शिक्षण",

        "event15.title": "ImageNet डेटासेट",
        "event15.pioneer": "फी-फी ली (चीन/संयुक्त राज्य अमेरिका)",
        "event15.description": "ImageNet बनाया, 20,000 श्रेणियों में 14 मिलियन लेबल वाली छवियों के साथ एक विशाल डेटासेट। यह डेटासेट बेंचमार्क बन गया जिसने कंप्यूटर विज़न में डीप लर्निंग क्रांति को उत्प्रेरित किया।",
        "badge.dataset": "डेटासेट निर्माण",

        "event16.title": "गूगल ब्रेन प्रोजेक्ट",
        "event16.pioneer": "एंड्रयू एनजी और जेफ डीन (संयुक्त राज्य अमेरिका)",
        "event16.description": "गूगल ब्रेन लॉन्च किया, गहरे न्यूरल नेटवर्क को प्रशिक्षित करने के लिए विशाल कम्प्यूटेशनल संसाधनों का उपयोग करते हुए। प्रसिद्ध बिल्ली पहचान प्रयोग ने दिखाया कि न्यूरल नेटवर्क स्पष्ट प्रोग्रामिंग के बिना अवधारणाओं की पहचान करना सीख सकते हैं।",
        "badge.large-scale": "बड़े पैमाने पर ML",
        "badge.unsupervised": "अनुपयोगी शिक्षण",

        "event17.title": "AlexNet की विजय",
        "event17.pioneer": "एलेक्स क्रिज़ेव्स्की, जेफ्री हिंटन और इल्या सुत्सकेवर (कनाडा)",
        "event17.description": "AlexNet ने रिकॉर्ड-ब्रेकिंग 15.3% त्रुटि दर के साथ ImageNet प्रतियोगिता जीती, पिछले तरीकों को कुचलते हुए। इस निर्णायक जीत ने डीप लर्निंग क्रांति को प्रज्वलित किया, GPU-प्रशिक्षित न्यूरल नेटवर्क की शक्ति को साबित किया।",
        "badge.breakthrough": "डीप लर्निंग सफलता",

        // Era 4: Modern AI (2012-2020)
        "era4.badge": "2012 - 2020",
        "era4.title": "आधुनिक AI युग",
        "era4.description": "डीप लर्निंग मुख्यधारा बन गई, खेलों, दृष्टि और भाषा कार्यों में अलौकिक प्रदर्शन प्राप्त करते हुए, जबकि नई AI कंपनियाँ इन सफलताओं को व्यावसायिक बनाने के लिए उभरीं।",

        "event18.title": "जनरेटिव एडवर्सरियल नेटवर्क",
        "event18.pioneer": "इयान गुडफेलो (संयुक्त राज्य अमेरिका)",
        "event18.description": "GANs का आविष्कार किया, एक क्रांतिकारी वास्तुकला जहाँ दो न्यूरल नेटवर्क प्रतिस्पर्धा करते हैं: एक नकली डेटा उत्पन्न करता है, दूसरा इसे पहचानने की कोशिश करता है। GANs ने अभूतपूर्व यथार्थवाद के साथ छवि निर्माण को सक्षम किया।",
        "badge.generative": "जनरेटिव AI",
        "badge.image-gen": "छवि निर्माण",

        "event19.title": "OpenAI की स्थापना",
        "event19.pioneer": "एलन मस्क, सैम अल्टमैन, इल्या सुत्सकेवर और अन्य (संयुक्त राज्य अमेरिका)",
        "event19.description": "$1 बिलियन की प्रतिबद्धताओं के साथ गैर-लाभकारी AI अनुसंधान कंपनी के रूप में स्थापित, यह सुनिश्चित करने का लक्ष्य रखते हुए कि AGI सभी मानवता को लाभ पहुँचाए। OpenAI बाद में GPT और ChatGPT बनाएगा।",
        "badge.safety": "AI सुरक्षा",
        "badge.research-lab": "अनुसंधान प्रयोगशाला",

        "event20.title": "AlphaGo ने ली सेडोल को हराया",
        "event20.pioneer": "डेमिस हासाबिस और DeepMind टीम (यूनाइटेड किंगडम)",
        "event20.description": "AlphaGo ने विश्व चैंपियन ली सेडोल को 4-1 से गो में हराया, एक ऐसा खेल जिसमें ब्रह्मांड में परमाणुओं से अधिक संभावित स्थितियाँ हैं। इस आश्चर्यजनक उपलब्धि ने AI की सहज, रचनात्मक कार्यों में महारत हासिल करने की क्षमता दिखाई।",
        "badge.reinforcement": "रीइन्फोर्समेंट लर्निंग",

        "event21.title": "डीप लर्निंग ट्यूरिंग पुरस्कार",
        "event21.pioneer": "जेफ्री हिंटन (कनाडा), योशुआ बेंगियो (कनाडा) और यान लेकुन (फ्रांस)",
        "event21.description": "AI के गॉडफादर्स को गहरे न्यूरल नेटवर्क को कंप्यूटिंग का एक महत्वपूर्ण घटक बनाने वाली वैचारिक और इंजीनियरिंग सफलताओं के लिए ट्यूरिंग पुरस्कार मिला। उनके तीन दशकों के काम को आखिरकार मान्यता मिली।",
        "badge.nobel-computing": "कंप्यूटिंग का नोबेल",

        "event22.title": "AlphaFold ने प्रोटीन फोल्डिंग हल किया",
        "event22.pioneer": "डेमिस हासाबिस और DeepMind टीम (यूनाइटेड किंगडम)",
        "event22.description": "AlphaFold2 ने 50 वर्षीय प्रोटीन फोल्डिंग समस्या को हल किया, परमाणु-स्तर की सटीकता के साथ 3D प्रोटीन संरचनाओं की भविष्यवाणी की। इस सफलता ने दवा खोज को गति दी और हासाबिस को 2024 में रसायन विज्ञान का नोबेल पुरस्कार दिलाया।",
        "badge.biology": "कम्प्यूटेशनल जीव विज्ञान",
        "badge.discovery": "वैज्ञानिक खोज",

        // Era 5: Generative AI (2017-Present)
        "era5.badge": "2017 - वर्तमान",
        "era5.title": "जनरेटिव AI युग",
        "era5.description": "ट्रांसफॉर्मर आर्किटेक्चर और बड़े भाषा मॉडल ने AI में क्रांति ला दी, इसे अरबों लोगों के लिए सुलभ बनाया और मनुष्यों के प्रौद्योगिकी के साथ बातचीत करने के तरीके को बदल दिया।",

        "event23.title": "अटेंशन ही आपको चाहिए",
        "event23.pioneer": "आशीष वस्वानी और गूगल ब्रेन टीम (संयुक्त राज्य अमेरिका)",
        "event23.description": "ट्रांसफॉर्मर पेपर प्रकाशित किया, सेल्फ-अटेंशन मैकेनिज्म पेश किया जो अनुक्रमों को समानांतर में संसाधित कर सकता था। यह आर्किटेक्चर GPT, BERT और सभी आधुनिक बड़े भाषा मॉडल का आधार बन गया।",
        "badge.transformer": "ट्रांसफॉर्मर",
        "badge.nlp": "NLP क्रांति",

        "event24.title": "GPT-1: पहला GPT",
        "event24.pioneer": "एलेक रैडफोर्ड और OpenAI (संयुक्त राज्य अमेरिका)",
        "event24.description": "117 मिलियन पैरामीटर के साथ GPT-1 जारी किया, प्रदर्शित किया कि भाषा मॉडल अनुपयोगी पूर्व-प्रशिक्षण के माध्यम से सामान्य भाषा समझ सीख सकते हैं और विविध कार्यों में मजबूत प्रदर्शन हासिल कर सकते हैं।",
        "badge.language": "भाषा मॉडल",
        "badge.transfer": "ट्रांसफर लर्निंग",

        "event25.title": "GPT-2 रिलीज़ के लिए बहुत खतरनाक",
        "event25.pioneer": "एलेक रैडफोर्ड और OpenAI (संयुक्त राज्य अमेरिका)",
        "event25.description": "GPT-2 (1.5 बिलियन पैरामीटर) ने इतना सुसंगत पाठ उत्पन्न किया कि OpenAI ने शुरू में दुरुपयोग की चिंताओं का हवाला देते हुए इसे जारी करने से इनकार कर दिया। इसने AI सुरक्षा और जिम्मेदार प्रकटीकरण के बारे में महत्वपूर्ण बहस को जन्म दिया।",
        "badge.llm": "बड़े भाषा मॉडल",
        "badge.ethics": "AI नैतिकता",

        "event26.title": "Anthropic की स्थापना",
        "event26.pioneer": "डारियो अमोडेई और डेनिएला अमोडेई (संयुक्त राज्य अमेरिका)",
        "event26.description": "पूर्व OpenAI शोधकर्ताओं ने Anthropic की स्थापना की, AI सुरक्षा और विश्वसनीय, व्याख्यायोग्य AI प्रणालियों के निर्माण पर ध्यान केंद्रित करते हुए। उनका संवैधानिक AI दृष्टिकोण अधिक नियंत्रणीय और संरेखित मॉडल बनाने का लक्ष्य रखता है।",
        "badge.ethics-first": "नैतिकता-प्रथम AI",

        "event27.title": "DALL-E छवि निर्माण",
        "event27.pioneer": "OpenAI अनुसंधान टीम (संयुक्त राज्य अमेरिका)",
        "event27.description": "DALL-E पाठ विवरण से रचनात्मक छवियाँ उत्पन्न कर सकता था, अभूतपूर्व क्रॉस-मोडल समझ का प्रदर्शन करते हुए। इसने दिखाया कि AI वास्तव में रचनात्मक हो सकता है, नए तरीकों से अवधारणाओं को मिलाते हुए।",
        "badge.text-to-image": "टेक्स्ट-टू-इमेज",
        "badge.multimodal": "मल्टीमॉडल AI",

        "event28.title": "Stable Diffusion ओपन सोर्स",
        "event28.pioneer": "एमैड मोस्टाक और Stability AI (यूनाइटेड किंगडम)",
        "event28.description": "Stable Diffusion को ओपन सोर्स के रूप में जारी किया, AI छवि निर्माण को लोकतांत्रिक बनाया। बंद प्रतिस्पर्धियों के विपरीत, कोई भी इसे स्थानीय रूप से चला सकता था, रचनात्मक AI अनुप्रयोगों में विस्फोट को जन्म दिया।",
        "badge.open-source": "ओपन सोर्स AI",

        "event29.title": "ChatGPT लॉन्च",
        "event29.pioneer": "OpenAI और सैम अल्टमैन (संयुक्त राज्य अमेरिका)",
        "event29.description": "ChatGPT 30 नवंबर 2022 को लॉन्च हुआ, 5 दिनों में 1 मिलियन उपयोगकर्ताओं और 2 महीनों में 100 मिलियन तक पहुँच गया - इतिहास में सबसे तेजी से बढ़ने वाला उपभोक्ता एप्लिकेशन। इसने AI को मुख्यधारा में लाया और दुनिया को बदल दिया।",
        "badge.consumer": "उपभोक्ता AI",
        "badge.impact": "सांस्कृतिक प्रभाव",

        "event30.title": "GPT-4 रिलीज़",
        "event30.pioneer": "OpenAI अनुसंधान टीम (संयुक्त राज्य अमेरिका)",
        "event30.description": "GPT-4 ने कई पेशेवर परीक्षाओं में मानव-स्तरीय प्रदर्शन प्रदर्शित किया, बार परीक्षा में 90वें प्रतिशतक में स्कोर करने सहित। इसने मल्टीमॉडल क्षमताओं को पेश किया, पाठ और छवियों दोनों को संसाधित करते हुए।",
        "badge.agi": "AGI प्रगति",

        "event31.title": "Claude 3 परिवार",
        "event31.pioneer": "Anthropic अनुसंधान टीम (संयुक्त राज्य अमेरिका)",
        "event31.description": "Claude 3 (Opus, Sonnet, Haiku) जारी किया, Opus ने कई बेंचमार्क पर GPT-4 को पार किया। Claude ने अत्याधुनिक प्रदर्शन हासिल करते हुए सुरक्षा, ईमानदारी और उपयोगिता पर जोर दिया।",
        "badge.constitutional": "संवैधानिक AI",
        "badge.ethical": "नैतिक AI",

        "event32.title": "Gemini Ultra और 2M संदर्भ",
        "event32.pioneer": "गूगल DeepMind (यूनाइटेड किंगडम/संयुक्त राज्य अमेरिका)",
        "event32.description": "गूगल ने अभूतपूर्व 2 मिलियन टोकन संदर्भ विंडो के साथ Gemini 1.5 जारी किया, घंटों के वीडियो या संपूर्ण कोडबेस को संसाधित करने में सक्षम। Gemini Ultra ने सभी बेंचमार्क पर GPT-4 से मेल खाया।",
        "badge.long-context": "लंबा संदर्भ",

        "event33.title": "DeepSeek-V3 ओपन सोर्स",
        "event33.pioneer": "लियांग वेनफेंग और DeepSeek (चीन)",
        "event33.description": "चीनी स्टार्टअप DeepSeek ने V3 (671 बिलियन पैरामीटर) को ओपन सोर्स के रूप में जारी किया, GPT-4 के प्रदर्शन से मेल खाते हुए जबकि प्रशिक्षण लागत केवल $5.5 मिलियन थी। इसने साबित किया कि अत्याधुनिक AI को अरब डॉलर के बजट की आवश्यकता नहीं है।",
        "badge.cost": "लागत दक्षता",

        "event34.title": "GLM-4 सफलता",
        "event34.pioneer": "तांग जी और Zhipu AI (चीन)",
        "event34.description": "Zhipu AI के GLM-4 ने केवल 9 बिलियन पैरामीटर के साथ 1 मिलियन टोकन संदर्भ विंडो हासिल की, असाधारण बहुभाषी क्षमताओं का प्रदर्शन करते हुए और पूरी तरह से ओपन सोर्स होने के बावजूद पश्चिमी मॉडल के साथ प्रतिस्पर्धी प्रदर्शन।",
        "badge.multilingual": "बहुभाषी AI",

        // Awards Section
        "awards.title": "प्रमुख मान्यताएं और पुरस्कार",
        "awards.description": "AI को बदलने वाले अग्रदूतों को विज्ञान और प्रौद्योगिकी में उच्चतम सम्मान से सम्मानित किया गया है।",
        "award1.title": "2018 ट्यूरिंग पुरस्कार",
        "award1.recipients": "जेफ्री हिंटन, योशुआ बेंगियो, यान लेकुन",
        "award1.description": "गहरे न्यूरल नेटवर्क में वैचारिक और इंजीनियरिंग सफलताओं के लिए कंप्यूटिंग का नोबेल पुरस्कार।",
        "award2.title": "2011 ट्यूरिंग पुरस्कार",
        "award2.recipients": "जुडिया पर्ल",
        "award2.description": "संभाव्य और कारण तर्क के माध्यम से AI में मौलिक योगदान के लिए।",
        "award3.title": "2024 रसायन विज्ञान नोबेल पुरस्कार",
        "award3.recipients": "डेमिस हासाबिस (DeepMind)",
        "award3.description": "प्रोटीन संरचना भविष्यवाणी में AlphaFold2 की सफलता के लिए।",
        "award4.title": "2022 IEEE सम्मान पदक",
        "award4.recipients": "यान लेकुन",
        "award4.description": "डीप लर्निंग और कन्वोल्यूशनल न्यूरल नेटवर्क में अग्रणी योगदान के लिए।",
        "award5.title": "2022 प्रिंसेस ऑफ एस्टुरियस पुरस्कार",
        "award5.recipients": "डेमिस हासाबिस",
        "award5.description": "AI के माध्यम से वैज्ञानिक और तकनीकी अनुसंधान में उत्कृष्ट योगदान के लिए।",
        "award6.title": "TIME 100 सबसे प्रभावशाली",
        "award6.recipients": "सैम अल्टमैन (2023), डारियो अमोडेई (2024)",
        "award6.description": "जनरेटिव AI क्रांति का नेतृत्व करने और इसके भविष्य को आकार देने के लिए मान्यता प्राप्त।",

        // Footer
        "footer.description": "AI उपकरण और प्रौद्योगिकियों के लिए आपकी अंतिम मार्गदर्शिका। सर्वश्रेष्ठ AI समाधान खोजें, तुलना करें और मास्टर करें।",
        "footer.quick-links": "त्वरित लिंक",
        "footer.resources": "संसाधन",
        "footer.follow": "हमें फ़ॉलो करें",
        "footer.copyright": "© 2024 TechVernia। सर्वाधिकार सुरक्षित।"
    }
};

// Translation function with debug logging
function translateAIHistory(lang) {
    

    const translations = aiHistoryTranslations[lang] || aiHistoryTranslations.en;
    const elements = document.querySelectorAll('[data-i18n]');
    

    let translatedCount = 0;
    let skippedCount = 0;

    elements.forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[key]) {
            element.textContent = translations[key];
            translatedCount++;
        } else {
            
            skippedCount++;
        }
    });

    
    
    );
}

// Initialize translation on page load
document.addEventListener('DOMContentLoaded', () => {
    
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    
    translateAIHistory(currentLang);
});

// Listen for language changes from main.js
document.addEventListener('languageChanged', (event) => {
    
    translateAIHistory(event.detail.language);
});

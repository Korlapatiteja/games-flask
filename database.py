import sqlite3
c = sqlite3.connect('test.db')
cur=c.cursor()
data=[
('The Sims 4', 'EA', '20GB', 5, 'Simulation'),
('Microsoft Flight Simulator', 'Xbox Game Studios', '100GB', 5, 'Simulation'),
('Cities Skylines', 'Paradox Interactive', '8GB', 5, 'Simulation'),
('Euro Truck Simulator 2', 'SCS Software', '12GB', 4, 'Simulation'),
('Planet Zoo', 'Frontier Developments', '16GB', 5, 'Simulation'),
('Farming Simulator 22', 'Giants Software', '35GB', 4, 'Simulation'),
('Train Simulator', 'Dovetail Games', '40GB', 3, 'Simulation'),
('House Flipper', 'Empyrean', '6GB', 4, 'Simulation'),
('Car Mechanic Simulator', 'Red Dot Games', '10GB', 4, 'Simulation'),
('Prison Architect', 'Paradox Interactive', '4GB', 5, 'Simulation'),

('The Legend of Zelda: Breath of the Wild', 'Nintendo', '14GB', 5, 'Adventure'),
('Uncharted 4', 'Naughty Dog', '50GB', 5, 'Adventure'),
('Tomb Raider', 'Square Enix', '25GB', 4, 'Adventure'),
('Red Dead Redemption 2', 'Rockstar Games', '150GB', 5, 'Adventure'),
('Assassins Creed Valhalla', 'Ubisoft', '80GB', 4, 'Adventure'),
('God of War', 'Sony', '45GB', 5, 'Adventure'),
('Horizon Zero Dawn', 'Guerrilla Games', '50GB', 5, 'Adventure'),
('Far Cry 5', 'Ubisoft', '40GB', 4, 'Adventure'),
('Ghost of Tsushima', 'Sucker Punch', '60GB', 5, 'Adventure'),
('Life is Strange', 'Dontnod', '15GB', 4, 'Adventure'),

('Call of Duty Modern Warfare', 'Activision', '80GB', 5, 'Action'),
('Battlefield V', 'EA', '50GB', 4, 'Action'),
('DOOM Eternal', 'Bethesda', '40GB', 5, 'Action'),
('Resident Evil Village', 'Capcom', '35GB', 5, 'Action'),
('Sekiro Shadows Die Twice', 'FromSoftware', '25GB', 5, 'Action'),
('Devil May Cry 5', 'Capcom', '30GB', 5, 'Action'),
('Watch Dogs Legion', 'Ubisoft', '45GB', 4, 'Action'),
('Just Cause 4', 'Square Enix', '60GB', 4, 'Action'),
('Hitman 3', 'IO Interactive', '70GB', 5, 'Action'),
('Max Payne 3', 'Rockstar Games', '35GB', 4, 'Action'),

('FIFA 24', 'EA Sports', '50GB', 4, 'Sports'),
('eFootball 2024', 'Konami', '40GB', 3, 'Sports'),
('NBA 2K24', '2K Sports', '90GB', 4, 'Sports'),
('WWE 2K23', '2K Sports', '60GB', 4, 'Sports'),
('Madden NFL 24', 'EA Sports', '55GB', 4, 'Sports'),
('PGA Tour 2K23', '2K Sports', '30GB', 3, 'Sports'),
('Cricket 22', 'Big Ant Studios', '45GB', 4, 'Sports'),
('F1 23', 'Codemasters', '80GB', 5, 'Sports'),
('Tennis World Tour 2', 'Nacon', '20GB', 3, 'Sports'),
('Pro Cycling Manager', 'Nacon', '15GB', 3, 'Sports'),

('Forza Horizon 5', 'Xbox Game Studios', '110GB', 5, 'Racing'),
('Need for Speed Unbound', 'EA', '50GB', 4, 'Racing'),
('Gran Turismo 7', 'Sony', '100GB', 5, 'Racing'),
('F1 24', 'Codemasters', '90GB', 5, 'Racing'),
('The Crew 2', 'Ubisoft', '60GB', 4, 'Racing'),
('Assetto Corsa', 'Kunos Simulazioni', '30GB', 5, 'Racing'),
('Project Cars 2', 'Slightly Mad Studios', '50GB', 4, 'Racing'),
('Dirt Rally 2.0', 'Codemasters', '45GB', 5, 'Racing'),
('Burnout Paradise Remastered', 'EA', '20GB', 4, 'Racing'),
('MotoGP 23', 'Milestone', '35GB', 4, 'Racing')]
cur.executemany('insert into games(name,company,size,ratting,gametype) values(?,?,?,?,?)',data)
c.commit()



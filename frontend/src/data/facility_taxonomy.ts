// Curated, extensible facility taxonomy
// Add/modify categories and types as needed; keep keys human-readable

export type FacilityTaxonomy = Record<string, string[]>;

export const FACILITY_TAXONOMY: FacilityTaxonomy = {
  Fitness: [
    'Gym', 'Fitness Studio', 'Yoga Studio', 'Pilates Studio', 'CrossFit Box',
    'Martial Arts Academy', 'Swimming Pool', 'Sports Club', 'Cycling Studio', 'Climbing Gym',
    'Dance Studio', 'Boxing Gym', 'Athletic Track', 'Recreation Center'
  ],
  Education: [
    'School', 'College', 'University', 'Coaching Center', 'Training Institute', 'Library', 'EdTech Center',
    'Research Institute', 'Language School', 'Vocational Training', 'Kindergarten'
  ],
  'Product Software': [
    'SaaS Company', 'DevTools', 'AI Platform', 'Analytics', 'Security Product', 'Fintech Product',
    'Gaming Studio', 'Hardware Manufacturer'
  ],
  'Services Software': [
    'IT Services', 'Consulting', 'Digital Agency', 'Cloud Services', 'Managed Services',
    'Cybersecurity Services', 'Web Development', 'Mobile App Development', 'Data Center'
  ],
  Healthcare: [
    'Hospital', 'Clinic', 'Pharmacy', 'Diagnostic Center', 'Dental Clinic', 'Physiotherapy Center',
    'Rehabilitation Center', 'Veterinary Clinic', 'Mental Health Clinic', 'Medical Lab', 'Eye Clinic'
  ],
  Retail: [
    'Shopping Mall', 'Supermarket', 'Electronics Store', 'Clothing Store', 'Bookstore', 'Convenience Store',
    'Department Store', 'Furniture Store', 'Grocery Store', 'Pharmacy Retail', 'Hardware Store'
  ],
  Hospitality: [
    'Hotel', 'Restaurant', 'Cafe', 'Resort', 'Bed & Breakfast', 'Motel', 'Hostel', 'Event Venue', 'Catering Service'
  ],
  Logistics: [
    'Warehouse', 'Fulfillment Center', 'Logistics Hub', 'Courier Office', 'Distribution Center',
    'Freight Forwarder', 'Port Cargo', 'Airport Cargo'
  ],
  Finance: [
    'Bank', 'ATM', 'Insurance Office', 'Brokerage', 'Investment Firm', 'Credit Union', 'Accounting Firm'
  ],
  Government: [
    'Post Office', 'Police Station', 'Fire Station', 'Municipal Office', 'Court House', 'Embassy', 'City Hall'
  ],
  Transportation: [
    'Airport', 'Train Station', 'Bus Station', 'Metro Station', 'Ferry Terminal', 'Car Rental', 'Taxi Stand',
    'Parking Garage', 'Auto Repair'
  ],
  Agriculture: [
    'Agri Supply', 'Farm Equipment', 'Agri Consulting', 'Seed Store', 'Farm', 'Dairy', 'Winery', 'Fishery'
  ],
  'Arts & Entertainment': [
    'Museum', 'Art Gallery', 'Theater', 'Cinema', 'Music Venue', 'Amusement Park', 'Aquarium', 'Zoo'
  ],
  Automotive: [
    'Car Dealer', 'Auto Repair', 'Car Wash', 'Gas Station', 'Auto Parts Store', 'EV Charging Station'
  ],
  'Beauty & Spa': [
    'Salon', 'Barber Shop', 'Spa', 'Nail Salon', 'Massage Center'
  ],
  'Business & Office': [
    'Coworking Space', 'Corporate Office', 'Business Park', 'Conference Center'
  ],
  'Community & Organizations': [
    'Community Center', 'NGO', 'Charity', 'Youth Center', 'Senior Center'
  ],
  Construction: [
    'Construction Company', 'Architect', 'Civil Engineering', 'Contractor', 'Building Materials Store'
  ],
  'Food & Drink': [
    'Bakery', 'Butcher', 'Deli', 'Ice Cream Shop', 'Food Court', 'Food Truck'
  ],
  'Housing & Real Estate': [
    'Apartment Complex', 'Real Estate Agency', 'Property Management', 'Student Housing'
  ],
  Industrial: [
    'Factory', 'Industrial Park', 'Manufacturing Plant', 'Power Plant'
  ],
  Landmarks: [
    'Monument', 'Historical Site', 'Tourist Attraction', 'Viewpoint'
  ],
  Media: [
    'TV Station', 'Radio Station', 'Newspaper Office', 'Recording Studio'
  ],
  'Outdoors & Recreation': [
    'Park', 'Playground', 'Hiking Trail', 'Beach', 'Campground'
  ],
  Pets: [
    'Pet Store', 'Pet Grooming', 'Animal Shelter', 'Veterinary Clinic'
  ],
  'Professional Services': [
    'Law Firm', 'Consulting Firm', 'Design Studio', 'Photography Studio', 'Recruitment Agency'
  ],
  Religious: [
    'Temple', 'Church', 'Mosque', 'Gurudwara', 'Synagogue'
  ],
  'Science & Research': [
    'Research Lab', 'Innovation Center', 'Tech Park'
  ],
  Shopping: [
    'Market', 'Flea Market', 'Wholesale Market', 'Outlet Store', 'Jewelry Store'
  ],
  'Sports & Recreation': [
    'Stadium', 'Sports Complex', 'Cricket Ground', 'Football Ground', 'Tennis Court', 'Badminton Court'
  ],
  'Travel & Tourism': [
    'Tour Operator', 'Travel Agency', 'Visitor Center', 'Tourist Information'
  ],
  Utilities: [
    'Water Utility', 'Electric Utility', 'Waste Management', 'Recycling Center'
  ],
};

export const DEFAULT_CATEGORY = 'Fitness';
export const DEFAULT_TYPE = 'Gym';

export function getAllTypes(): string[] {
  return Object.values(FACILITY_TAXONOMY).flat();
}



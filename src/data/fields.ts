// Available Google Place Details fields (only fields that Google Places API actually provides)
// Grouped by category for better organization

export const AVAILABLE_FIELDS: Record<string, Record<string, string>> = {
  'Basic Information': {
    name: 'Facility Name',
    place_id: 'Place ID',
    business_status: 'Business Status',
  },
  'Contact Information': {
    formatted_phone_number: 'Phone (Local)',
    international_phone_number: 'Phone (International)',
    website: 'Website',
  },
  'Location Details': {
    formatted_address: 'Full Address',
    vicinity: 'Vicinity',
    location: 'Search Location',
  },
  'Ratings & Reviews': {
    google_rating: 'Google Rating',
    user_ratings_total: 'Total Reviews',
    price_level: 'Price Level',
  },
  'Business Details': {
    types: 'Business Types',
    url: 'Google Maps URL',
  },
  'Coordinates': {
    geometry: 'Coordinates',
    plus_code: 'Plus Code',
  },
  'Web Scraped Data': {
    email: 'Email Address',
    facebook: 'Facebook Page',
    twitter: 'Twitter/X Handle',
    linkedin: 'LinkedIn Profile',
    youtube: 'YouTube Channel',
    phone: 'Additional Phone Numbers',
    address: 'Website Address',
    hours: 'Business Hours',
    description: 'Business Description',
    founded: 'Founded Year',
  },
};

export const defaultFields: string[] = [
  'name',
  'formatted_phone_number',
  'website',
  'formatted_address',
  'google_rating',
  'user_ratings_total',
  'business_status',
];

export const fieldDescriptions: Record<string, string> = {
  // Basic Information
  name: 'Official or commonly known facility name from Google Places',
  place_id: 'Google Places unique identifier for the location',
  business_status: 'Current operational status (OPERATIONAL, CLOSED_TEMPORARILY, CLOSED_PERMANENTLY)',
  
  // Contact Information
  formatted_phone_number: 'Phone number in local format as provided by Google',
  international_phone_number: 'Phone number in E.164 international format',
  website: 'Official website URL if available',
  
  // Location Details
  formatted_address: 'Complete formatted address as provided by Google',
  vicinity: 'General area or neighborhood name',
  location: 'Search location context (city, country)',
  
  // Ratings & Reviews
  google_rating: 'Average Google user rating (0.0 - 5.0)',
  user_ratings_total: 'Total number of user ratings on Google',
  price_level: 'Price level indicator (0-4, where 4 is most expensive)',
  
  // Business Details
  types: 'Business categories and types as classified by Google',
  url: 'Direct link to Google Maps page for this place',
  
  // Coordinates
  geometry: 'Latitude and longitude coordinates',
  plus_code: 'Google Plus Code for precise location reference',
  
  // Web Scraped Data
  email: 'Email address extracted from business website',
  facebook: 'Facebook page URL found on website',
  twitter: 'Twitter/X handle or profile URL',
  linkedin: 'LinkedIn company or personal profile URL',
  youtube: 'YouTube channel URL',
  phone: 'Additional phone numbers found on website',
  address: 'Business address extracted from website',
  hours: 'Operating hours extracted from website',
  description: 'Business description from website meta or content',
  founded: 'Year business was founded (from website)',
};



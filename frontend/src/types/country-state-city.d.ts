declare module 'country-state-city' {
  export interface ICountry { name: string; isoCode: string; }
  export interface IState { name: string; isoCode: string; }
  export interface ICity { name: string; }

  export const Country: {
    getAllCountries(): ICountry[];
  };

  export const State: {
    getStatesOfCountry(countryIsoCode: string): IState[];
  };

  export const City: {
    getCitiesOfState(countryIsoCode: string, stateIsoCode: string): ICity[];
  };
}



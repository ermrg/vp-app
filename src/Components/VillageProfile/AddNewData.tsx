import React from "react";
import GharKoBiabarn from "./Forms/GharKoBiabarn";
const requiredFields = [1, 2]
export default function AddNewData(props: any) {
  let { data } = props;
  data.requiredFields = requiredFields
  return (
    <div className="vp-form-wrapper">
      <GharKoBiabarn data={data}/>
    </div>
  );
}

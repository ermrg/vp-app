import React from "react";
import GharKoBiabarn from "./Forms/GharKoBiabarn";

export default function AddNewData(props: any) {
  let { data } = props;
  return (
    <div className="vp-form-wrapper">
      <GharKoBiabarn data/>
    </div>
  );
}

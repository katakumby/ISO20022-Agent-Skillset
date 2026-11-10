---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.8 ProrationBelowMinimumQuantity <PrratnBlwMinQty>", "3.4.11.8.2 Proprietary <Prtry>"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.8.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
CodeName Name Definition
MILU RoundUp Instructions will be accepted but rounded
up to the specified minimum multiple
quantity to instruct.
UKWN Unknown Processing of instructions prorated
below the minimum quantity to instruct is
unknown.
3.4.11.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the proration below minimum quantity type.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.11.9  NonDomicileCountry <NonDmclCtry>
Presence: [0..*]
Definition: Holder of the security has to certify, in line with the terms of the corporate action, that it is not
domiciled in the country indicated.
Impacted by: C17 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
3.4.11.10  ValidDomicileCountry <VldDmclCtry>
Presence: [0..*]
Definition: Country of domicile in which the Corporate Action option is valid. The holder of the security
has to certify that it is domiciled in the country indicated.
Impacted by: C17 "Country"
Datatype: "CountryCode" on page 1205
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 144 February 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: []
file_pages: [139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# Continuation at file page 139

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 139 to 139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 139

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     InformationToComplyWith <InfToCmplyWth> [0..*]  248
       Language <Lang> [1..1] CodeSet 248
       AdditionalInformation <AddtlInf> [1..*] Text 248
     SecurityRestriction <SctyRstrctn> [0..*]  249
       Language <Lang> [1..1] CodeSet 249
       AdditionalInformation <AddtlInf> [1..*] Text 249
     TaxationConditions <TaxtnConds> [0..*]  249
       Language <Lang> [1..1] CodeSet 249
       AdditionalInformation <AddtlInf> [1..*] Text 250
     Disclaimer <Dsclmr> [0..*]  250
       Language <Lang> [1..1] CodeSet 250
       AdditionalInformation <AddtlInf> [1..*] Text 250
     CertificationBreakdown <CertfctnBrkdwn> [0..*]  250
       Language <Lang> [1..1] CodeSet 250
       AdditionalInformation <AddtlInf> [1..*] Text 251
Constraints
• AdditionalTextRule
If OptionType/Code is OTHR (Other), then at least one occurrence of AdditionalInformation/
AdditionalText/AdditionalInformation must be present.
(MT564 NVR C5).
On Condition
    /OptionType/Code is present
 And    /OptionType/Code is equal to value 'Other'
Following Must be True
    /AdditionalInformation Must be present
 And    /AdditionalInformation/AdditionalText[*] Must be present
 And    /AdditionalInformation/AdditionalText[*]/AdditionalInformation Must be 
present
• AppliedOptionRule
If DefaultProcessingOrStandingInstruction/DefaultOptionIndicator is present and its value is '1' or
'true' (Yes), then AppliedOptionIndicator value must not be '1' or 'true' (Yes).
• InstructCashAmountRule
If OptionFeatures/Code QCAS (InstructCashAmount) is not present, then any message elements in
the list (PriceDetails/MaximumCashToInstruct, PriceDetails/MinimumCashToInstruct, PriceDetails/
MinimumMutipleCashToInstruct) must not be present.
(MT564 NVR C20).
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 139 February 2026
```


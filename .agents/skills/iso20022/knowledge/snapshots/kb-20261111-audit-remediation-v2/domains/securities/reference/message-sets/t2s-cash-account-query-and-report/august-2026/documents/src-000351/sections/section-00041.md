---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.6 AccountReturnCriteria <AcctRtrCrit>", "2.4.6.19 Proprietary <Prtry>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.6.19 Proprietary <Prtry>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 181):
• Meaning When True: Yes
• Meaning When False: No
2.4.6.19  Proprietary <Prtry>
Presence: [0..*]
Definition: Indicates if this field must be present in the response.
Proprietary <Prtry> contains the following GenericIdentification42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SchemeName <SchmeNm> [0..1] Text 45
   Issuer <Issr> [0..1] Text 45
2.4.6.19.1  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 183
2.4.6.19.2  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 183
2.4.7 DigitalSignature <DgtlSgntr>
Presence: [0..*]
Definition: Contains the signature with its components, namely signed info, signature value, key info
and the object.
DigitalSignature <DgtlSgntr> contains the following PartyAndSignature4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 45
   Signature <Sgntr> [1..1] (External Schema) 46
2.4.7.1  Party <Pty>
Presence: [1..1]
Definition: Entity involved in an activity.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 45 August 2026
```


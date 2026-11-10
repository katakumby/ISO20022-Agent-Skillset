---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.40 AfterExchangePhysicalForm <AftrXchgPhysForm>", "13.1.6.4.40.2 Proprietary <Prtry>"]
file_pages: [440]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.40.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 440 to 440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 440

```text
13.1.6.4.40.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Initial physical form expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.4.41  CommonSafekeeper <CmonSfkpr>
Presence: [0..1]
Definition: Entity appointed by the ICSDs to provide safekeeping for securities in new global note (NGN)
form.
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 530
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
13.1.6.4.42  RedemptionType <RedTp>
Presence: [0..1]
Definition: Indicates the type of redemption at maturity.
RedemptionType <RedTp> contains one of the following MaturityRedemptionType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 440
Or}   Proprietary <Prtry> [1..1] ± 441
13.1.6.4.42.1  Code <Cd>
Presence: [1..1]
Definition: Maturity redemption type expressed as an ISO 20022 code.
Datatype: "MaturityRedemptionType1Code" on page 519
CodeName Name Definition
FRED FinalRedemption Indicates that the type of redemption at
maturity is final.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 440 March 2024
```


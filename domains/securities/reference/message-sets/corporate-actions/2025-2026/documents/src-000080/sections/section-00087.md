---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.4 OptionFeatures <OptnFeatrs>", "3.4.11.4.2 Proprietary <Prtry>"]
file_pages: [142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.4.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 142 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 142

```text
CodeName Name Definition
BOIS BeneficiaryOwnerInstruction Indicates that the holder needs to
instruct at beneficiary owner level only.
QCAS InstructCashAmount Feature whereby the holder should only
instruct a cash amount.
SHAR ShareholderNumber Indicates usage of a reference number
to identify an investor or a shareholder
with the issuer or the registration
provider (for instance allocation code).
RGRS GrossDividendReinvestment Gross dividend is reinvested.
RNET NetDividendReinvestment Dividend reinvestment is processed net
of withholding tax.
FCFS FirstComeFirstServed Securities will be accepted in the order
they have been submitted until the target
number of quantity sought is reached.
3.4.11.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the features that may apply to a corporate action option.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.11.5  OptionAvailabilityStatus <OptnAvlbtySts>
Presence: [0..1]
Definition: Specifies the status of the option.
OptionAvailabilityStatus <OptnAvlbtySts> contains one of the following elements (see
"OptionAvailabilityStatus3Choice" on page 891 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 891
Or}   Proprietary <Prtry> [1..1] ± 891
3.4.11.6  CertificationBreakdownType <CertfctnBrkdwnTp>
Presence: [0..*]
Definition: Type of certification/breakdown.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 142 February 2026
```


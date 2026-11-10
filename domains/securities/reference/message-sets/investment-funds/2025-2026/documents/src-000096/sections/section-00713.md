---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.5 Portfolio <Prtfl>", "35.4.14.5.3 Pension <Pnsn>"]
file_pages: [981]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.5.3 Pension <Pnsn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 981 to 981.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 981

```text
35.4.14.5.3  Pension <Pnsn>
Presence: [1..1]
Definition: Portfolio is a pension policy, plan or scheme.
Pension <Pnsn> contains the following Pension6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1]  981
     Identifier <Idr> [1..1] Text 981
     SubIdentifier <SubIdr> [0..1] Text 981
     AdditionalInformation <AddtlInf> [0..1] ± 982
   Type <Tp> [0..1]  982
{Or     Code <Cd> [1..1] CodeSet 982
Or}     Proprietary <Prtry> [1..1] ± 983
   TransferScope <TrfScp> [0..1] ± 983
   TaxReference <TaxRef> [0..*] ± 984
   DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 984
   NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 984
   AdditionalInformation <AddtlInf> [0..*] ± 984
35.4.14.5.3.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the pension policy, plan or scheme.
Identification <Id> contains the following PensionPolicy1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identifier <Idr> [1..1] Text 981
   SubIdentifier <SubIdr> [0..1] Text 981
   AdditionalInformation <AddtlInf> [0..1] ± 982
35.4.14.5.3.1.1  Identifier <Idr>
Presence: [1..1]
Definition: Reference number of the pension policy, plan or scheme.
Datatype: "Max35Text" on page 5403
35.4.14.5.3.1.2  SubIdentifier <SubIdr>
Presence: [0..1]
Definition: Sub-identification of the pension policy, plan or scheme, such as a member reference.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 981 May 2026
```


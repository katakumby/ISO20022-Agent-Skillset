---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.3 TransferConfirmationIdentification <TrfConfId>"]
file_pages: [979]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.3 TransferConfirmationIdentification <TrfConfId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 979 to 979.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 979

```text
Definition: Identification assigned to the transfer of assets.
Datatype: "Max35Text" on page 5403
35.4.14.3  TransferConfirmationIdentification <TrfConfId>
Presence: [0..1]
Definition: Identification of the confirmation assigned by the transferor to the transfer.
Datatype: "Max35Text" on page 5403
35.4.14.4  RequestedTransferDate <ReqdTrfDt>
Presence: [0..1]
Definition: Date for which the instructing party requests the transfer of the portfolio as a whole.
Datatype: "ISODate" on page 5388
35.4.14.5  Portfolio <Prtfl>
Presence: [0..1]
Definition: Choice of tax efficient product, general investment or pension.
Portfolio <Prtfl> contains one of the following FundPortfolio8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TaxEfficientProduct <TaxEffcntPdct> [1..1] ± 979
Or   GeneralInvestment <GnlInvstmt> [1..1] ± 980
Or}   Pension <Pnsn> [1..1]  981
     Identification <Id> [0..1]  981
       Identifier <Idr> [1..1] Text 981
       SubIdentifier <SubIdr> [0..1] Text 981
       AdditionalInformation <AddtlInf> [0..1] ± 982
     Type <Tp> [0..1]  982
{Or       Code <Cd> [1..1] CodeSet 982
Or}       Proprietary <Prtry> [1..1] ± 983
     TransferScope <TrfScp> [0..1] ± 983
     TaxReference <TaxRef> [0..*] ± 984
     DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 984
     NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 984
     AdditionalInformation <AddtlInf> [0..*] ± 984
35.4.14.5.1  TaxEfficientProduct <TaxEffcntPdct>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 979 May 2026
```


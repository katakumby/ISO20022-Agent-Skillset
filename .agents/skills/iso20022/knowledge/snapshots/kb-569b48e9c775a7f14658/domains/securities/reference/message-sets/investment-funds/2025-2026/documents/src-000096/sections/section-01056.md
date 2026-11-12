---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.3 Portfolio <Prtfl>", "39.4.15.3.2 GeneralInvestment <GnlInvstmt>"]
file_pages: [1461]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.3.2 GeneralInvestment <GnlInvstmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1461 to 1461.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1461

```text
39.4.15.3.2  GeneralInvestment <GnlInvstmt>
Presence: [1..1]
Definition: Portfolio is a general investment.
GeneralInvestment <GnlInvstmt> contains the following elements (see "GeneralInvestment2" on
page 4509 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] ± 4509
   OwnershipType <OwnrshTp> [0..1] CodeSet 4509
   CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 4511
   EstimatedValue <EstmtdVal> [0..1] ± 4511
   AdditionalInformation <AddtlInf> [0..*] ± 4511
39.4.15.3.3  Pension <Pnsn>
Presence: [1..1]
Definition: Portfolio is a pension policy, plan or scheme.
Pension <Pnsn> contains the following Pension6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1]  1461
     Identifier <Idr> [1..1] Text 1462
     SubIdentifier <SubIdr> [0..1] Text 1462
     AdditionalInformation <AddtlInf> [0..1] ± 1462
   Type <Tp> [0..1]  1462
{Or     Code <Cd> [1..1] CodeSet 1462
Or}     Proprietary <Prtry> [1..1] ± 1463
   TransferScope <TrfScp> [0..1] ± 1464
   TaxReference <TaxRef> [0..*] ± 1464
   DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1464
   NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1464
   AdditionalInformation <AddtlInf> [0..*] ± 1465
39.4.15.3.3.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the pension policy, plan or scheme.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1461 May 2026
```


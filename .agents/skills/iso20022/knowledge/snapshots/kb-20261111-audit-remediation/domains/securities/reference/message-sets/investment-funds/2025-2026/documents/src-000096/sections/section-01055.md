---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.3 Portfolio <Prtfl>"]
file_pages: [1460]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.3 Portfolio <Prtfl>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1460 to 1460.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1460

```text
39.4.15.3  Portfolio <Prtfl>
Presence: [0..1]
Definition: Choice of tax efficient product, general investment or pension.
Portfolio <Prtfl> contains one of the following FundPortfolio9Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TaxEfficientProduct <TaxEffcntPdct> [1..1] ± 1460
Or   GeneralInvestment <GnlInvstmt> [1..1] ± 1461
Or}   Pension <Pnsn> [1..1]  1461
     Identification <Id> [0..1]  1461
       Identifier <Idr> [1..1] Text 1462
       SubIdentifier <SubIdr> [0..1] Text 1462
       AdditionalInformation <AddtlInf> [0..1] ± 1462
     Type <Tp> [0..1]  1462
{Or       Code <Cd> [1..1] CodeSet 1462
Or}       Proprietary <Prtry> [1..1] ± 1463
     TransferScope <TrfScp> [0..1] ± 1464
     TaxReference <TaxRef> [0..*] ± 1464
     DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1464
     NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1464
     AdditionalInformation <AddtlInf> [0..*] ± 1465
39.4.15.3.1  TaxEfficientProduct <TaxEffcntPdct>
Presence: [1..1]
Definition: Portfolio is a government scheme to encourage investment in securities based unit and
investment trusts, offering certain tax benefits. These are not investments in their own right but are tax
exempt 'wrappers' in which equities, bonds and funds can be held to shelter them from various types of
tax.
In the UK, a typical tax wrapper product is known as an 'ISA' (Individual Savings Account).
TaxEfficientProduct <TaxEffcntPdct> contains the following elements (see "TaxEfficientProduct4" on
page 4491 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 4492
   CurrentYear <CurYr> [0..1] Indicator 4492
   PreviousYears <PrvsYrs> [0..1] ± C23 4492
   AdditionalInformation <AddtlInf> [0..*] ± 4493
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1460 May 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.5 Portfolio <Prtfl>", "35.4.14.5.2 GeneralInvestment <GnlInvstmt>"]
file_pages: [980]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.5.2 GeneralInvestment <GnlInvstmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 980 to 980.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 980

```text
Definition: Portfolio is a government scheme to encourage investment in securities based unit and
investment trusts, offering certain tax benefits. These are not investments in their own right but are tax
exempt 'wrappers' in which equities, bonds and funds can be held to shelter them from various types of
tax.
In the UK, a typical tax wrapper product is known as an 'ISA' (Individual Savings Account).
TaxEfficientProduct <TaxEffcntPdct> contains the following elements (see "TaxEfficientProduct6" on
page 4501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 4502
   CurrentYear <CurYr> [0..1] Indicator 4502
   CashComponentIndicator <CshCmpntInd> [0..1] Indicator 4502
   PreviousYears <PrvsYrs> [0..1]  C42 4503
     PreviousYears <PrvsYrs> [1..1]  4503
{Or       AllPreviousYears <AllPrvsYrs> [1..1] Text 4503
Or}       SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 4503
     CashComponentIndicator <CshCmpntInd> [0..1] Indicator 4504
   CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C45 4504
     DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 4504
     EquityComponent <EqtyCmpnt> [0..1] Amount C1 4504
     CashComponent <CshCmpnt> [0..1] Amount C1 4505
     TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 4505
   AdditionalInformation <AddtlInf> [0..*] ± 4505
35.4.14.5.2  GeneralInvestment <GnlInvstmt>
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
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 980 May 2026
```


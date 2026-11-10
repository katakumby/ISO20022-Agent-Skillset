---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>"]
file_pages: [1536, 1537]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1536 to 1537.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1536

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalInformation <AddtlInf> [0..*] ± 1562
40.4.15.5.1  TaxEfficientProduct <TaxEffcntPdct>
Presence: [1..1]
Definition: Portfolio is a government scheme to encourage investment in securities based unit and
investment trusts, offering certain tax benefits. These are not investments in their own right but are tax
exempt 'wrappers' in which equities, bonds and funds can be held to shelter them from various types of
tax.
In the UK, a typical tax wrapper product is known as an 'ISA' (Individual Savings Account).
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1536 May 2026
```

## File page 1537

```text
TaxEfficientProduct <TaxEffcntPdct> contains the following TaxEfficientProduct7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1538
   CurrentYear <CurYr> [0..1] Indicator 1538
   CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1539
   PreviousYears <PrvsYrs> [0..1]  C49 1539
     PreviousYears <PrvsYrs> [1..1]  1539
{Or       AllPreviousYears <AllPrvsYrs> [1..1] Text 1539
Or}       SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1540
     CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1540
   PreviousYearSubscriptionAmount <PrvsYrSbcptAmt> [0..1] Amount C1 1540
   PreviousYearsSubscriptionAmount
<PrvsYrsSbcptAmt>
[0..1] Amount C1 1540
   DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1540
   CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C52 1541
     DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1541
     EquityComponent <EqtyCmpnt> [0..1] Amount C1 1541
     CashComponent <CshCmpnt> [0..1] Amount C1 1541
     TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1542
   BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1542
     TypeOfAmount <TpOfAmt> [1..1]  1543
{Or       Code <Cd> [1..1] CodeSet 1543
Or}       Proprietary <Prtry> [1..1] ± 1543
     Amount <Amt> [0..1] Amount C2 1543
     Reason <Rsn> [0..1]  1544
{Or       Code <Cd> [1..1] CodeSet 1544
Or}       Proprietary <Prtry> [1..1] ± 1544
     UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1544
     Outstanding <Outsdng> [0..1] Indicator 1545
     Reference <Ref> [0..1] Text 1545
     AdditionalInformation <AddtlInf> [0..*] ± 1545
   WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1545
   TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1545
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1537 May 2026
```


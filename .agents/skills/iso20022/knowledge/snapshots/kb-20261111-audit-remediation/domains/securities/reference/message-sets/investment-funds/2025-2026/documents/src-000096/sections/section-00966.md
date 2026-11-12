---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>"]
file_pages: [1345, 1346]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1345 to 1346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1345

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalInformation <AddtlInf> [0..*] ± 1371
38.4.15.4.1  TaxEfficientProduct <TaxEffcntPdct>
Presence: [1..1]
Definition: Portfolio is a government scheme to encourage investment in securities based unit and
investment trusts, offering certain tax benefits. These are not investments in their own right but are tax
exempt 'wrappers' in which equities, bonds and funds can be held to shelter them from various types of
tax.
In the UK, a typical tax wrapper product is known as an 'ISA' (Individual Savings Account).
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1345 May 2026
```

## File page 1346

```text
TaxEfficientProduct <TaxEffcntPdct> contains the following TaxEfficientProduct7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1347
   CurrentYear <CurYr> [0..1] Indicator 1347
   CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1348
   PreviousYears <PrvsYrs> [0..1]  C42 1348
     PreviousYears <PrvsYrs> [1..1]  1348
{Or       AllPreviousYears <AllPrvsYrs> [1..1] Text 1348
Or}       SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1349
     CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1349
   PreviousYearSubscriptionAmount <PrvsYrSbcptAmt> [0..1] Amount C1 1349
   PreviousYearsSubscriptionAmount
<PrvsYrsSbcptAmt>
[0..1] Amount C1 1349
   DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1349
   CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C45 1350
     DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1350
     EquityComponent <EqtyCmpnt> [0..1] Amount C1 1350
     CashComponent <CshCmpnt> [0..1] Amount C1 1350
     TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1351
   BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1351
     TypeOfAmount <TpOfAmt> [1..1]  1352
{Or       Code <Cd> [1..1] CodeSet 1352
Or}       Proprietary <Prtry> [1..1] ± 1352
     Amount <Amt> [0..1] Amount C2 1352
     Reason <Rsn> [0..1]  1353
{Or       Code <Cd> [1..1] CodeSet 1353
Or}       Proprietary <Prtry> [1..1] ± 1353
     UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1353
     Outstanding <Outsdng> [0..1] Indicator 1354
     Reference <Ref> [0..1] Text 1354
     AdditionalInformation <AddtlInf> [0..*] ± 1354
   WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1354
   TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1354
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1346 May 2026
```


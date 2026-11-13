---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>"]
file_pages: [1153, 1154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1153 to 1154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1153

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalInformation <AddtlInf> [0..*] ± 1179
36.4.15.5.1  TaxEfficientProduct <TaxEffcntPdct>
Presence: [1..1]
Definition: Portfolio is a government scheme to encourage investment in securities based unit and
investment trusts, offering certain tax benefits. These are not investments in their own right but are tax
exempt 'wrappers' in which equities, bonds and funds can be held to shelter them from various types of
tax.
In the UK, a typical tax wrapper product is known as an 'ISA' (Individual Savings Account).
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1153 May 2026
```

## File page 1154

```text
TaxEfficientProduct <TaxEffcntPdct> contains the following TaxEfficientProduct7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1155
   CurrentYear <CurYr> [0..1] Indicator 1155
   CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1156
   PreviousYears <PrvsYrs> [0..1]  C49 1156
     PreviousYears <PrvsYrs> [1..1]  1156
{Or       AllPreviousYears <AllPrvsYrs> [1..1] Text 1156
Or}       SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1157
     CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1157
   PreviousYearSubscriptionAmount <PrvsYrSbcptAmt> [0..1] Amount C1 1157
   PreviousYearsSubscriptionAmount
<PrvsYrsSbcptAmt>
[0..1] Amount C1 1157
   DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1157
   CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C52 1158
     DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1158
     EquityComponent <EqtyCmpnt> [0..1] Amount C1 1158
     CashComponent <CshCmpnt> [0..1] Amount C1 1158
     TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1159
   BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1159
     TypeOfAmount <TpOfAmt> [1..1]  1160
{Or       Code <Cd> [1..1] CodeSet 1160
Or}       Proprietary <Prtry> [1..1] ± 1160
     Amount <Amt> [0..1] Amount C2 1160
     Reason <Rsn> [0..1]  1161
{Or       Code <Cd> [1..1] CodeSet 1161
Or}       Proprietary <Prtry> [1..1] ± 1161
     UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1161
     Outstanding <Outsdng> [0..1] Indicator 1162
     Reference <Ref> [0..1] Text 1162
     AdditionalInformation <AddtlInf> [0..*] ± 1162
   WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1162
   TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1162
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1154 May 2026
```


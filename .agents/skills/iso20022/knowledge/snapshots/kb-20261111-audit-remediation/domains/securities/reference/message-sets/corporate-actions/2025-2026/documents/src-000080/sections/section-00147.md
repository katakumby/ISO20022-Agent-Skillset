---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.10 CashAccountIdentification <CshAcctId>"]
file_pages: [209, 210]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.10 CashAccountIdentification <CshAcctId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 209 to 210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 209

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
3.4.11.25.10  CashAccountIdentification <CshAcctId>
Presence: [0..1]
Definition: Identification of the account in which cash is maintained.
CashAccountIdentification <CshAcctId> contains one of the following elements (see
"CashAccountIdentification9Choice" on page 829 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 829
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 829
Or}   Proprietary <Prtry> [1..1] Text 830
3.4.11.25.11  AmountDetails <AmtDtls>
Presence: [0..1]
Definition: Provides information about the amounts related to a cash movement.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 209 February 2026
```

## File page 210

```text
AmountDetails <AmtDtls> contains the following CorporateActionAmounts77 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GrossAmount <GrssAmt> [0..1] Amount C2, C18 211
   NetAmount <NetAmt> [0..1] Amount C2, C18 212
   SolicitationFees <SlctnFees> [0..1] Amount C2, C18 212
   CashInLieuOfShare <CshInLieuOfShr> [0..1] Amount C2, C18 212
   CapitalGain <CptlGn> [0..1] Amount C2, C18 213
   InterestAmount <IntrstAmt> [0..1] Amount C2, C18 213
   IndemnityAmount <IndmntyAmt> [0..1] Amount C2, C18 214
   ManufacturedDividendPaymentAmount
<ManfctrdDvddPmtAmt>
[0..1] Amount C2, C18 214
   ReinvestmentAmount <RinvstmtAmt> [0..1] Amount C2, C18 215
   FullyFrankedAmount <FullyFrnkdAmt> [0..1] Amount C2, C18 215
   UnfrankedAmount <UfrnkdAmt> [0..1] Amount C2, C18 215
   SundryOrOtherAmount <SndryOrOthrAmt> [0..1] Amount C2, C18 216
   TaxFreeAmount <TaxFreeAmt> [0..1] Amount C2, C18 216
   TaxDeferredAmount <TaxDfrrdAmt> [0..1] Amount C2, C18 217
   ValueAddedTaxAmount <ValAddedTaxAmt> [0..1] Amount C2, C18 217
   StampDutyAmount <StmpDtyAmt> [0..1] Amount C2, C18 217
   TaxReclaimAmount <TaxRclmAmt> [0..1] Amount C2, C18 218
   TaxCreditAmount <TaxCdtAmt> [0..1] Amount C2, C18 218
   AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C2, C18 219
   WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C2, C18 219
   SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C2, C18 219
   FiscalStampAmount <FsclStmpAmt> [0..1] Amount C2, C18 220
   ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] Amount C2, C18 220
   PayingAgentCommissionAmount
<PngAgtComssnAmt>
[0..1] Amount C2, C18 221
   LocalBrokerCommissionAmount
<LclBrkrComssnAmt>
[0..1] Amount C2, C18 221
   RegulatoryFeesAmount <RgltryFeesAmt> [0..1] Amount C2, C18 221
   ShippingFeesAmount <ShppgFeesAmt> [0..1] Amount C2, C18 222
   ChargesAmount <ChrgsAmt> [0..1] Amount C2, C18 222
   EntitledAmount <EntitldAmt> [0..1] Amount C2, C18 223
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 210 February 2026
```


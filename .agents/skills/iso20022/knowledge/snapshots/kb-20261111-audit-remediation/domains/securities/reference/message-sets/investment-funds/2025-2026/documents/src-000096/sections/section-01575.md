---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.21 CashSettlementDetails <CshSttlmDtls>"]
file_pages: [2204, 2205, 2206, 2207]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.21 CashSettlementDetails <CshSttlmDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2204 to 2207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2204

```text
Definition: Currency to be used for pricing the fund. This currency must be among the set of currencies
in which the price may be expressed, as stated in the prospectus.
Impacted by: C4 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
44.4.4.9.21  CashSettlementDetails <CshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2204 May 2026
```

## File page 2205

```text
CashSettlementDetails <CshSttlmDtls> contains the following PaymentTransaction167 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  2208
{Or     CreditTransferDetails <CdtTrfDtls> [1..1]  2212
       Reference <Ref> [0..1] Text 2215
       Debtor <Dbtr> [0..1] ± 2215
       DebtorAccount <DbtrAcct> [0..1]  2215
         Identification <Id> [1..1]  2215
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 2216
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2216
Or}           Other <Othr> [1..1] ± 2216
         Name <Nm> [0..1] Text 2217
       DebtorAgent <DbtrAgt> [0..1]  2217
         Party <Pty> [1..1]  2217
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2218
Or           BICFI <BICFI> [1..1] IdentifierSet C6 2218
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2218
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2219
         LEI <LEI> [0..1] IdentifierSet 2219
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  2220
         Identification <Id> [1..1]  2220
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 2220
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2221
Or}           Other <Othr> [1..1] ± 2221
         Name <Nm> [0..1] Text 2221
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  2221
         Party <Pty> [1..1]  2222
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2222
Or           BICFI <BICFI> [1..1] IdentifierSet C6 2222
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2223
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2224
         LEI <LEI> [0..1] IdentifierSet 2224
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2205 May 2026
```

## File page 2206

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2225
         Identification <Id> [1..1]  2225
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 2225
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2226
Or}           Other <Othr> [1..1] ± 2226
         Name <Nm> [0..1] Text 2226
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  2226
         Party <Pty> [1..1]  2227
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2227
Or           BICFI <BICFI> [1..1] IdentifierSet C6 2227
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2228
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2229
         LEI <LEI> [0..1] IdentifierSet 2229
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2230
         Identification <Id> [1..1]  2230
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 2230
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2231
Or}           Other <Othr> [1..1] ± 2231
         Name <Nm> [0..1] Text 2231
       CreditorAgent <CdtrAgt> [1..1]  2231
         Party <Pty> [1..1]  2232
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2232
Or           BICFI <BICFI> [1..1] IdentifierSet C6 2232
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2233
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2234
         LEI <LEI> [0..1] IdentifierSet 2234
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  2235
         Identification <Id> [1..1]  2235
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 2235
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2236
Or}           Other <Othr> [1..1] ± 2236
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2206 May 2026
```

## File page 2207

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Name <Nm> [0..1] Text 2236
       Creditor <Cdtr> [0..1] ± 2236
       CreditorAccount <CdtrAcct> [1..1]  2237
         Identification <Id> [1..1]  2237
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 2237
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2238
Or}           Other <Othr> [1..1] ± 2238
         Name <Nm> [0..1] Text 2238
Or     ChequeDetails <ChqDtls> [1..1]  2238
       Number <Nb> [0..1] Text 2239
       PayeeIdentification <PyeeId> [1..1] ± 2239
       DraweeIdentification <DrweeId> [0..1]  2239
         Party <Pty> [1..1]  2240
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2240
Or           BICFI <BICFI> [1..1] IdentifierSet C6 2240
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2241
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2242
         LEI <LEI> [0..1] IdentifierSet 2242
       DrawerIdentification <DrwrId> [0..1] ± 2243
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  2243
       Number <Nb> [0..1] Text 2243
       PayeeIdentification <PyeeId> [1..1] ± 2243
       DraweeIdentification <DrweeId> [0..1]  2244
         Party <Pty> [1..1]  2244
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2244
Or           BICFI <BICFI> [1..1] IdentifierSet C6 2245
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2245
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2246
         LEI <LEI> [0..1] IdentifierSet 2246
       DrawerIdentification <DrwrId> [0..1] ± 2247
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 2247
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2207 May 2026
```


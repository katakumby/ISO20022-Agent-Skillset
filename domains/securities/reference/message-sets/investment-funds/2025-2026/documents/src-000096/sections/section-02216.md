---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.22 CashSettlementDetails <CshSttlmDtls>"]
file_pages: [3112, 3113, 3114, 3115, 3116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.22 CashSettlementDetails <CshSttlmDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3112 to 3116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3112

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
50.4.4.9.22  CashSettlementDetails <CshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3112 May 2026
```

## File page 3113

```text
CashSettlementDetails <CshSttlmDtls> contains the following PaymentTransaction180 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  3117
{Or     PaymentCardDetails <PmtCardDtls> [1..1]  3122
       Type <Tp> [1..1] CodeSet 3123
       Number <Nb> [1..1] Text 3123
       HolderName <HldrNm> [1..1] Text 3123
       StartDate <StartDt> [0..1] YearMonth 3123
       ExpiryDate <XpryDt> [1..1] YearMonth 3123
       CardIssuerName <CardIssrNm> [0..1] Text 3123
       CardIssuerIdentification <CardIssrId> [0..1] ± 3123
       SecurityCode <SctyCd> [0..1] Text 3124
       SequenceNumber <SeqNb> [0..1] Text 3124
Or     CreditTransferDetails <CdtTrfDtls> [1..1]  3124
       Reference <Ref> [0..1] Text 3127
       Debtor <Dbtr> [0..1] ± 3127
       DebtorAccount <DbtrAcct> [0..1]  3127
         Identification <Id> [1..1]  3127
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3128
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3128
Or}           Other <Othr> [1..1] ± 3128
         Name <Nm> [0..1] Text 3129
       DebtorAgent <DbtrAgt> [0..1]  3129
         Party <Pty> [1..1]  3129
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3130
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3130
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3130
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3131
         LEI <LEI> [0..1] IdentifierSet 3131
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  3132
         Identification <Id> [1..1]  3132
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3132
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3113 May 2026
```

## File page 3114

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3133
Or}           Other <Othr> [1..1] ± 3133
         Name <Nm> [0..1] Text 3133
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  3133
         Party <Pty> [1..1]  3134
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3134
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3134
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3135
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3136
         LEI <LEI> [0..1] IdentifierSet 3136
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3137
         Identification <Id> [1..1]  3137
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3137
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3138
Or}           Other <Othr> [1..1] ± 3138
         Name <Nm> [0..1] Text 3138
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  3138
         Party <Pty> [1..1]  3139
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3139
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3139
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3140
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3141
         LEI <LEI> [0..1] IdentifierSet 3141
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3142
         Identification <Id> [1..1]  3142
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3142
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3143
Or}           Other <Othr> [1..1] ± 3143
         Name <Nm> [0..1] Text 3143
       CreditorAgent <CdtrAgt> [1..1]  3143
         Party <Pty> [1..1]  3144
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3114 May 2026
```

## File page 3115

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3144
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3144
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3145
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3146
         LEI <LEI> [0..1] IdentifierSet 3146
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  3147
         Identification <Id> [1..1]  3147
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3147
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3148
Or}           Other <Othr> [1..1] ± 3148
         Name <Nm> [0..1] Text 3148
       Creditor <Cdtr> [0..1] ± 3148
       CreditorAccount <CdtrAcct> [1..1]  3149
         Identification <Id> [1..1]  3149
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3149
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3150
Or}           Other <Othr> [1..1] ± 3150
         Name <Nm> [0..1] Text 3150
Or     DirectDebitDetails <DrctDbtDtls> [1..1]  3150
       DebtorAccount <DbtrAcct> [1..1]  3151
         Identification <Id> [1..1]  3152
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3152
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3152
Or}           Other <Othr> [1..1] ± 3153
         Name <Nm> [0..1] Text 3153
       Debtor <Dbtr> [0..1] ± 3153
       DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3153
       DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3154
       Creditor <Cdtr> [0..1] ± 3154
       DebtorAgent <DbtrAgt> [1..1]  3154
         Party <Pty> [1..1]  3154
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3115 May 2026
```

## File page 3116

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3155
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3155
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3155
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3156
         LEI <LEI> [0..1] IdentifierSet 3156
       DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3157
       CreditorAgent <CdtrAgt> [0..1]  3157
         Party <Pty> [1..1]  3157
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3158
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3158
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3158
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3159
         LEI <LEI> [0..1] IdentifierSet 3159
       CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3160
       RegistrationIdentification <RegnId> [0..1] Text 3160
       MandateIdentification <MndtId> [0..1] Text 3160
Or     ChequeDetails <ChqDtls> [1..1]  3160
       Number <Nb> [0..1] Text 3161
       PayeeIdentification <PyeeId> [1..1] ± 3161
       DraweeIdentification <DrweeId> [0..1]  3161
         Party <Pty> [1..1]  3162
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3162
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3162
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3163
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3164
         LEI <LEI> [0..1] IdentifierSet 3164
       DrawerIdentification <DrwrId> [0..1] ± 3165
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  3165
       Number <Nb> [0..1] Text 3165
       PayeeIdentification <PyeeId> [1..1] ± 3165
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3116 May 2026
```


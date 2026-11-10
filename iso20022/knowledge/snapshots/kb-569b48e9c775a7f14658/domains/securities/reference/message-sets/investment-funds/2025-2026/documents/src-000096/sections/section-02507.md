---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [3534, 3535]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# Continuation at file page 3534

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3534 to 3535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3534

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Party <Pty> [1..1]  3775
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3775
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3775
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3776
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3777
             LEI <LEI> [0..1] IdentifierSet 3777
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  3778
             Identification <Id> [1..1]  3778
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3778
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3779
Or}               Other <Othr> [1..1] ± 3779
             Name <Nm> [0..1] Text 3779
           Creditor <Cdtr> [0..1] ± 3779
           CreditorAccount <CdtrAcct> [1..1]  3780
             Identification <Id> [1..1]  3780
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3780
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3781
Or}               Other <Othr> [1..1] ± 3781
             Name <Nm> [0..1] Text 3781
Or         ChequeDetails <ChqDtls> [1..1]  3781
           Number <Nb> [0..1] Text 3782
           PayeeIdentification <PyeeId> [1..1] ± 3782
           DraweeIdentification <DrweeId> [0..1]  3782
             Party <Pty> [1..1]  3783
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3783
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3783
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3784
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3785
             LEI <LEI> [0..1] IdentifierSet 3785
           DrawerIdentification <DrwrId> [0..1] ± 3786
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  3786
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3534 May 2026
```

## File page 3535

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Number <Nb> [0..1] Text 3786
           PayeeIdentification <PyeeId> [1..1] ± 3786
           DraweeIdentification <DrweeId> [0..1]  3787
             Party <Pty> [1..1]  3787
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3787
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3788
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3788
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3789
             LEI <LEI> [0..1] IdentifierSet 3789
           DrawerIdentification <DrwrId> [0..1] ± 3790
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 3790
           AccountIdentification <AcctId> [0..1] Text 3790
           Type <Tp> [0..1] ± 3790
Or}         BlockChainCashWallet <BlckChainCshWllt> [1..1]  3791
           Identification <Id> [1..1] Text 3791
           Type <Tp> [0..1] ± 3791
           Name <Nm> [0..1] Text 3791
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3792
   ForeignExchangeDetails <FXDtls> [0..1]  3792
     UnitCurrency <UnitCcy> [1..1] CodeSet C2 3792
     QuotedCurrency <QtdCcy> [1..1] CodeSet C2 3793
     ExchangeRate <XchgRate> [1..1] Rate 3793
     QuotationDate <QtnDt> [0..1] DateTime 3793
     QuotingInstitution <QtgInstn> [0..1] ± 3794
   FinancialAdvice <FinAdvc> [0..1] CodeSet 3794
   NegotiatedTrade <NgtdTrad> [0..1] CodeSet 3794
   CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 3794
   TransactionChannelType <TxChanlTp> [0..1] ± 3795
   SignatureType <SgntrTp> [0..1] ± 3795
   OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C38 3795
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3535 May 2026
```


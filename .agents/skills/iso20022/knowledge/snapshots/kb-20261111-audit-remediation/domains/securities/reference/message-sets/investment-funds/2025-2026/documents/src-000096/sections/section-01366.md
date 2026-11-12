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
file_pages: [1904, 1905, 1906, 1907]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# Continuation at file page 1904

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1904 to 1907.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1904

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       GatingOrHoldBackDetails <GtgOrHldBckDtls> [0..1]  2047
         Type <Tp> [1..1] CodeSet 2048
         Amount <Amt> [0..1] Amount C3, C10 2049
         ExpectedReleaseDate <XpctdRlsDt> [0..1] Date 2049
         FinancialInstrumentIdentification <FinInstrmId> [0..1]  2049
{Or           ISIN <ISIN> [1..1] IdentifierSet 2050
Or           SEDOL <SEDOL> [1..1] IdentifierSet 2050
Or           CUSIP <CUSIP> [1..1] IdentifierSet 2051
Or           RIC <RIC> [1..1] IdentifierSet 2051
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 2051
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 2051
Or           CTA <CTA> [1..1] IdentifierSet 2051
Or           QUICK <QUICK> [1..1] IdentifierSet 2051
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 2051
Or           Dutch <Dtch> [1..1] IdentifierSet 2052
Or           Valoren <Vlrn> [1..1] IdentifierSet 2052
Or           Sicovam <SCVM> [1..1] IdentifierSet 2052
Or           Belgian <Belgn> [1..1] IdentifierSet 2052
Or           Common <Cmon> [1..1] IdentifierSet 2052
Or           DTI <DTI> [1..1] IdentifierSet 2052
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  2052
             Identification <Id> [1..1] Text 2053
             IdentificationSource <IdSrc> [1..1] ± 2053
         FinancialInstrumentName <FinInstrmNm> [0..1] Text 2053
         RedemptionCompletion <RedCmpltn> [0..1] CodeSet 2053
         FinalConfirmation <FnlConf> [0..1] Indicator 2053
     RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 2054
     RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 2054
     TotalSettlementAmount <TtlSttlmAmt> [0..1] Amount C3, C10 2054
     BulkCashSettlementDetails <BlkCshSttlmDtls> [0..1]  2055
       PaymentInstrument <PmtInstrm> [1..1]  2059
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1904 May 2026
```

## File page 1905

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or         CreditTransferDetails <CdtTrfDtls> [1..1]  2063
           Reference <Ref> [0..1] Text 2066
           Debtor <Dbtr> [0..1] ± 2066
           DebtorAccount <DbtrAcct> [0..1]  2066
             Identification <Id> [1..1]  2066
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2067
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2067
Or}               Other <Othr> [1..1] ± 2067
             Name <Nm> [0..1] Text 2068
           DebtorAgent <DbtrAgt> [0..1]  2068
             Party <Pty> [1..1]  2068
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2069
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2069
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2069
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2070
             LEI <LEI> [0..1] IdentifierSet 2070
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  2071
             Identification <Id> [1..1]  2071
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2071
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2072
Or}               Other <Othr> [1..1] ± 2072
             Name <Nm> [0..1] Text 2072
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  2072
             Party <Pty> [1..1]  2073
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2073
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2073
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2074
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2075
             LEI <LEI> [0..1] IdentifierSet 2075
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2076
             Identification <Id> [1..1]  2076
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1905 May 2026
```

## File page 1906

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2076
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2077
Or}               Other <Othr> [1..1] ± 2077
             Name <Nm> [0..1] Text 2077
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  2077
             Party <Pty> [1..1]  2078
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2078
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2078
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2079
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2080
             LEI <LEI> [0..1] IdentifierSet 2080
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2081
             Identification <Id> [1..1]  2081
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2081
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2082
Or}               Other <Othr> [1..1] ± 2082
             Name <Nm> [0..1] Text 2082
           CreditorAgent <CdtrAgt> [1..1]  2082
             Party <Pty> [1..1]  2083
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2083
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2083
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2084
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2085
             LEI <LEI> [0..1] IdentifierSet 2085
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  2086
             Identification <Id> [1..1]  2086
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2086
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2087
Or}               Other <Othr> [1..1] ± 2087
             Name <Nm> [0..1] Text 2087
           Creditor <Cdtr> [0..1] ± 2087
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1906 May 2026
```

## File page 1907

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           CreditorAccount <CdtrAcct> [1..1]  2088
             Identification <Id> [1..1]  2088
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2088
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2089
Or}               Other <Othr> [1..1] ± 2089
             Name <Nm> [0..1] Text 2089
Or         ChequeDetails <ChqDtls> [1..1]  2089
           Number <Nb> [0..1] Text 2090
           PayeeIdentification <PyeeId> [1..1] ± 2090
           DraweeIdentification <DrweeId> [0..1]  2090
             Party <Pty> [1..1]  2091
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2091
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2091
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2092
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2093
             LEI <LEI> [0..1] IdentifierSet 2093
           DrawerIdentification <DrwrId> [0..1] ± 2094
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  2094
           Number <Nb> [0..1] Text 2094
           PayeeIdentification <PyeeId> [1..1] ± 2094
           DraweeIdentification <DrweeId> [0..1]  2095
             Party <Pty> [1..1]  2095
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2095
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2096
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2096
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2097
             LEI <LEI> [0..1] IdentifierSet 2097
           DrawerIdentification <DrwrId> [0..1] ± 2098
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 2098
           AccountIdentification <AcctId> [0..1] Text 2098
           Type <Tp> [0..1] ± 2098
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1907 May 2026
```


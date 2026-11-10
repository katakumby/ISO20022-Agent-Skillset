---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>"]
file_pages: [2055, 2056, 2057, 2058]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2055 to 2058.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2055

```text
Note: The decimal separator is a dot.
43.4.5.13  BulkCashSettlementDetails <BlkCshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2055 May 2026
```

## File page 2056

```text
BulkCashSettlementDetails <BlkCshSttlmDtls> contains the following PaymentTransaction167
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  2059
{Or     CreditTransferDetails <CdtTrfDtls> [1..1]  2063
       Reference <Ref> [0..1] Text 2066
       Debtor <Dbtr> [0..1] ± 2066
       DebtorAccount <DbtrAcct> [0..1]  2066
         Identification <Id> [1..1]  2066
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2067
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2067
Or}           Other <Othr> [1..1] ± 2067
         Name <Nm> [0..1] Text 2068
       DebtorAgent <DbtrAgt> [0..1]  2068
         Party <Pty> [1..1]  2068
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2069
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2069
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2069
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2070
         LEI <LEI> [0..1] IdentifierSet 2070
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  2071
         Identification <Id> [1..1]  2071
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2071
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2072
Or}           Other <Othr> [1..1] ± 2072
         Name <Nm> [0..1] Text 2072
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  2072
         Party <Pty> [1..1]  2073
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2073
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2073
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2074
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2075
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2056 May 2026
```

## File page 2057

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         LEI <LEI> [0..1] IdentifierSet 2075
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2076
         Identification <Id> [1..1]  2076
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2076
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2077
Or}           Other <Othr> [1..1] ± 2077
         Name <Nm> [0..1] Text 2077
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  2077
         Party <Pty> [1..1]  2078
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2078
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2078
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2079
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2080
         LEI <LEI> [0..1] IdentifierSet 2080
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2081
         Identification <Id> [1..1]  2081
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2081
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2082
Or}           Other <Othr> [1..1] ± 2082
         Name <Nm> [0..1] Text 2082
       CreditorAgent <CdtrAgt> [1..1]  2082
         Party <Pty> [1..1]  2083
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2083
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2083
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2084
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2085
         LEI <LEI> [0..1] IdentifierSet 2085
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  2086
         Identification <Id> [1..1]  2086
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2086
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2087
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2057 May 2026
```

## File page 2058

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Other <Othr> [1..1] ± 2087
         Name <Nm> [0..1] Text 2087
       Creditor <Cdtr> [0..1] ± 2087
       CreditorAccount <CdtrAcct> [1..1]  2088
         Identification <Id> [1..1]  2088
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2088
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2089
Or}           Other <Othr> [1..1] ± 2089
         Name <Nm> [0..1] Text 2089
Or     ChequeDetails <ChqDtls> [1..1]  2089
       Number <Nb> [0..1] Text 2090
       PayeeIdentification <PyeeId> [1..1] ± 2090
       DraweeIdentification <DrweeId> [0..1]  2090
         Party <Pty> [1..1]  2091
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2091
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2091
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2092
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2093
         LEI <LEI> [0..1] IdentifierSet 2093
       DrawerIdentification <DrwrId> [0..1] ± 2094
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  2094
       Number <Nb> [0..1] Text 2094
       PayeeIdentification <PyeeId> [1..1] ± 2094
       DraweeIdentification <DrweeId> [0..1]  2095
         Party <Pty> [1..1]  2095
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2095
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2096
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2096
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2097
         LEI <LEI> [0..1] IdentifierSet 2097
       DrawerIdentification <DrwrId> [0..1] ± 2098
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2058 May 2026
```


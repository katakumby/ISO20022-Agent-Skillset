---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.34 CashSettlementDetails <CshSttlmDtls>", "49.4.5.9.34.1 PaymentInstrument <PmtInstrm>", "49.4.5.9.34.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [2881]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.34.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2881 to 2881.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2881

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  2925
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2925
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2926
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2926
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2927
       LEI <LEI> [0..1] IdentifierSet 2927
     DrawerIdentification <DrwrId> [0..1] ± 2928
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 2928
     AccountIdentification <AcctId> [0..1] Text 2928
     Type <Tp> [0..1] ± 2928
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  2929
     Identification <Id> [1..1] Text 2929
     Type <Tp> [0..1] ± 2929
     Name <Nm> [0..1] Text 2929
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2930
49.4.5.9.34.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 2882
   Number <Nb> [1..1] Text 2882
   HolderName <HldrNm> [1..1] Text 2882
   StartDate <StartDt> [0..1] YearMonth 2882
   ExpiryDate <XpryDt> [1..1] YearMonth 2882
   CardIssuerName <CardIssrNm> [0..1] Text 2882
   CardIssuerIdentification <CardIssrId> [0..1] ± 2882
   SecurityCode <SctyCd> [0..1] Text 2883
   SequenceNumber <SeqNb> [0..1] Text 2883
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2881 May 2026
```


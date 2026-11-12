---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "50.4.4.10.1 PaymentInstrument <PmtInstrm>", "50.4.4.10.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [3192]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.10.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3192 to 3192.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3192

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  3236
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3236
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3237
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3237
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3238
       LEI <LEI> [0..1] IdentifierSet 3238
     DrawerIdentification <DrwrId> [0..1] ± 3239
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 3239
     AccountIdentification <AcctId> [0..1] Text 3239
     Type <Tp> [0..1] ± 3239
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  3240
     Identification <Id> [1..1] Text 3240
     Type <Tp> [0..1] ± 3240
     Name <Nm> [0..1] Text 3240
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3241
50.4.4.10.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 3193
   Number <Nb> [1..1] Text 3193
   HolderName <HldrNm> [1..1] Text 3193
   StartDate <StartDt> [0..1] YearMonth 3193
   ExpiryDate <XpryDt> [1..1] YearMonth 3193
   CardIssuerName <CardIssrNm> [0..1] Text 3193
   CardIssuerIdentification <CardIssrId> [0..1] ± 3193
   SecurityCode <SctyCd> [0..1] Text 3194
   SequenceNumber <SeqNb> [0..1] Text 3194
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3192 May 2026
```


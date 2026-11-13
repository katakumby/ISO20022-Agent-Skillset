---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.35 CashSettlementDetails <CshSttlmDtls>", "52.4.5.10.35.1 PaymentInstrument <PmtInstrm>", "52.4.5.10.35.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [3367]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.35.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3367 to 3367.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3367

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  3411
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3411
Or         BICFI <BICFI> [1..1] IdentifierSet C7 3412
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3412
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3413
       LEI <LEI> [0..1] IdentifierSet 3413
     DrawerIdentification <DrwrId> [0..1] ± 3414
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 3414
     AccountIdentification <AcctId> [0..1] Text 3414
     Type <Tp> [0..1] ± 3414
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  3415
     Identification <Id> [1..1] Text 3415
     Type <Tp> [0..1] ± 3415
     Name <Nm> [0..1] Text 3415
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3416
52.4.5.10.35.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 3368
   Number <Nb> [1..1] Text 3368
   HolderName <HldrNm> [1..1] Text 3368
   StartDate <StartDt> [0..1] YearMonth 3368
   ExpiryDate <XpryDt> [1..1] YearMonth 3368
   CardIssuerName <CardIssrNm> [0..1] Text 3368
   CardIssuerIdentification <CardIssrId> [0..1] ± 3368
   SecurityCode <SctyCd> [0..1] Text 3369
   SequenceNumber <SeqNb> [0..1] Text 3369
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3367 May 2026
```


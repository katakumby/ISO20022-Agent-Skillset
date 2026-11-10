---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "52.4.5.12.1 PaymentInstrument <PmtInstrm>", "52.4.5.12.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [3437]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.12.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3437 to 3437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3437

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  3481
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3481
Or         BICFI <BICFI> [1..1] IdentifierSet C7 3482
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3482
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3483
       LEI <LEI> [0..1] IdentifierSet 3483
     DrawerIdentification <DrwrId> [0..1] ± 3484
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 3484
     AccountIdentification <AcctId> [0..1] Text 3484
     Type <Tp> [0..1] ± 3484
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  3485
     Identification <Id> [1..1] Text 3485
     Type <Tp> [0..1] ± 3485
     Name <Nm> [0..1] Text 3485
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3486
52.4.5.12.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 3438
   Number <Nb> [1..1] Text 3438
   HolderName <HldrNm> [1..1] Text 3438
   StartDate <StartDt> [0..1] YearMonth 3438
   ExpiryDate <XpryDt> [1..1] YearMonth 3438
   CardIssuerName <CardIssrNm> [0..1] Text 3438
   CardIssuerIdentification <CardIssrId> [0..1] ± 3438
   SecurityCode <SctyCd> [0..1] Text 3439
   SequenceNumber <SeqNb> [0..1] Text 3439
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3437 May 2026
```


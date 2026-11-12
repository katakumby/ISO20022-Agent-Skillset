---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>", "49.4.5.13.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [2951]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2951 to 2951.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2951

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  2995
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2995
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2996
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2996
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2997
       LEI <LEI> [0..1] IdentifierSet 2997
     DrawerIdentification <DrwrId> [0..1] ± 2998
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 2998
     AccountIdentification <AcctId> [0..1] Text 2998
     Type <Tp> [0..1] ± 2998
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  2999
     Identification <Id> [1..1] Text 2999
     Type <Tp> [0..1] ± 2999
     Name <Nm> [0..1] Text 2999
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3000
49.4.5.13.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 2952
   Number <Nb> [1..1] Text 2952
   HolderName <HldrNm> [1..1] Text 2952
   StartDate <StartDt> [0..1] YearMonth 2952
   ExpiryDate <XpryDt> [1..1] YearMonth 2952
   CardIssuerName <CardIssrNm> [0..1] Text 2952
   CardIssuerIdentification <CardIssrId> [0..1] ± 2952
   SecurityCode <SctyCd> [0..1] Text 2953
   SequenceNumber <SeqNb> [0..1] Text 2953
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2951 May 2026
```


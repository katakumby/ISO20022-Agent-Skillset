---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "53.4.5.18.1.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [3702]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3702 to 3702.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3702

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  3746
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3746
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3747
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3747
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3748
       LEI <LEI> [0..1] IdentifierSet 3748
     DrawerIdentification <DrwrId> [0..1] ± 3749
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 3749
     AccountIdentification <AcctId> [0..1] Text 3749
     Type <Tp> [0..1] ± 3749
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  3750
     Identification <Id> [1..1] Text 3750
     Type <Tp> [0..1] ± 3750
     Name <Nm> [0..1] Text 3750
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3751
53.4.5.18.1.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 3703
   Number <Nb> [1..1] Text 3703
   HolderName <HldrNm> [1..1] Text 3703
   StartDate <StartDt> [0..1] YearMonth 3703
   ExpiryDate <XpryDt> [1..1] YearMonth 3703
   CardIssuerName <CardIssrNm> [0..1] Text 3703
   CardIssuerIdentification <CardIssrId> [0..1] ± 3703
   SecurityCode <SctyCd> [0..1] Text 3704
   SequenceNumber <SeqNb> [0..1] Text 3704
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3702 May 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.20 CashSettlementDetails <CshSttlmDtls>", "47.4.4.8.20.1 PaymentInstrument <PmtInstrm>", "47.4.4.8.20.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [2641]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.20.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2641 to 2641.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2641

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  2685
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2685
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2686
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2686
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2687
       LEI <LEI> [0..1] IdentifierSet 2687
     DrawerIdentification <DrwrId> [0..1] ± 2688
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 2688
     AccountIdentification <AcctId> [0..1] Text 2688
     Type <Tp> [0..1] ± 2688
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  2689
     Identification <Id> [1..1] Text 2689
     Type <Tp> [0..1] ± 2689
     Name <Nm> [0..1] Text 2689
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2690
47.4.4.8.20.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 2642
   Number <Nb> [1..1] Text 2642
   HolderName <HldrNm> [1..1] Text 2642
   StartDate <StartDt> [0..1] YearMonth 2642
   ExpiryDate <XpryDt> [1..1] YearMonth 2642
   CardIssuerName <CardIssrNm> [0..1] Text 2642
   CardIssuerIdentification <CardIssrId> [0..1] ± 2642
   SecurityCode <SctyCd> [0..1] Text 2643
   SequenceNumber <SeqNb> [0..1] Text 2643
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2641 May 2026
```


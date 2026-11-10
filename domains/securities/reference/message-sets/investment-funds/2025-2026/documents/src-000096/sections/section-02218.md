---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.22 CashSettlementDetails <CshSttlmDtls>", "50.4.4.9.22.1 PaymentInstrument <PmtInstrm>", "50.4.4.9.22.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [3122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.22.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3122 to 3122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3122

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  3166
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3166
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3167
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3167
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3168
       LEI <LEI> [0..1] IdentifierSet 3168
     DrawerIdentification <DrwrId> [0..1] ± 3169
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 3169
     AccountIdentification <AcctId> [0..1] Text 3169
     Type <Tp> [0..1] ± 3169
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  3170
     Identification <Id> [1..1] Text 3170
     Type <Tp> [0..1] ± 3170
     Name <Nm> [0..1] Text 3170
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3171
50.4.4.9.22.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 3123
   Number <Nb> [1..1] Text 3123
   HolderName <HldrNm> [1..1] Text 3123
   StartDate <StartDt> [0..1] YearMonth 3123
   ExpiryDate <XpryDt> [1..1] YearMonth 3123
   CardIssuerName <CardIssrNm> [0..1] Text 3123
   CardIssuerIdentification <CardIssrId> [0..1] ± 3123
   SecurityCode <SctyCd> [0..1] Text 3124
   SequenceNumber <SeqNb> [0..1] Text 3124
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3122 May 2026
```


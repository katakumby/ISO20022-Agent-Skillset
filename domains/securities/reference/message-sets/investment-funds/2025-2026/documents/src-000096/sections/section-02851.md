---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "55.4.5.21.1.1.1 PaymentCardDetails <PmtCardDtls>"]
file_pages: [4015]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.1.1 PaymentCardDetails <PmtCardDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4015 to 4015.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4015

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Party <Pty> [1..1]  4059
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4059
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4060
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4060
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4061
       LEI <LEI> [0..1] IdentifierSet 4061
     DrawerIdentification <DrwrId> [0..1] ± 4062
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 4062
     AccountIdentification <AcctId> [0..1] Text 4062
     Type <Tp> [0..1] ± 4062
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  4063
     Identification <Id> [1..1] Text 4063
     Type <Tp> [0..1] ± 4063
     Name <Nm> [0..1] Text 4063
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4064
55.4.5.21.1.1.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
PaymentCardDetails <PmtCardDtls> contains the following PaymentCard34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 4016
   Number <Nb> [1..1] Text 4016
   HolderName <HldrNm> [1..1] Text 4016
   StartDate <StartDt> [0..1] YearMonth 4016
   ExpiryDate <XpryDt> [1..1] YearMonth 4016
   CardIssuerName <CardIssrNm> [0..1] Text 4016
   CardIssuerIdentification <CardIssrId> [0..1] ± 4016
   SecurityCode <SctyCd> [0..1] Text 4017
   SequenceNumber <SeqNb> [0..1] Text 4017
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4015 May 2026
```


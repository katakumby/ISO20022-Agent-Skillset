---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.4 Message Building Blocks", "32.4.2.10 QueryInformation <QryInf>", "32.4.2.10.4 RejectionReason <RjctnRsn>", "32.4.2.10.4.2 Proprietary <Prtry>"]
file_pages: [807, 808]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.4.2.10.4.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 807 to 808.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 807

```text
CodeName Name Definition
PRCT PercentageHoldingBreach Percentage holding breach, for example,
PPM rules; taxation rules (ERISA).
IVAG ReceivingAgent Receiving agent is not recognised or is
invalid.
NCRR SettlementAmountCurrency Unrecognised or invalid Settlement
Amount Currency.
DTRD TradeDate Unrecognised or invalid trade date or
requested trade date or future trade
date.
UPAY UnacceptedPaymentMethod Payment method, for example, cheque
or payment card, is not accepted.
URSC UnacceptedRequestedSettlementCurrency Settlement currency requested is not
supported.
32.4.2.10.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Rejected reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
32.4.2.11  RequestIssuer <ReqIssr>
Presence: [0..1]
Definition: Party that issues the request message.
RequestIssuer <ReqIssr> contains the following elements (see "PartyIdentification139" on page 5043
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
32.4.2.12  RequestRecipient <ReqRcpt>
Presence: [0..1]
Definition: Party that receives the request message.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 807 May 2026
```

## File page 808

```text
RequestRecipient <ReqRcpt> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
32.4.3 MarketPracticeVersion <MktPrctcVrsn>
Presence: [0..1]
Definition: Identifies the market practice to which the message conforms.
MarketPracticeVersion <MktPrctcVrsn> contains the following elements (see
"MarketPracticeVersion1" on page 4818 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4818
   Date <Dt> [0..1] YearMonth 4819
   Number <Nb> [0..1] Text 4819
32.4.4 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C4 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 808 May 2026
```


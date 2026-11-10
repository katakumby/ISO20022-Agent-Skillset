---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.2 Option <Optn>", "28.4.2.2.1.4.2.13 Standardisation <Stdstn>", "28.4.2.2.1.4.2.13.2 Proprietary <Prtry>"]
file_pages: [1661]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.2.13.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1661 to 1661.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1661

```text
CodeName Name Definition
instruments, expiration date and contract
size of the derivatives are not
standardised.
STAN Standardised The underlying instruments, expiration
date and contract size of the derivatives
are standardised.
28.4.2.2.1.4.2.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Standardisation expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.2.1.4.2.14  TradingPartyRole <TradgPtyRole>
Presence: [0..1]
Definition: Specifies the party which is the buyer or the seller.
TradingPartyRole <TradgPtyRole> contains one of the following OptionParty3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..*] CodeSet 1661
Or}   Proprietary <Prtry> [1..1] ± 1661
28.4.2.2.1.4.2.14.1  Code <Cd>
Presence: [1..*]
Definition: Option party expressed as an ISO 20022 code.
Datatype: "OptionParty1Code" on page 3266
CodeName Name Definition
SLLR Seller Seller in a trade.
BYER Buyer Buyer in a trade.
28.4.2.2.1.4.2.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option party expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1661 August 2026
```


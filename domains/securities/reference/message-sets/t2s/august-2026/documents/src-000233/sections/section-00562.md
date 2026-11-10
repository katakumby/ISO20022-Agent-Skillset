---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.2 Option <Optn>", "27.4.2.2.4.2.13 Standardisation <Stdstn>", "27.4.2.2.4.2.13.2 Proprietary <Prtry>"]
file_pages: [737]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.2.13.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 737 to 737.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 737

```text
CodeName Name Definition
instruments, expiration date and contract
size of the derivatives are not
standardised.
STAN Standardised The underlying instruments, expiration
date and contract size of the derivatives
are standardised.
27.4.2.2.4.2.13.2  Proprietary <Prtry>
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
27.4.2.2.4.2.14  TradingPartyRole <TradgPtyRole>
Presence: [0..1]
Definition: Specifies the party which is the buyer or the seller.
TradingPartyRole <TradgPtyRole> contains one of the following OptionParty3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..*] CodeSet 737
Or}   Proprietary <Prtry> [1..1] ± 737
27.4.2.2.4.2.14.1  Code <Cd>
Presence: [1..*]
Definition: Option party expressed as an ISO 20022 code.
Datatype: "OptionParty1Code" on page 3266
CodeName Name Definition
SLLR Seller Seller in a trade.
BYER Buyer Buyer in a trade.
27.4.2.2.4.2.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option party expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 737 August 2026
```


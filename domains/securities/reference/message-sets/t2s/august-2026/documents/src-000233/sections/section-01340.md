---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.2 Option <Optn>", "32.4.3.1.1.2.4.2.13 Standardisation <Stdstn>", "32.4.3.1.1.2.4.2.13.2 Proprietary <Prtry>"]
file_pages: [1939]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.2.13.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1939 to 1939.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1939

```text
CodeName Name Definition
instruments, expiration date and contract
size of the derivatives are not
standardised.
STAN Standardised The underlying instruments, expiration
date and contract size of the derivatives
are standardised.
32.4.3.1.1.2.4.2.13.2  Proprietary <Prtry>
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
32.4.3.1.1.2.4.2.14  TradingPartyRole <TradgPtyRole>
Presence: [0..1]
Definition: Specifies the party which is the buyer or the seller.
TradingPartyRole <TradgPtyRole> contains one of the following OptionParty3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..*] CodeSet 1939
Or}   Proprietary <Prtry> [1..1] ± 1939
32.4.3.1.1.2.4.2.14.1  Code <Cd>
Presence: [1..*]
Definition: Option party expressed as an ISO 20022 code.
Datatype: "OptionParty1Code" on page 3266
CodeName Name Definition
SLLR Seller Seller in a trade.
BYER Buyer Buyer in a trade.
32.4.3.1.1.2.4.2.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option party expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1939 August 2026
```


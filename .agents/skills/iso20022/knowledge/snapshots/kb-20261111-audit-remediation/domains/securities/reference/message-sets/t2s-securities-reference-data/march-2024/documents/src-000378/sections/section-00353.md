---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.45 SettlementInformation <SttlmInf>"]
file_pages: [446]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.45 SettlementInformation <SttlmInf>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 446 to 446.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 446

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.4.45  SettlementInformation <SttlmInf>
Presence: [0..*]
Definition: Settlement of the securities in a securities transaction, that is, the instruction to deliver or
receive securities, involving the payment of an amount of money or not.
SettlementInformation <SttlmInf> contains the following SettlementInformation17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesQuantityType <SctiesQtyTp> [0..1]  446
{Or     Code <Cd> [1..1] CodeSet 446
Or}     Proprietary <Prtry> [1..1] ± 447
   ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 447
   MinimumDenomination <MinDnmtn> [0..1] ± 447
   MinimumMultipleQuantity <MinMltplQty> [0..1] ± 447
   DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 448
13.1.6.4.45.1  SecuritiesQuantityType <SctiesQtyTp>
Presence: [0..1]
Definition: Choice between formats for the quantity of security.
SecuritiesQuantityType <SctiesQtyTp> contains one of the following SettlementUnitType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 446
Or}   Proprietary <Prtry> [1..1] ± 447
13.1.6.4.45.1.1  Code <Cd>
Presence: [1..1]
Definition: Settlement unit type expressed as an ISO 20022 code.
Datatype: "SettlementUnitType1Code" on page 523
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 446 March 2024
```


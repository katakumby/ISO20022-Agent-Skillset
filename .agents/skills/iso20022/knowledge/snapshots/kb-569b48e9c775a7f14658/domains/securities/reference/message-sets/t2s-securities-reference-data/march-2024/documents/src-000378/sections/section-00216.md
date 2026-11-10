---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.46 SettlementInformation <SttlmInf>"]
file_pages: [294]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.46 SettlementInformation <SttlmInf>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 294 to 294.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 294

```text
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
13.1.6.2.46  SettlementInformation <SttlmInf>
Presence: [0..*]
Definition: Settlement of the securities in a securities transaction, that is, the instruction to deliver or
receive securities, involving the payment of an amount of money or not.
SettlementInformation <SttlmInf> contains the following SettlementInformation17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesQuantityType <SctiesQtyTp> [0..1]  294
{Or     Code <Cd> [1..1] CodeSet 294
Or}     Proprietary <Prtry> [1..1] ± 295
   ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 295
   MinimumDenomination <MinDnmtn> [0..1] ± 295
   MinimumMultipleQuantity <MinMltplQty> [0..1] ± 295
   DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 296
13.1.6.2.46.1  SecuritiesQuantityType <SctiesQtyTp>
Presence: [0..1]
Definition: Choice between formats for the quantity of security.
SecuritiesQuantityType <SctiesQtyTp> contains one of the following SettlementUnitType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 294
Or}   Proprietary <Prtry> [1..1] ± 295
13.1.6.2.46.1.1  Code <Cd>
Presence: [1..1]
Definition: Settlement unit type expressed as an ISO 20022 code.
Datatype: "SettlementUnitType1Code" on page 523
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 294 March 2024
```


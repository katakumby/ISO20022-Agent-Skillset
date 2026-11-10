---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.3.2.46 SettlementInformation <SttlmInf>"]
file_pages: [1534]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.2.46 SettlementInformation <SttlmInf>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1534 to 1534.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1534

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
28.4.2.1.3.2.46  SettlementInformation <SttlmInf>
Presence: [0..*]
Definition: Settlement of the securities in a securities transaction, that is, the instruction to deliver or
receive securities, involving the payment of an amount of money or not.
SettlementInformation <SttlmInf> contains the following SettlementInformation17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesQuantityType <SctiesQtyTp> [0..1]  1534
{Or     Code <Cd> [1..1] CodeSet 1534
Or}     Proprietary <Prtry> [1..1] ± 1535
   ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 1535
   MinimumDenomination <MinDnmtn> [0..1] ± 1535
   MinimumMultipleQuantity <MinMltplQty> [0..1] ± 1535
   DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 1536
28.4.2.1.3.2.46.1  SecuritiesQuantityType <SctiesQtyTp>
Presence: [0..1]
Definition: Choice between formats for the quantity of security.
SecuritiesQuantityType <SctiesQtyTp> contains one of the following SettlementUnitType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1534
Or}   Proprietary <Prtry> [1..1] ± 1535
28.4.2.1.3.2.46.1.1  Code <Cd>
Presence: [1..1]
Definition: Settlement unit type expressed as an ISO 20022 code.
Datatype: "SettlementUnitType1Code" on page 3303
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1534 August 2026
```


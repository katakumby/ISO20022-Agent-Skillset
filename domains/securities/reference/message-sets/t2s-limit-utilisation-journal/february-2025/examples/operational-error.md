---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Operational error example"
domain: "securities"
source_ids: ["src-000362"]
message_sets: ["t2s-limit-utilisation-journal"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
source_locations: [{"source_id": "src-000362", "locator": "P314–P363; Business Examples; original payload excerpts"}, {"source_id": "src-000362", "locator": "Word file/printed pages22,23"}]
flow_ids: ["flow-src-000362-p137-pull-mode"]
limitations: ["These are supplied illustrative examples. Payload fragments omit BAH and document namespace wrapper; not claimed as standalone schema-valid messages."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
xml_fragment_wellformedness: "pass"
source_editions: ["february-2025"]
---

# Operational error example

Source [src-000362](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`; P314–P363. P162 says the complete instances are embedded in BAH, while the shown excerpts contain only the business message.

**P314** In this example the “LimitUtilisationJournalQuery” is used by an NCB (H) "CBHHBIC2XXX”, participating in T2S, to query via camt.064 the journal utilisation of Auto-collateralisation limits for the payment bank “PBKHBIC0XXX” on January 9th, 2015 with Limit Utilisation activity date in the future.

**P315** The result of this query is sent using “LimitUtilisationJournalReport” (camt.065) specifying the operational error resulting from the processing of this request.

**P316** In this example, the Error Code “Q065” is returned with the corresponding Error description.

## Query

[camt.064.001.01](../../../../messages/camt.064.001.01/index.md); P320–P340.

```xml
  <LmtUtlstnJrnlQry>
	 <MsgHdr>
		<MsgId>REFKLM</MsgId>
	 </MsgHdr>
	 <SchCrit>
		<LmtTp>ACOL</LmtTp>
		<JrnlActvtyDt>2015-01-21</JrnlActvtyDt>
		<BilLmtCtrPtyId>
				<Id>
					<Id>
						<AnyBIC> PBKHBIC0XXX </AnyBIC>
					</Id>
				</Id>
				<RspnsblPtyId>
					<Id>
						<AnyBIC> CBHHBIC2XXX </AnyBIC>
					</Id>
				</RspnsblPtyId>
			</BilLmtCtrPtyId>
	 </SchCrit>
	</LmtUtlstnJrnlQry>
```

## Report

[camt.065.001.01](../../../../messages/camt.065.001.01/index.md); P344–P363.

```xml
<LmtUtlstnJrnlRpt>
	<MsgHdr>
		<MsgId>NONREF</MsgId>
		<OrgnlBizInstr>
			<MsgId>REFKLM</MsgId>
		</OrgnlBizInstr>
	</MsgHdr>
	<Pgntn>
		<PgNb>1</PgNb>
		<LastPgInd>true</LastPgInd>
	</Pgntn>
		<RptOrErr>
		  <OprlErr>
			  <Err>
			    <Prtry>Q065</Prtry>
			  </Err>
			  <Desc>The specified business date is in the future</Desc>
		  </OprlErr>
		</RptOrErr>
	</LmtUtlstnJrnlRpt>
```

The example values and identifier strings are preserved exactly, including source whitespace inside AnyBIC values where present. [Source pull flow](../flows/flow-src-000362-p137-pull-mode.md).

## Review evidence

Full source scenario, numeric values, identifiers, XML labels/attributes and split boundaries compared against [Word22](../../../../../assets/src-000362/source-page-renders/word-page-22.png), [Word23](../../../../../assets/src-000362/source-page-renders/word-page-23.png). Both payload fragments parse as well-formed XML; this does not establish XSD validity without the omitted namespace/document wrapper. Checked2026-11-09.

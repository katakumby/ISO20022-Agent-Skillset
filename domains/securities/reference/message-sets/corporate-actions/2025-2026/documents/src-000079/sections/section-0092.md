---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionMovementPreliminaryAdviceCancellationAdvice seev.044.00x.13"]
content_origin: "source-transcription"
---

# CorporateActionMovementPreliminaryAdviceCancellationAdvice seev.044.00x.13

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionMovementPreliminaryAdviceCancellationAdvice seev.044.00x.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1908** CorporateActionMovementPreliminaryAdviceCancellationAdvice seev.044.00x.13

**P1909** Description

**P1910** This example describes a CorporateActionMovementPreliminaryAdviceCancellationAdvice sent by an account servicer to cancel the movements preliminary advice sent previously.

**P1911** This CorporateActionMovementPreliminaryAdviceCancellationAdvice sample message illustrates the cancellation of the movement preliminary advice message illustrated in the example 1 of the CorporateActionMovementPreliminaryAdvice section.

**P1912** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash

**P1913** Business Data

**P1914** Issue name

**P1915** Glaxo Holdings

**P1916** ISIN GB0007123466

**P1917** Terms

**P1918** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P1919** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P1920** Relative dates

**P1921** Ex date - 01 September 2010

**P1922** Record date - 07 September 2010

**P1923** Dividend payment date - 02 October 2010

**P1924** Response deadline date - 23 September 2010

**P1925** Transaction description

**P1926** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P1927** Message Instance (with application header)

**P1928** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1929** 	<Fr>

**P1930** 		<FIId>

**P1931** 			<FinInstnId>

**P1932** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1933** 			</FinInstnId>

**P1934** 		</FIId>

**P1935** 	</Fr>

**P1936** 	<To>

**P1937** 		<FIId>

**P1938** 			<FinInstnId>

**P1939** 				<BICFI>WXYZFRPP666</BICFI>

**P1940** 			</FinInstnId>

**P1941** 		</FIId>

**P1942** 	</To>

**P1943** 	<BizMsgIdr> LOCCUS0000000088</BizMsgIdr>

**P1944** 	<MsgDefIdr>seev.044.001.13</MsgDefIdr>

**P1945** 	<CreDt>2010-09-15T17:30:00Z</CreDt>

**P1946** </AppHdr>

**P1947** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.044.001.13" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1948** <CorpActnMvmntPrlimryAdvcCxlAdvc>

**P1949** 	<MvmntPrlimryAdvcId>

**P1950** 		<Id>LOCCUS0000000076</Id>

**P1951** 	</MvmntPrlimryAdvcId>

**P1952** 	<CorpActnGnlInf>

**P1953** 		<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P1954** 		<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1955** 		<EvtTp>

**P1956** 			<Cd>DVOP</Cd>

**P1957** 		</EvtTp>

**P1958** 		<MndtryVlntryEvtTp>

**P1959** 			<Cd>CHOS</Cd>

**P1960** 		</MndtryVlntryEvtTp>

**P1961** 		<FinInstrmId>

**P1962** 			<ISIN>GB0007123466</ISIN>

**P1963** 			<Desc>GLAXO HOLDINGS</Desc>

**P1964** 		</FinInstrmId>

**P1965** 	</CorpActnGnlInf>

**P1966** 	<AcctDtls>

**P1967** 		<AcctsList>

**P1968** 			<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P1969** 		</AcctsList>

**P1970** 	</AcctDtls>

**P1971** </CorpActnMvmntPrlimryAdvcCx>

**P1972** </Document>

**P1974** Revision Record

[T30 - complete table](../tables/tbl-0030.md)

**P1975** Disclaimer

**P1976** Although the Registration Authority has used all reasonable efforts to ensure accuracy of the contents of the iso20022.org website and the information published thereon, the Registration Authority assumes no liability whatsoever for any inadvertent errors or omissions that may appear thereon. Moreover, the information is provided on an "as is" basis. The Registration Authority disclaims all warranties and conditions, either express or implied, including but not limited to implied warranties of merchantability, title, non-infringement and fitness for a particular purpose.

**P1977** The Registration Authority shall not be liable for any direct, indirect, special or consequential damages arising out of the use of the information published on the iso20022.org website, even if the Registration Authority has been advised of the possibility of such damages.

**P1978** Intellectual Property Rights

**P1979** The ISO 20022 MessageDefinitions described in this document were contributed by SWIFT. The ISO 20022 IPR policy is available at www.ISO20022.org > About ISO 20022 > Intellectual Property Rights.

